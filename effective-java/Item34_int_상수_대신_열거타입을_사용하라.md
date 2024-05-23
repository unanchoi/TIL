# 아이템 34. int  상수 대신 열거 타입을 사용하라

열거 타입은 일정 개수의 상수 값을 정의한 다음, 그 외의 값은 허용하지 않는 타입

```Java
public static final int APPLE_FUJI = 0

public static final int APPLE_PIPPIN = 1

public static final int APPLE_GRAhMY_SMITH = 2

public static final int 0RANGE_NAVEL = 0;

public static final int 0RANGE_TEMPLE = 1;

public static final int 0RANGE_BL00D = 2;
```

정수 열거 패턴의 단점
1. 타입 안전을 보장할 방법이 없고, 표현력도 좋지않다.


단순한 열거 타입
```Java
public enum Apple { FUJI, PIPPIN, GRANNY_SMITH }
```


데이터와 메서드를 갖는 열거 타입
```Java
public enum Planet {
    MERCURY(3.302e+23, 2.439e6),
    VENUS(4.869e+24, 6.052e6),
    EARTH(5.975e+24, 6.378e6),
    MARS(6.419e+23, 3.393e6),
    JUPITER(1.899e+27, 7.149e7),
    SATURN(5.685e+26, 6.027e7),
    URANUS(8.683e+25, 2.556e7),
    NEPTUNE(1.024e+26, 2.477e7);

    private final double mass; // 질량 (단위: 킬로그램)
    private final double radius; // 반지름 (단위: 미터)
    private final double surfaceGravity; // 표면중력 (단위: m / s^2)

    // 중력상수 (단위: m^3 / kg s^2)
    private static final double G = 6.67300E-11;

    // 생성자
    Planet(double mass, double radius) {
        this.mass = mass;
        this.radius = radius;
        surfaceGravity = G * mass / (radius * radius);
    }

    public double mass() { return mass; }
    public double radius() { return radius; }
    public double surfaceGravity() { return surfaceGravity; }

    public double surfaceWeight(double mass) {
        return mass * surfaceGravity; // F = ma
    }
}
```

보다시피 거대한 열거 타입을 만드는 일도 그리 어렵지 않다. 
`열거 타입 상수 각각을 특정 데이터와 연결지으려면 생성자에서 데이터를 받아 인스턴스 필드에 저장하면 된다.`

```Java
public class WeightTable {
    public static void main(String[] args) {
        double earthWeight = Double.parseDouble(args[0]);
        double mass = earthWeight / Planet.EARTH.surfaceGravity();
        for (Planet p : Planet.values())
            System.out.printf("%s에서의 무게는 %f이다.%n", p, p.surfaceWeight(mass));
    }
}
```

값이 사라지는 경우, 해당 값만 삭제해주면 된다. -> 클라이언트에서도 컴파일 오류가 발생하므로 쉽게 대응할 수 있다.

```Java

public enum Operation {
  PLUS, MINUS, TIMES, DIVIDE;

  // 상수가 뜻하는 연산을 수행한다.
  public double apply(double x, double y) {
    switch(this) {
      case PLUS: return x+y;
      case MINUS: return x-y;
      case TIMES: return x*y;
      case DIVIDE: return x/y;
    }
    throw new AssertionError("알수 없는 연산:" + this);
  }
}
```

enum은 상수별로 다르게 동작하는 코드를 구현할 수 있다.

```Java
public enum Operation {
  PLUS {public double apply(double x, double y){return x + y;}},

MINUS {public double apply(double x, double y){return x - y;}},

TIMES {public double apply(double x, double y){return x * y;}},

DIVIDE{public double apply(double x； double y){return x / y;}};

public abstract double apply(double x, double y);
}
```

열거 타입에는 상수 이름을 입력받아 그 이름에 해당하는 상수를 반환해주는 valueOf(String) 메소드가 자동 생성된다.
한편 enum의 toString 메서드를 재정의하려거든, toString이 반환하는 문자열을 해당 열거 타입 상수로 변환해주는 fromString 메서드도 함께 제공하는 걸 고려해보자.

fromString 예시
```Java
private static final Map<String, Operation> stringToEnum = Stream.of(values()).collect(

toMap(Object::toString, e -> e));

// 지정한 문자열에 해당하는 Operation을

(존재한다면) 반환한다.

public static Optional<Operation> fromString(String symbol) {

return Optional.ofNullable(stringToEnum.get(symbol));

}
```

fromString이 `Optional<Operation>`을 반환하는 점도 주의하자.



전략 열거 타입 패턴 예시
```Java
enum PayrollDay {

MONDAY(WEEKDAY), TUESDAY(WEEKDAY), WEDNESDAY(WEEKDAY),

THURSDAY(WEEKDAY), FRIDAY(WEEKDAY),

SATURDAY (WEEKEND), SUNDAY (WEEKBID);

private final PayType payType;

PayrollDay(PayType payType) { this.payType = payType; }

int pay(int minutesWorked, int payRate) {

return payType.pay(minutesWorked, payRate);

}

// 전략 열거 타입

enum PayType {

WEEKDAY {

int overtimePay(int minsWorked, int payRate) {

return minsWorked <= MINS_PER_SHIFT ? 0 :

(minsWorked - MINS_PER_SHIFT) * payRate / 2;

}

},

WEEKBJD {

int overtimePay(int minsWorked, int payRate) {

return minsWorked * payRate / 2;

}

}；

abstract int overtimePay(int mins, int payRate);

private static final int MINS_PER_SHIFT = 8 * 60;

int pay(int minsWorked, int payRate) {
	int basePay = minsWorked * payRate;
	return basePay + overtimePay(minsWorked, payRate);
	}
	}
}
```

switch 문은 열거 타입의 상수별 동작을 구현하는 데 적합하지 않다. 하지만 
`기존 열거 타입에 상수별 동작을 혼합해 넣을 떄는 switch 문이 좋은 선택이 될 수 있다.`

```Java
public static Operation inverse(Operation op) {
  switch (op) {
    case PLUS: return Operation.MINUS;
    case MINUS: return Opeation.PLUS;
    case TIMES: return Operation.DIVIDE;
    case DIVIDE: return Operation.TIMES;
    default: throw new AsserionError("알수 없는 연산 : " + op);
  }
}
```

### 핵심정리
열거 타입은 확실히 정수 상수보다 뛰어나다. 더 읽기 쉽고 안전하고, 강력하다. 대다수 열거 타입이 명시적 생성자나 메서드 없이 쓰이지만, 각 상수를 특정 데이터와 연결짓거나 상수마다 다르게 동작하게 할 때는 필요하다.
드물게는 하나의 메서드가 상수별로 다르게 동작해야할 때도 있다.
이런 열거 타입에서는 switch 문 대신 상수별 메서드 구현을 사용하자.
열거 타입 상수 일부가 같은 동작을 공유한다면 전략 열거 타입 패턴을 사용하자.
