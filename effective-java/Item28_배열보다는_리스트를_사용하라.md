# 아이템 28. 배열보다는 리스트를 사용하라.


### 1. 배열은 공변.
배열 : 공변(covariant)
제네릭은 불공변(invariant)이다.
즉, 서로 다른 타입 Type1, Type2가 있을 때 List<Type1>은 List<Type2>의 하위 타입도 아니고 상위 타입도 아니다.


런타임에 실패하는 예시.
```Java
Object[] objectArray = new Long[1];
objectArray[0] = "타입이 달라 넣을 수 없다."; // ArrayStoreException을 던진다.
```

컴파일되지 않는 예시.
```Java
List<Object> ol = new ArrayList<Long>(); 
or.add("타입이 달라 넣을 수 없다.");
```

어느 쪽이든 Long용 저장소에 String을 넣을 수 없다.

### 2. 배열은 실체화(reify)된다.

배열은 Runtime에서도 자신이 담기로한 원소의 타입을 확인한다.
하지만 제네릭은 타입 정보가 런타임에는 소거(erasure)된다.

따라서 배열과 제네릭은 잘 어우러지지 못함.
배열은 제네릭, 매개변수화 타입, 타입 매개변수로 사용할 수 없음.

`new List<E>[]` , `new List<String>[]`, `new E[]` 식으로 작성하면 컴파일할 때 제네릭 배열 생성 오류를 일으킨다.

제네릭 배열을 만들지 못하게 막은 이유 ? -> 타입이 안전하지 않기 때문.
만약 가능하면, 컴파일러가 자동 생성한 형변환 코드에서 런타임에 `ClassCastException`이 발생할 수 있따. 런타임에 ClassCastException이 발생하는 일을 막아주겠다는 제네릭 타입 시스템의 취지에 어긋남.


제네릭 배열 생성을 허용하지 않는 이유 - 컴파일되지 않는 코드 예시.
```Java
List<String>[] stringList = new List<String>[1]; // (1) 
List<Integer> intList = List.of(42); // (2)
Object[] objects = stringLists; // (3)
objects[0] = intList; // (4)
String s = stringLists[0].get(0); // (5)
```

제네릭 배열을 생성하는 (1)이 허용된다고 가정.
(2)는 원소가 하나인 List<Integer>를 생성한다.
(3)은 (1)에서 생성한 List<String>의 배열을 Object배열에 할당한다.
배열은 공변이니 문제없다.


(4)는 (2)에서 생성한 List<Integer>의 인스턴스를 Object 배열의 첫 원소로 저장한다. 제네릭은 소거 방식으로 구현되어서 이 역시 성공한다. 즉, 런타임에는 List<Integer> 인스턴스 타입은 단순히 List가 되고, List<Integer>[]의 인스턴스 타입은 List[]가 된다. 따라서 (4)에도 ArrayStoreException을 일으키지 않는다.

List<String> 인스턴스만 담겠다고 선언한 stringLits 배열에는 지금 List<Integer> 인스턴스가 저장돼 있다. 그리고 (5)는 이 배열의 처음 리스트에서 첫 원소를 꺼내려고 한다.
컴파일러는 꺼낸 원소를 자동으로 String으로 형변환하는데, 이 원소는 Integer이므로 런타임에 ClassCastException이 발생한다. 이런 일을 방지하려면 
(제네릭 배열이 생성되지 않도록) (1)에서 컴파일 오류를 내야한다.

`E` , `List<String>`, `List<E>`  와 같은 타입을 실체화 불가 타입(non-reifiable type) 이라고 한다.

쉽게 말해, 실체화되지 않아서 런타임에는 컴파일타임보다 타입 정보를 적게 가지는 타입이다.


---
배열로 형변환할 때 제네릭 배열 생성 오류, 비검사 형변환 경고가 뜨는 경우 대부분은 배열인 E[] 대신 컬렉션인 List<E>를 사용하면 해결됨.

코드가 복잡해지고 성능이 나빠질 수 있지만, 타입 안정성과 상호 운영성이 좋아짐.


제네릭을 적용해야하는 예시
```
public class Chooser {

private final Objectl] choiceArray;

public Chooser(Collection choices) {

choiceArray = choices. toArray);

｝

public Object choose() {

Random rnd = ThreadLocalRandom. current);

return choiceArray [rnd.nextInt(choiceArray. length)];

}
```


```Java
public class Chooser<T> {
  private final List<T> choiceList;

 public Chooser(Collection<T> choices) {
	 choiceList = new ArrayList<>(choices);
 }

public T choose() {
	Random rnd = ThreadLocalRandom.current();
	  return choiceList.get(rnd.nextInt(choiceList.size()))
}

}
```

### 핵심 정리
배열은 공변, 실체화 됨.
베네릭은 불공변, 타입 정보가 소거.

배열은 런타임에는 타입 안전, 컴파일때는 아님.
제네릭은 반대임.

따라서 섞어 쓰기 어려움.  따라서 컴파일 오류나 경고를 만나면 가장 먼저 배열을 리스트로 대체하는 방법을 적용하자.
