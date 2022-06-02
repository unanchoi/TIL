package item4;


public abstract class UtilClass{
    // static을 참조하므로 앞에 static을 붙여야한다.
    static class AnotherClass extends UtilClass {

    }

    public static String getHello() {
        return "Hello";
    }

    public static void main(String[] args) {
        AnotherClass anotherClass = new AnotherClass();

        anotherClass.getHello();
        System.out.println(anotherClass.getHello());
        System.out.println(UtilClass.getHello());
    }
}
