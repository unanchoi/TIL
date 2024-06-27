# 아이템 39. 명명 패턴보다 Annotation을 사용해라.

### 명명패턴의 단점
1. 오타가 나면 안 된다.
2. 올바른 프로그램 요소에서만 사용될거라고 보증할 방법이 없다.
3. 프로그램 요소를 매개변수로 전달할 마땅한 방법이 없다.

메타 어노테이션 : 어노테이션에 선언하는 어노테이션. 
@Retention, @Target

애노테이션을 직접 정의할 수 있다.

```Java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface ExceptionTest {
    Class<? extends Throwable>[] value();
}

```

여러개의 값을 받는 경우 @Repeatable 메타애너테이션을 사용할 . 수있다.
```Java
@Retention(RetentionPolicy.RUNTIME)

@Target(ElementType.METHOD)

@Repeatable(ExceptionTestContainer.class)

public @interface ExceptionTest {

    Class<? extends Throwable> value();

}
```


### 핵심 정리
Annotation으로 할 수 있는 일을 명명패턴으로 처리할 이유는 없다.
