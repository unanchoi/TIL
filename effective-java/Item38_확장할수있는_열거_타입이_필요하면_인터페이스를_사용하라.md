열거 타입의 단점 : 확장할 수 없다.

열거 타입이 임의의 인터페이스를 구현할 수 있기 때문에, 인터페이스를 정의하고 열거 타입이 이 인터페이스를 구현하게하자.

```Java
public interface Operation {
    double apply(double x, double y);
}

public enum BasicOperation implements Operation {
    PLUS("+") {
        public double apply(double x, double y) { return x + y; }
    },
    MINUS("-") {
        public double apply(double x, double y) { return x - y; }
    },
    TIMES("*") {
        public double apply(double x, double y) { return x * y; }
    },
    DIVIDE("/") {
        public double apply(double x, double y) { return x / y; }
    };

    private final String symbol;

    BasicOperation(String symbol) {
        this.symbol = symbol;
    }

    @Override public String toString() {
        return symbol;
    }
}
```
열거 타입인 BasicOperation은 확장할 수 없지만 인터페이스인 Operation은 확장할 수 있다. 이 인터페이스를 연산의 타입으로 사용하면 된다.

```Java
public enum ExtendedOperation implements Operation {

    EXP("^") {

        public double apply(double x, double y) {
            return Math.pow(x, y);
        }

    },

    REMAINDER("%") {
        public double apply(double x, double y) {
            return x % y;
        }
    };
    
    private final String symbol;

    ExtendedOperation(String symbol) {
        this.symbol = symbol;
    }

  

    @Override public String toString() {
        return symbol;
    }

}
```

새롭게 작성한 연산은 기존 연산을 쓰던 곳이면 모두 사용 가능하다.'

#### 단점
열거 타입끼리 구현을 상속할 수 없다.
아무 상태에도 의존하지 않으면 -> default method 구현
Operation 에는 연산 기호를 저장하고 찾는 로직이 BasicOperation, ExtendedOperation에 모두 들어가야함. 공유하기는 기능이 많은 경우, 도우미 클래스나 정적 도우미 메서드로 분리하여 코드 중복을 줄일 수 있다.

---

자바 라이브러리도 이번 아이템에서 소개한 패턴을 사용한다.

그 예로 java,nio.file.LinkOption 열거 타입은 CopyOption과 OpenOption 인터페이스를 구현했다.

### 핵심정리

열거 타입 자체는 확장할 수 없지만, 인터페이스와 그 인터페이스를 구현하는 기본 열거타입을 함께 사용해 같은 효과를 낼 수 있다.

이렇게 하면 클라이언트는 이 인터페이스를 구현해 자신만의 열거 타입（혹은 다른 타입）을 만들 수 있다.

그리고 API가 （기본 열거타입을 직접 명시하지 않고） 인터페이스 기반으로 작성되었다면 기본 열거 타입의 인스턴스가 쓰이는 모든 곳을 새로 확장한 열거 타입의 인스턴스로 대체해 사용할 수 있다.

