# 생성자란?

- 인스턴스가 생성될  때, 호출되는 인스턴스 초기화 메서드이다.
- python의 `__init__(self)`

## 기능

1. 인스턴스 초기화(인스턴스 변수들을 초기화)
2. 인스턴스 생성 시에 실행되어야 할 작업을 위해 사용.

## 특징

1. Return 값이 없다. ⇒ method 이지만, 항상 return 값이 없기 때문에, void를 생략할 수 있다.
2. 생성자의 이름은 class의 이름과 같다.
3. (*) 연산자 new가 인스턴스를 생성하는 것. 생성자는 인스턴스를 생성하는 것이 아니다.

```java
public class Book {

	private String writer;
	private String content;
	private int page;

// 매개변수가 있는 생성자
public Book(String writer, String content, int page) {
	this.writer = writer;
	this.content = content;
	this.page = page;
	
	}

// 매개 변수가 없는 생성자
public Book() {
	
}

}
```

`Book peterRabbit = new Book();` 

- 위 코드의 new로 인해, 메모리(heap)에 Book 인스턴스가 생성된다.
- 생성자 Book()이 호출되어 수행된다.
- 연산자 new의 결과로, 생성된 Book instance 주소가 반환되어 `peterRabbit` 에 저장된다.
- 만약, class의 생성자를 정의하지 않으면 Compiler는 `기본 생성자` 를 추가하여 compile 한다.

## 매개변수가 있는 생성자

```java
class Post {
	String writer;
	String content;

  Post() {
		
	}

	Post(String w, String c) {
		writer = w;
		content = c;
	}
}
```

### 생성자에서 다른 생성자 호출하기

- 생성자의 이름으로 클래스이름 대신 this를 사용한다.
- 한 생성자에서 다른 생성자를 호출할 때는 반드시 첫 줄에서만 호출이 가능하다

- this : 인스턴스 자기 자신을 가리키는 참조변수. 인스턴스의 주소가 저장되어 있다.

→ 모든 인스턴스  메서드에 지역변수로 숨겨진 채로 존재한다.

- this(), this(매개변수) : 생성자. 같은 클래스의 다른 생성자를 호출 할 때 사용한다.

```java
public class Post {
    protected String writer;
    protected String title;
    protected String content;

    Post() {
        this("unan", "test", "test post 입니다.");
    }

    public Post(String writer, String title, String content) {
        this.writer = writer;
        this.title = title;
        this.content = content;
    }

}

class PostTest {
    public static void main(String[] args) {
        Post post1 = new Post();
        System.out.println("post1 정보" + post1.title + post1.content + post1.writer);

        Post post2 = new Post("unan2", "test2", "test post2");
        System.out.println("post2 정보" + post2.title + post2.content + post2.writer);
    }
}
```

- 실행결과
    - unan test post test
    - unan2 test post2 test2
    
- ‘this’는 참조 변수로 인스턴스 자신을 가리킨다. 참조변수를 통해 인스턴스의 멤버에 접근할 수 있는 것처럼 ‘this’로 인스턴스 변수에 접근할 수 있다.
- static method(class method)에서는 this를 사용할 수 없다. static method는 인스턴스의 생성 없이, 호출될 수 있기 때문이다.

# Reference

- JAVA의 정석
