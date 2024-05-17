# 아이템 31. 한정적 와일드카드를 사용해 API 유연성을 높이라.

매개변수화 타입은 불공변 (invariant)이다. 즉, 서로 다른 타입 Type1과 Type2가 있을 때, List<Type1>은 List<Type2>의 하위 타입도 상위 타입도 아니다.

-> List<String>은 List<Object>가 하는 일을 제대로 수행하지 못하니 하위 타입이 될 수 없다. (리스코프 치환 원칙에 어긋난다.)


와일드카드 타입을 사용하지 않은 pushAll method 예시

```Java
public void pushAll(Iterable<E> src) {
	for (E e : src) {
		push(e);
	}
}
```

컴파일 되고, Iterable src의 원소 타입이 스택의 원소타입과 일치하면 잘 작동한다. 하지만 Stack<Number>로 선언한 후 pushAll(intVal)을 호출하면 어떻게 될까?

```Java
Stack<Number> numberStack = new Stack<>();
Iterable<Integer> integers = ...;
numberStack.pushAll(integers);
```

하지만 실제로는 다음의 오류 메세지가 뜬다. 매개변수화 타입이 불공변이기 때문이다.

자바는 한정적 와일드카드 타입이라는 것을 지원함.

```Java
public void pushAll(Iterable<? extends E> src) {
  for (E e : src) {
      push(e);
  }
}
```

Stack과 Stack을 사용하는 클라이언트 코드도 컴파일된다. 


```Java
public void popAll(Collection<? super E> dst) {
  while (!isEmpty()) {
    dst.add(pop());
  }
}
```

**유연성을 극대화하려면 원소의 생산자나 소비자용 입력 매개변수에 와일드카드 타입을 사용하라.**
입력 매개변수가 생산자와 소비자 역할을 동시에 한다면, 와일드카드 타입을 써도 좋을 게 없다. 타입을 정확히 지정해야 하는 상황으로, 이때는 와일드 카드 타입을 쓰지 말아야한다.


PECS(producer-extends, consumer-super)
: 매개변수화 타입 T가 생산자라면 <? extends T>를 사용하고, 소비자라면 <? super T>를 사용하라. Stack 예에서 pushAll의 src 매개변수는 Stack이 사용할 E 인스턴스를 생산하므로 src의 적절한 타입은 `Iterable<? extends E>` 이다.

한편 popAll의 dst 매개변수는 Stack으로부터 E 인스턴스를 소비하므로 dst의 적절한 타입은 Collection<? super E>이다.

아이템 28의 Chooser
```Java
public Chooser(Collection<T> choices)
```

생성자 매개변수에 와일드카드 타입 적용
```Java
public Chooser(Collection<? extends T> choices)
```

차이점
- 수정 전 생성자로는 컴파일 조차 안되지만, 한정적 와일드카드 타입으로 선언한 수정 후에 생성자에서는 문제가 사라진다.


```Java
public static <E> Set<E> union(Set<E> s1, Set<E> s2) 
```

s1, s2 모두 E의 생산자이니 PECS 공식에 따라 다음처럼 선언해야 한다.
```Java
public static <E> Set<E> union(Set<? extends E> s1, Set<? extends E> s2) 

```
반환 타입은 여전히 Set<E>이다. 반환 타입에는 **한정적 와일드카드 타입을 사용하면 안된다.** 유연성을 높여주기는 커녕 클라이언트코드에서도 와일드카드 타입을 써야하기 때문이다.

제대로 사용하면 사용자는 와일드카드 타입을 썼다는 사실 조차 인식하지 못한다.

** 클래스 사용자가 와일드 카드 타입을 신경써야 하면 해당 API는 문제 있을 가능성이 크다.**

```Java
public static <E extends Comparable<E>> E max(List<E> list) {

}
```


다음은 와일드카드 타입을 사용해 다듬은 모습이다.

```Java
public static <E extends Comparable<? super E>> E max(List<? extends E> list)
```

Comparable은 언제나 소비자이므로, 일반적으로 Comparable<E> 보다는 Comparable<? super E>를 사용하는 편이 낫다.

일반적으로 Comparator<E> 보다는 Comparator<? super E>를 사용하는 편이 낫다.
![image](https://github.com/unanchoi/TIL/assets/81692211/13af87bf-2911-4142-ba50-0ae980671e6b)



### 타입 매개변수와 와일드카드 선언
기본 규칙 : 메서드 선언에 타입 매개변수가 한 번만 나오면 와일드카드로 대체하라.


```Java
public static void swap(List<?> list, int i, int j) {
  swapHelper(list, i, j);
}

// 와일드카드 타입을 실제 타입으로 바꿔주는 private 도우미 메서드
private static <E> void swapHelper(List<E> list, int i, int j) {
  list.set(i, list.set(j, list.get(i)));
}
```


### 핵심정리
복잡하더라도 와일드카드 타입을 적용하면 API가 훨씬 유연해짐.
널리 쓰일 라이브러리를 작업한다면 와일드카드 타입을 적절히 사용하자.

#### PECS 공식
생산자는 extends를 소비자는 super를

Comparable, Comparator 모두 소비자임.
