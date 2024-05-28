#  아이템 36. 비트 필드 대신 EnumSet을 사용하라.

열거한 값들이 주로 집합으로 사용될 경우, 예전에는 . 각상수에 서로 다른 2의 거듭제곱 값을 할당한 정수 열거 패턴을 사용해 왔다.

비트 필드 열거 상수 - 구닥다리 기법
```Java
public class Text {
  public static final int STYLE_BOLD = 1 << 0;
  public static final int STYLE_ITALIC = 1 << 1;
  public static final int STYLE_UNDERLINE = 1 << 2;
  public static final int STYLE_STRAIKETHROUGH = 1 << 3;
}
```

비트 필드를 사용하면 비트별 연산을 사용해 합집합과 교집합같은 집합연산을 효율적으로 수행할 . 수있다.
하지만 정수 열거 상수 단점을 그대로 갖고 있다.

비트 피드 값이 그대로 출력되면 단순한 정수 열거 상수를 출력할 때보다 해석하기가 훨씬 어렵다. 비트 필드 하나에 녹아 있는 모든 원소를 순회하기도 까다롭다. 마지막으로 최대 몇 비트가 필요한지를 API 작성 시 미리 예측하여 적절한 타입을 선택해야 한다.
API를 수정하지 않고는 비트 수를 더 늘릴 수 없기 떄문이다.

비트 필드 대체 -> EnumSet

```Java

public class Text {
  public enum Style {
    BOLD, ITALIC, UNDERLINE, STRIKETHROUGH
  }
  // 어떤 Set을 넘겨도 되나, EnumSet이 가장 좋다.
  public void applyStyles(Set<Style> styles) {
    ...
  }
}
```

### 핵심정리
열거할 수 있는 타입을 한데 모아 집합 형태로 사용한다고 해도 비트 필드를 사용할 이유는 없다.
EnumSet의 유일한 단점 : 자바 9까지는 불변 EnumSet을 만들 수 없다.
