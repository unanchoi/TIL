package item1;

public class Foo {

    String firstName;
    String lastName;

    public Foo() {
    }

    public Foo(String firstName) {
        this.firstName = firstName;
    }

    public static Foo withFirstName(String firstName) {
        return new Foo(firstName);
    }

    public static Foo withLastName(String lastName) {
        return new Foo(lastName);
    }

    public static void main(String[] args) {
        Foo foo = new Foo("unan");
    }


}
