package item3;

public class Poketmon {

    private static final Poketmon pikachu = new Poketmon();

    private Poketmon() {

    }

    public static Poketmon getPikachu() {
        return pikachu;
    }

    public void lighteningVolt() {
        System.out.println("백만볼트!");
    }

    public static void main(String[] args) {
        Poketmon poketmon = new Poketmon();
        Poketmon poketmon1 = getPikachu();

        System.out.println(poketmon);
        System.out.println(poketmon1);
    }

}
