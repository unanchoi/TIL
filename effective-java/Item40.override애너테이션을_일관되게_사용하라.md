# 아이템 40. @Override 애너테이션을 일관되게 사용하라.

@Override : 상위 타입의 메서드를 재정의했음을 뜻함.


```Java
import java.util.HashSet;

import java.util.Set;

  

public class Bigram {

    private final char first;

    private final char second;

  

    public Bigram(char first, char second) {

        this.first = first;

        this.second = second;

    }

  

    @Override

    public boolean equals(Object obj) {

        if (this == obj) {

            return true;

        }

        if (obj == null || getClass() != obj.getClass()) {

            return false;

        }

        Bigram bigram = (Bigram) obj;

        return first == bigram.first && second == bigram.second;

    }

  

    @Override

    public int hashCode() {

        return 31 * first + second;

    }

  

    public static void main(String[] args) {

        Set<Bigram> s = new HashSet<>();

        for (int i = 0; i < 10; i++) {

            for (char ch = 'a'; ch <= 'z'; ch++) {

                s.add(new Bigram(ch, ch));

            }

        }

        System.out.println(s.size());

    }

}
```

해당 코드는 equals를 재정의한 것이 아니라 다중정의 했다. -> 따라서 size가 다르게 동작한다.
Object의 equals를 재정의하려면 매개변수 타입을 Object로 해야 하는데, 그렇게 하지 않음.

@Override 애너테이션을 달고 다시 컴파일하면 컴파일 오류가 발생한다.

따라서 **상위 클래스의 메서드를 재정의하려는 모든 메서드에 @Override 애너테이션을 달자.

메서드를 재정의할 때는 굳이 @Override를 달지 않아도 된다. 구체 클래스인데 아직 구현하지 않은 추상 메서드가 남아 있다면 컴파일러가 그 사실을 바로 알려주기 때문.


Set 인터페이스는 Collection 인터페이스를 확장했지만 새로 추가한 메서드는 없다.

따라서 모든 메서드 선언에 @Override를 달아 실수로 추가한 메서드가 없음을 보장했다.

### 핵심 정리
재정의한 모든 메서드에 @Override 애너테이션을 의식적으로 달면 여러분이 실수했을때 컴파일러가 바로 알려준다.
예외 : 구체클래스에서 상위클래스의 추상 메서드를 재정의한 경우엔 이 애너테이션을 달지 않아도 된다.
