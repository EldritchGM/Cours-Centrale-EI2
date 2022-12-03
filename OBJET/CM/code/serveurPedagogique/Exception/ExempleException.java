class MyEException1 extends Exception {
}

class MyEException2 extends Exception {
}


class ExempleException {
	public static void main(String[] args) throws MyEException2 {
		try {
			new ExempleException().doIt(args[0]);
		}
		catch (ArrayIndexOutOfBoundsException ex) {
			System.out.println("il fallait mettre un argument lors de l'appel");
		}
	}
	
	public void doIt(String e) throws MyEException2 {
		System.out.println("marqueur 1");
		try {
			if (e.equals("STOP")) {
				throw new MyEException1();
			}
			if (e.equals("2")) {
				throw new MyEException2();
			}
			
			System.out.println("marqueur 2");
			
			return; 
			
		} // fin du bloc try
		catch (MyEException1 ex) {
			System.out.println("marqueur 3");
			return;
		}
		finally {
			System.out.println("marqueur finally");
		}
	}

}
