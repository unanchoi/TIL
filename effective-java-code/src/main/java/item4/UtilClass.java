package item4;


public abstract class UtilClass{
    public static String getName() {
        return "unan";
    }

    static class AnotherClass extends UtilClass {

    }

    public static void main(String[] args) {
        AnotherClass anotherClass = new AnotherClass();

        System.out.println(anotherClass.getName());
        System.out.println(UtilClass.getName());

    }
}
