class MonException extends Exception {
}

public class TestException {
	public void method1() throws MonException {
		throw new MonException();
	}
	
	
	public void method2() {
		method1();
	}
	
	/*
    // Solution 1
	public void method2() throws MonException {
		method1();
	}
	*/
   /*
    // Solution 2
	public void method2() {
		try { 
			method1(); 
		}
		catch (MonException e) {
	 		// ...
		}
	}
    */
   
   public static void main(String[] args) {
      
   }
}

