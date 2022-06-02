package item4;

public class UtilClass3 {

    private UtilClass3() {
        throw new  AssertionError();
    }

    public static String getName() {
        return "unan";
    }

    public static void main(String[] args) {
        UtilClass3 utilClass3 = new UtilClass3();
        System.out.println(utilClass3.getName());
    }
}
