#아이템 35. ordinal 메서드 대신 인스턴스 필드를 사용하라.

잘못된 예시
```Java
public enum Ensemble {
  SOLO, DUET, TRIO, QUARTET, QUINTET, SEXTET, SEPTET, OCTET, NONET, DECTET
}
```

상수 선언 순서를 바꾸면, numberOfMusicians가 오동작함.
이미 사용중인 정수와 값이 같은 상수는 추가할 방법이 없다.

=> `열거 타입 상수에 연결된 값은 ordinal 메서드로 얻지 말고, 인스턴스 필드에 저장하자.`

```Java
public enum Ensemble {
 SOLO(1), DUET(2), TRIO(3), QUARTET(4), QUINTET(5),
 SEXTET(6), SEPTET(7), OCTET(8), DOUBLE_QUARTET(8),
 NONET(9), DECTET(10), TRIPLE_QUARTET(12);


private final int numberOfMusicions;

Ensemble(int size) {
  this.numberOfMusicians = size;
}

public int numberOfMusicians() {
  return numberOfMusicians;
}

}
```

Enum API문서에 "대부분 프로그래머는 . 이 메서드를 쓸 일이 없다. 이 메서드는 EnumSet과 EnumMap 같이 열거 타입 기반의 범용 자료구조에 쓸 목적으로 설계되었다."



