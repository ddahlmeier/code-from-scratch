/**
 * Reference examples in java
**/

class A {
    int value;
}


class B {

    public void testFinalReferences() {
	// final references are do not prevent refererenced object from being altered
	final A a = new A();
	a. value= 1;
	System.out.println("A.value = " + a.value);
	// alter referenced object, this actually works
	a.value = 2;
	System.out.println("A.value = " + a.value);
	// try to modify the references, this fails with a compiler error
	// a = new A();
    }
}

public class Scratch {

    public static void main (String args[]) {
	B b = new B();
	b.testFinalReferences();
    }
}