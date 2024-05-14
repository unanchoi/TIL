# 아이템 29. 이왕이면 제네릭 타입으로 만들라.


Object 기반 스택 - 제네릭이 절실한 강력 후보
```Java
public class Stack {
private Object[] elements;
private int size = 0;
private static final int DEFAULT_INITIAL_CAPACITY = 16;

public Stack() {
	elements = new Object[DEFAULT_INITIAL_CAPACITY];
}

public void push(Object e) {
	ensureCapacity();
	elements[size++] = e;
}

public Object pop() {
	if (size == 0) {
		throw new EmptyStackException();
	}
	
	Object result = elements[--size];
	elements[size] = null;
	return result;
}

public boolean isEmpty() {
	return size == 0;
}

private void ensureCapacity() {
	if (elements.length == size) {
		elements = Arrays.copyOf(elements, 2 * size + 1)l
	}
}

}
```

해당 클래스가 제네릭이 아니기 때문에, 클라이언트는 스택에서 꺼낸 객체를 형변환해야하는데 이때 런타임 오류가 날 위험이 있다.

일반 클래스를 제네릭 클래스로 만드는 방법
1. 클래스 선언에 타입 매개변수를 추가하는 것.

주의점
- E와 같은 실체화 불가능한 타입으로 배열을 만들 수 없다.
```Java
public Stack() {
	elements = new E[DEFAULT_INITIAL_CAPACITY];
}
```

=> 
1. 제네릭 배열 생성을 금지하는 제약을 우회한다.
	- 가독성이 좋음. 배열의 타입을 E[]로 선언하여 오직 E타입 인스턴스만 받는다는 것을 어필할 수 있고, 코드가 짧다.
	- 형변환을 배열 생성시에 한번만 해주면 됨.
	- 하지만 배열의 런타임 타입이 컴파일타입과 달라 힙 오염(heap pollution)을 일으킨다.
```Java
// 배열 element는 push(E)로 넘어온 E인스턴스만 담는다.
// 따라서 타입 안정성을 보장하지만,
// 이 배열의 런타임 타입은 E[]가 아닌 Object[]다!
@SuppressWarnings("unchecked")
public Stack() {
  elements = (E[]) new Object[DEFAULT_INITIAL_CAPACITY];
}
```
2. elements 필드의 타입을 E[]에서 Object[]로 바꾸는 것.
	- 배열에서 원소를 읽을때마다 해줘야함.

```Java
// 비검사 경고를 적절히 숨긴다.
public E pop() {
	if (size == 0) {
		throw new EmptyStackException();
	}

	// push에서 E Type만 허용하므로 이 형변환은 안전하다.
	@SuppressWarnings("unchecked") E result = (E) elements[--size];
	elements[size] = null;
	return result;
}

```

아이템 28인 배열보다는 리스트를 우선하라와 모순되어 보이지만, 제네릭 타입안에서 리스트를 사용하는게 항상 가능하지도 않고, 꼭 좋은 것이 아닐 수 있다. ArrayList같은 제네릭 타입도 결국은 기본 타입인 배열을 사용해 구현, HashMap 같은 제네릭 타입은 성능을 목적으로 배열을 사용하기도 함.

제네릭 Stack을 사용하는 예시
```Java
public static void main(String[] args) {
	Stack<String> stack = new Stack<>();
	for (String arg: args) {
		stack.push(arg);
	}
	while (!stack.isEmpty()) {
		System.out.println(stack.pop().toUpperCase());
	}

}
```

### 핵심정리

클라이언트에서  직접 형변환해야하는 타입 보다 제네릭 타입이 더 안전하고 쓰기 편하다. 그러니 새로운 타입을 설계할 때는 형변환 없이도 사용할 수 있도록 하라.
기존 타입 중 제네릭이었어야 하는 것이 있다면 제네릭으로 변경하자.
