# 아이템 30. 이왕이면 제네릭 메서드로 만들라

클래스와 마찬가지로, 메서드도 제네릭으로 만들 수 있다. 매개변수화 타입을 받는 정적 유틸리티 메서드는 보통 제네릭이다. 예컨대 Collections의 알고리즘 메서드는 모두 제네릭이다.


두 집합의 합집합을 반환하는 문제가 있는 메소드
raw type 사용 - 수용 불가
```Java
public static Set union(Set s1, Set s2) {
	Set result = new HashSet(s1);
	result.addAll(s2);
	return result;
}
```

컴파일은 되지만 경고가 2개 발생한다.

```
Union. java:5: warning: [unchecked] unchecked call to HashSet (Collection‹? extends E>) as a member of raw type HashSet
Set result = new HashSet (s1);

Union.java:6: warning: [unchecked] unchecked call to addAll (Collections? extends E>) as a member of raw type Set
result.addAll(s2);

```

(타입 매개변수들을 선언하는) 타입 매개변수 목록은 메서드의 제한자와 반환 타입 사이에 온다.

```Java
public static <E> Set<E> union(Set<E> s1, Set<E>s2) {
  Set<E> result = new HashSet<>(s1);
  result.addAll(s2);
  return result;
}
```

제네릭은 런타임에 타입 정보가 소거되므로 하나의 객체를 어떤 타입으로든 매개변수화 할 수 있다. 하지만 이렇게 하려면 요청한 타입 매개변수에 맞게 배번 그 객체의 타입을 바꿔주는 정적 팩토리를 만들어야함.

제네릭 싱글톤 팩토리

```Java
private static UnaryOperator<Object> IDENTITY_FN = (t) -> t;

@SuppressWarnings("unchecked")
public static <T> UnaryOperator<T> identityFunction() {
	return (UnaryOperator<T>) IDENTITY_FN;
}
```


제네릭 싱글톤 사용 예시`
```Java
public static void main(String[] args) {
	String[] strings = { "삼베", "대마", "나일론"};
	UnaryOperator<String> sameString = identityFunction();
	for (String s: strings) {
		System.out.println(sameString.apply(s));
	}

	Number[] numbers = { 1, 2.0, 3L };
	UnaryOperator<Number> sameNumber = identityFunction();
	for (Number n : numbers) {
		System.out.println(sameNumber.apply(n));
	}
}
```

상대적으로 드물긴 하지만, 자기 자신이 들어간 표현식을 사용하여 타입 매개변수의 허용 범위를 한정할 수 있다. 바로 재귀적 타입 한정 (recursive type bound)이라는 개념이다.

재귀적 타입 한정은 주로 타입의 자연적 순서를 정하는 Comparable interface와 함께 쓰인다.
예를 살펴보자.

```Java
public interface Comparable<T> {
  int compareTo(T o);
}

```


재귀적 타입 한정을 이용해 상호 비교할 수 있음 을 표현
```Java
public static <E extends Comparable<E>> E max(Collection<E> c);
```

구현 예시
```Java
public static <E extends Comparable<E>> E max(Collection<E> c) {
 if (c.isEmpty()) {
   throw new IllegalArgumentException("컬렉션이 비어 있습니다.");
   E result = null;
   for (E e : c) {
     if (result == null || e.compareTo(result) > 0) {
       result = Objects.requireNonNull(e);
		} 
   }
   return result;
 }
}
```


### 핵심 정리
제네릭 타입과 마찬가지로, 클라이언트에서 입력 매개변수와 반환값을 명시적으로 형변환해야하는 메서드보다 제네릭 메서드가 더 안전하며 사용이 쉽다.

타입과 마찬가지로, 메서드도 형변환 없이 사용할 수 있는 편이 좋으며, 많은 경우 그렇게 하려면 제네릭메서드가 되어야 한다.
형변환을 해야하는 메소드는 제네릭하게 만들자.
