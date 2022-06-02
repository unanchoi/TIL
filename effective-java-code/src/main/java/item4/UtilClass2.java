package item4;

public class UtilClass2 {

    // 생성자가 존재하지만, 못쓰는 생성자이므로, Assertion Error 처리 => 주석으로 표현하자.
    private UtilClass2() {
        throw new AssertionError();
    }
}
