# 할 수 있는한 모든 비검사 경고를 제거하라.

경고를 제거할 수 없지만 타입이 안전하다고 확신할 수 있다면 `@SuppressWarnings("unchecked" )` 애너테이션을 달아 경고를 숨기자.

`@SuppressWarnings("unchecked" )`애너테이션은 항상 가능한 한 좁은 범위에 적용하자.

```Java
public <T> T[] toArray(T[] a) {
	if (a.length < size {
		return (T[] Arrays.copyOf(elements, size, a.getClass()));
		System.arraycopy(elements, 0, a, 0, size);
	}

	if (a.length > size) {
		a[size] = null;
	}
	return a;
}
```

ArrayList를 컴파일하면 이 메서드에서 다음 경고가 발생한다.
```
ArrayList.java:305: warning: [unchecked] unchecked cast
return (T[]) Arrays.copyOf (elements, size, a.getClass());

required: T[]

found: Object []
```

애너테이션은 선언에만 달 수 있기 때문에 return 문에는 @SuprressWarning을 다는 것이 불가능하다.


지역변수를 선언해 SuprressWarnings의 범위를 좁힌다.
```Java
public <T> T[] toArray(T[] a) {
	if (a.length < size) {
	// 생성한 배열과 매개변수로 받은 배열의 타입이 모두 T로 같으므로 올바른 형변환이다
	@SuprressWarnings("unchecked") T[] result = (T[])  Arrays.copyOf (elements, size, a.getClass());
	return result;
	}
	System.arraycopy(elements, 0, a, 0, size);
		
	if (a.length > size) {
		a[size] = null;
	}
	return a;
}

```

### 핵심정리

비검사 경고는 중요하니 무시하지 말자. ClassCastException 예외를 발생시킬 수 있다.
경고를 없앨 방법이 없으면 최대한 범위를 좁히고 @SuprressWarning 사용하여 경고를 제거하고, 그 근거를 주석으로 남기자.
