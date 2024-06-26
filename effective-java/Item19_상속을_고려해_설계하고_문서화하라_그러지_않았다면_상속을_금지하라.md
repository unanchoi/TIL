# 아이템 19. 상속을 고려해 설계하고 문서화하라. 그러지 않았다면 상속을 금지하라.

### 1. 메서드를 재정의하면 어떤 일이 일어나는지 정확히 정리하여 문서화 -> 상속용 클래스는 재정의할 수 있는 메소드들을 내부적으로 어떻게 이용하는지(자기사용) 문서로 남겨야 한다.

`Implementation Requirements` -> 메서드의 내부 동작방식을 설명하는 곳
`@implSpec` 태그를 붙여주면 자바독 도구가 생성해준다.


예시

`java.util.AbstractCollection`
```Java
	public boolean remove(Object o);
	
	
주어진 원소가 이 컬렉션 안에 있다면 그 인스턴스를 하나 제거한다.(선택적 동작) 더 정확하게 말하면, 이 컬렉션 안에 ‘Object.equals（o, e）가 참인 원소’ e가 하나 이상 있다면 그 중 하나를 제거한다. 주어진 원소가 컬렉션 안에 있었다면（즉,  호출 결과 이 컬렉션이 변경됐다면） true를 반환한다.

Implementation Requirements： 이 메서드는 컬렉션을 순회하며 주어진 원소를 찾도록 구현되었다. 주어진 원소를 찾으면 반복자의 remove 메서드를 사용해 컬렉션에서 제거한다. 이 컬렉션이 주어진 객체를 갖고 있으나, 이 컬렉션의 iterator 메서드가 반환한 반복자가 remove 메서드를 구현하지 않았다면 UnsupportedOperationException을 던지니 주의하자.

```

클래스를 안전하게 상속할 수 있도록 하려면 내부 구현 방식을 설명해야함. (캡슐화를 해침)

### 2. 클래스의 내부 동작 과정 중간에 끼얼들 수 있는 훅(hook)을 잘 선별하여 protected 메서드 형태로 공개해야 할 수도 있다.


예시

`java.util.AbstractList` removeRange
```Java

protected void removeRange(int fromIndex, int toIndex)

fromIndex(포함)부터 toIndex(미포함)까지의 모든 원소를 이 리스트에서 제거한다.

toIndex 이후의 원소들은 앞으로 (index만큼씩) 당겨진다. 이 호출로 리스트는 ‘toIndex

- fromIndex 만큼 짧아진다. (toIndex == fromindex라면 아무런 효과가 없다.) 이 리스트 혹은 이 리스트의 부분리스트에 정의된 cLear 연산이 이 메서드를 호출한다.

리스트 구현의 내부 구조를 활용하도록 이 메서드를 재정의하면 이 리스트와 부분리스트의 clear 연산 성능을 크게 개선할 수 있다.

Implementation Requirements

자를 얻어 모든 원소를 제거할 때까지 ListIterator.next와 ListIterator.remove를 반 복 호출하도록 구현되었다. 주의: ListIterator.remove가 선형 시간이 걸리면 이 구현의 성능은 제곱에 비례한다.

Parameters:

fromIndex 제거할 첫 원소의 인덱스

toIndex 제거할 마지막 원소의 다음 인덱스

```

상속용 클래스 설계시에 protected로 노출할 메소드 선정 방법 ? -> 정답 없음.

시험 방법 : 직접 만들어보기. -> 배포전에 검증 해보는게 좋음.

### 3. 상속용 클래스의 생성자는 직접적, 간접적으로든 재정의 가능 메서드를 호출하면 안됨.

```Java
public class Super {
	// 잘못된 예 - 생성자가 재정의 가능 메서드를 호출한다.
	public Super() {
		overrideMe();
	}
	
	public void overrideMe() {
	
	}
}
```

```Java
public final class Sub extends Super {
	// 초기화 되지 않은 final 필드. 생성자에서 초기화한다.
	private final Instant instant;

	Sub() {
		instant = Instant.now();
	}

	// 재정의 가능 메서드. 상위 클래스의 생성자가 호출한다.
	@Override public void overrideMe() {
		System.out.println(instant);
	}

	public static void main(String[] args) {
		Sub sub = new Sub();
		sub.overrideme();
	}
}
```

해당 프로그램 예상 동작 : instant 두 번 출력 -> But 첫번째는 null 출력
why? 상위 클래스의 생성자는 하위 클래스의 생성자가 인스턴스 필드를 초기화하기 전에 overrideMe를 호출.

final 필드의 상태가 위 프로그램에서는 두 가지임. (정상이라면 하나여야 함.)
overrideMe에서 Instant 객체 메소드를 호출하면, 상위 클래스의 생성자가 overrideMe를 호출할 때, NPE가 발생.

참고
| private final static method는 재정의가 불가능하니 생성자에서 안심하고 호출해도 된다.

Cloneable과 Serializable 인터페이스는 상속용 설계의 어려움을 한층 더해줌.
- clone, readObject는 생성자와 비슷한 효과를 낸다. -> 모두 직접적으로 간접적으로 재정의 가능 메소드를 호출해서는 안된다.

Serializable을 구현한 상속용 클래스가 readResolve() , write() 를 가지면 private이 아닌 protected로 선언해야함.

### 상속용으로 설계하지 않은 클래스는 상속하지 말자.
1. 둘 중 더 쉬운 쪽을 final로 선언
2. 모든 생성자를 private이나 package-private으로 선언하고, 정적 팩토리를 만들자.

구체 클래스가 표준 인터페이스를 구현하지 않았는데, 상속을 금지하면 사용하기 불편. -> 상속하게 하려면 클래스 내부에서는 재정의 가능 메서드를 사용하지 않게 만들고, 이 사실을 문서로 남김.

## 핵심정리
- 상속용 클래스 설계는 어려움. -> 자기 사용 패턴에 대한 문서를 남기고, 지키자.
- 효율적인 하위클래스를 위해 protected를 사용할 수도 있다.
- 클래스를 확장해야할 명확한 이유가 없으면 상속을 금지하자.
	- final로 선언
	- 생성자 모두를 외부에서 접근 불가능하게 만들자.
