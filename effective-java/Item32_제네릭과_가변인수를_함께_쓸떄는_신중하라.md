# 아이템 32. 제네릭과 가변인수를 함께 쓸 때는 신중하라.

가변인수(varargs)는 메서드에 넘기는 인수의 개수를 클라이언트가 조절할 수 있게 해주는데, 구현 방식에 허점이 있음.
가변인수 메서드를 호출하면 가변인수를 담기 위한 배열이 자동으로 하나 만들어짐.

매개변수화 타입의 변수가 타입이 다른 객체를 참조하면 힙 오염이 발생한다.


제네릭과 varargs를 혼용하면 타입 안정성이 깨진다.

```Java
static void dangerous(List<String>... stringLists) {
  List<Integer> intList = List.of(42);
  Object[] objects = stringLists;
  objects[0] = intList;  // 힙 오염 발생
  String s = stringLists[0].get(0) // ClassCastException
}
```

이 메서드는 형변환하는 곳이 보이지 않지만, ClassCastException을 던진다. 마지막 줄에 컴파일러가 생성한 형변환이 숨어 있기 때문.
따라서 제네릭 varargs 배열 매개변수에 값을 저장하는 것은 안전하지 않다.

자바 7의 `@SafeVarargs` 애너테이션은 메서드 작성자가 그 메서드가 타입 안전함을 보장하는 장치다. 컴파일러는 이 약속을 믿고, 그 메서드가 안전하지 않을 수 있다는 경고를 더이상 하지 않는다.

하지만 메서드가 안전한게 확실하지 않다면, 애너테이션을 달아서는 안된다.

안전한지 확신하는 방법은 ?
-> 가변인수 메서드를 호출할 때 varargs 매개변수를 담는 제네릭 배열이 만들어진다는 사실을 기억하자. 메서드가 이 배열에 아무것도 저장하지 않고 그 배열의 참조가 밖으로 노출되지 않는다면(신뢰할 수 없는 코드가 배열에 접근할 수 없다면) 타입 안전하다.


자신의 제네릭 매개변수 배열의 참조를 노출한다. <- 안전하지 않다!
```Java
static <T> T[] toArray(T... args) {
 return args;
}
```

```Java
static <T> T[] pickTwo(T a, T b, T c) {
switch (ThreadLocalRandom.current().nextInt(3)) {
  case 0: return toArray(a, b);
  case 1: return toArray(a, c);
  case 2: return toArray(b, c);
}
  throw new AssertionError(); // 도달할 수 없다.
}
```

pickTwo는 Object[] 타입 배열을 반환한다.


```Java
public static void main（String[] args） {

String[] attributes = pickTwo（"좋은", "빠른", "저렴한"）;
}
```
-> 컴파일은 되지만 `ClassCastException`을 던진다. 형변환하는 곳이 보이지 않는데도 말이다.
무엇을 놓친 것일까? pickTwo의 반환값을 attributes에 저장하기 위해 String[]로 형변환하는 코드를 컴파일러가 자동 생성한다는 점을 놓쳤다. Object[]는 String[]의 하위 타입이 아니므로 형변환에 실패한다.

`제네릭 varargs 매개변수 배열에 다른 메서드가 접근하도록 허용하면 안전하지 않다` 

예외
1. `@SafeVarargs`로 제대로 애노테이트된 또 다른 varargs 메서드에 넘기는 것은 안전하다.
2. 배열 내용의 일부 함수를 호출만 하는 일반 메서드에 넘기는 것도 안전하다.


제네릭 varargs 매개변수를 안전하게 사용하는 메서드
```Java
@SafeVarargs
static <T> List<T> flatten(List<? extends T> ...lists) {
  List<T> result = new ArrayList<>();
    for (List<? extends T> list: lists)
      result.addAll(list);
  return result;
}
```

@SafeVarargs 애너테이션을 사용해야 할 때를 정하는 규칙은 간단함.
`제네릭이나 매개변수화 타입의 varargs 매개변수를 받는 모든 메서드에 @SafeVarargs를 달라.`
-> 안전하지 않은 varargs 메서드는 절대 작성하지 말자.

다음 두 가지를 어기면 수정해야함.
- varargs 매개변수 배열에 아무 것도 저장하지 않는다.
- 그 배열을 신뢰할 수 없는 코드에 노출하지 않는다.

제네릭 varargs 매개변수를 List로 대체한 예시 - 타입 안전하다.
```Java
static <T> List<T> flatten(List<List<? extends T>> lists) {
  List<T> result = new ArrayList();
  for (List<? extends T> list: lists) {
    result.addAll(list);
  }
  return result;
}
```

정적 팩터리 메서드인 `List.of`를 활용하면 다음 코드와 같이 이 메서드에 임의 개수의 인수를 넘길수 있다. 이렇게 사용하는게 가능한 이유는 List.of에도 @SafeVarargs 애너테이션이 달려 있기 때문이다.

`audience = flatten(List.of(friends, romans, coutrymen));`

@SafeVarargs 애너테이션을 직접 달아주지 않아도 되고, 실수로 안전하다고 판단할 걱정도 없다.
단점 : 클라이언트 코드가 지저분해짐.


```Java
static <T> List<T> pickTwo(T a, T b, T c) {
  switch(ThreadLocalRandom.current().nextInt(3)) {
    case 0: return List.of(a,b);
    case 1: return List.of(a,c);
    case 2: return List.of(b,c);
  }
  throw new AssertionError();
}
```

main method는 다음과 같이 변함.
```Java
public static void main（String[] args） {
 List<String> attributes = pickTwo（"좋은", "빠른", "저렴한"）;
}
 
```
결과 코드는 배열없이 제네릭만 사용하므로 타입 안전하다.

### 핵심정리
가변인수와 제네릭은 궁합이 좋지 않다. 가변인수 기능은 배열을 노출하여 추상화가 완벽하지 못하고, 배열과 제네릭의 타입 규칙이 서로 다르기 때문이다. 제네릭 varargs 매개변수는 타입 안전하지는 않지만 허용된다. 메서드에 제네릭(or 매개변수화된) varargs 매개변수를 사용하고자 한다면, 먼저 그 메서드가 타입 안전한지 확인한 다음 `@SafeVarargs` 애너테이션을 달아 사용하는 데 불편함이 없게끔 하자.
