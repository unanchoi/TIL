package item3;

public class Main {
    public static void main(String[] args) {
        Singleton1 singleton1 = Singleton1.getInstance();
        Singleton1 singleton2 = Singleton1.getInstance();

        System.out.println("singleton1 : " + singleton1);
        System.out.println("singleton2 : " + singleton2);

        String singleton3 = Singleton3.INSTANCE.getName();
        System.out.println("singleton3 : " + singleton3);

    }
}
