
# 아이템 33: 타입 안전 이종 컨테이너를 고려하라
제네릭은 Set<E>, Map<K, V> 등의 컬렉션과 ThreadLocal<T> , AtomicReference<T> 등의 단일원소 컨테이너에도 흔히 쓰인다.

이런 모든 쓰임에서 매개변수화되는 대상은 (원소가 아닌) 컨테이너 자신이다. 따라서 하나의 컨테이너에서 매개변수화할 수 있는 타입의 수가 제한된다.

컨테이너의 일반적인 용도에 맞게 설계된 것이니 문제될 건 없다.


### 타입 안전 이종 컨테이너 패턴(type safe heterogeneous container pattern)
- 컨테이너 대신 키를 매개변수화한 다음, 컨테이너에 값을 넣거나 뺄 때 매개변수화한 키를 함께 제공하면 된다. 이렇게 하면 제네릭 타입 시스템이 값의 타입이 키와 같음을 보장해준다.

예시) 타입별로 즐겨 찾는 인스턴스를 저장하고, 검색할 수 있는 Favorites 클래스


타입 안전 이종 컨테이너 패턴
```Java
public class Favorites {
  public <T> void putFavorite(Class<T> type, T instance);
  public <T> T getFavorite(Class<T> type);
}
```

타입 안전 이종 컨테이너 패턴
```Java
public static void main(String[] args) {

Favorites f = new FavoritesO;

f.putFavorite(String.class, "Java”);

f.putFavorite(Integer.class, Oxcafebabe);

f.putFavorite(Class.class, Favorites.class);

String favoriteSt ring = f.getFavo rite(St ring.class);

int favoriteInteger = f.getFavorite(Integer.class);

Class<?> favoriteClass = f.getFavorite(Class.class);

System.out.printf("%s %x %s%n", favoritestring,

favoriteinteger； favoriteClass.getName());

}
```

참고) Java와 printf가 C의 printf와 다른 점이 하나 있다. 이 코드에서는 만약 C였다면 \n을 썼을 곳에 %n을 썼는데, 이 %n은 플랫폼에 맞는 줄바꿈 문자로 자등으로 대체된다.


Favorites 인스턴스는 타입 안전함. -> 타입 안전 이종 컨테이너


타입안전 이종 컨테이너 패턴 - 구현
```Java
public class Favorites {
     private Map<Class<?>, Object> favorites = new HashMap<>();
 
	public <T> void putFavorite(Class <T> type, T instance) {
	  favorites.put(Objects.requireNonNull(type), instance);
	}
	
	 public <T> T getFavorite(Class<T> type) {
	   return type.cast(favorites.get(type));
	 }
}
```

- 와일드 카드가 중첩되어 있음.
- 모든키가 서로다른 매개변수화가 타입일 수 있다. 
- Favorites 맵의 값 타입은 단순히 Object이다. 맵은 키와 값 사이의 타입 관계를 보증하지 않는다.


cast 메서드가 단지 인수를 그대로 반환하는데 사용하는 이유 ? -> cast 메서드의 시그니처가 Class가 제네릭이라는 점을 활용

```Java
public class Class<T> {
  T cast(Object obj);
}

### Favorite 클래스에 알아두어야할 제약

1. 악의적인 클라이언트가 Class 객쳋를 로 타입으로 넘기면 Favorites 인스턴스의 타입 안정성이 쉽게 깨진다. 하지만 이렇게 짜여진 클라이언트 코드에서는 컴파일할 때 비검사 경고가 뜬다.

동적 형변환으로 런타임 타입 안정성 확보
```Java
public <T> void putFavorite(Class<T> type, T instance) {
  favorites.put(Objects.requireNonNull(type), type.cast(instance));
}
```

java.util.Collections에 `checkedSet`, `checkedList`, `checkedMap` 같은 메서드들이 이 방식을 적용한 컬렉션 래퍼들이다.

이 정적 팩터리들은 컬렉션과 함께 1개의 Class 객체를 받는다. 이 메서드들은 모두 제네릭이라 Class 객체와 컬렉션의 컴파일타임 타입이 같음을 보장한다. 
예컨대 런타임에 Coin을 `Collection<Stamp>` 에 넣으라하면 `ClassCastException`을 던진다. 이 래퍼들은 제네릭과 로 타입을 섞어 사용하는 애플리케이션에서 클라이언트 코드가 컬렉션에 잘못된 타입의 원소를 넣지 못하게 추적하는 도움울 줌.

2. 실체화 불가 타입에는 사용할 수 없다는 것이다.
다시 말해, 즐겨찾는 String이나 String[]은 저장할 수 있어도 즐겨 찾는 List<String>은 저장할 수 없다.


참고 :
두 번째 제약을 슈퍼타입토큰으로 해결하려는 시도가 있다.
Spring에서는 ParameterizedTypeReference라는 클래스를 미리 구현해둠.


Favorites가 사용하는 타입 토큰은 비한정적임.
getFavorites과 putFavorite은 어떤 Class 객체든 받아들임.

애너테이션 API는 한정적 타입 토큰을 적극적으로 사용한다.

```Java
public <T extends Annotation> T getAnnotation(Class<T> annotationType);
```

여기서 annotationType 인수는 애너테이션 타입을 뜻하는 한정적 타입 토큰이다.

asSubclass 메소드는 호출된 인스턴스 자신의 Class 객체를 인수가 명시한 클래스로 형변환한다.
형변환에 성공하면 인수로받은 클래스 객체를 반환하고, 실패하면 ClassCastException을 던진다.

asSubclass를 사용해 한정적 타입 토큰을 안전하게 형변환한다.
```Java
static Annotation getAnnotation(AnnotatedElement element, String annotationTypeName) {
  Class<?> annotationType = null; // 비한정적 타입 토큰
try {
  annotationType = Class.forName(annotationTypeName);
  } catch (Exception ex) {
    throw new IllegalArgumentException(ex);
  }
  return element.getAnnotation(annotationType.asSubclass(Annotation.class));
}

```

### 핵심정리
컬렉션 API 로 대표되는 일반적인 제네릭 형태에서는 한 컨테이너가 다룰 수 있는 타입 매개변수의 수가 고정되어 있다.

하지만 컨테이너 자체가 아닌 키를 타입 매개변수로 바꾸면 이런 제약이 없는 타입 안전 이종 컨테이너를 만들 수 있다. 타입 안전 이종 컨테이너는 Class를 키로 쓰며, 이런 식으로 쓰이는 `Class 객체를 타입 토큰`이라 한다.
예컨대 데이터베이스의 행을 표현한 DatabaseRow 타입에는 제네릭 타입인 Column<T> 키로 사용할 수 있다.
