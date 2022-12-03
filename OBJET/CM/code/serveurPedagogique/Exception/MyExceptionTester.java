class MyException1 extends Exception {
}

class MyException2 extends MyException1 {
}

class MyException3 extends MyException2 {
}

public class MyExceptionTester {

	public void doIt(String ex) {
		// le code qui va lever les exceptions
		try {
			if (ex.equals("Exception1")) {
				throw new MyException1();
			}
			if (ex.equals("Exception2")) {
				throw new MyException2();
			}
			if (ex.equals("Exception3")) {
				throw new MyException3();
			}
		}
		catch (MyException1 e) {
			System.out.println(e.getMessage());
			return;
		}
		catch (MyException2 e) {
			System.out.println(e.getMessage());
			return;
		}
		catch (MyException3 e) {
			System.out.println(e.getMessage());
			return;
		}
	}
	
	public static void main(String[] args) {
		new MyExceptionTester().doIt(args[0]);
	}
}
