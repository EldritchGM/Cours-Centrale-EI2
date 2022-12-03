/**
	* \file ExempleConcurrent.java
*/
public class ExempleConcurrent extends Thread {

	private static int compte = 0;

  public void run() {
		int tmp = compte;
		try {
			Thread.sleep(1); // ms
		} catch (InterruptedException e) {
			System.out.println("ouch!\n");
			return;
		}
		tmp = tmp + 1;
		compte = tmp;
	}

  public static void main(String args[]) throws InterruptedException {
		Thread T1 = new ExempleConcurrent();
		Thread T2 = new ExempleConcurrent();
		T1.start();
		T2.start();
		T1.join();
		T2.join();
    System.out.println( "compteur=" + compte );
  }
}
 
