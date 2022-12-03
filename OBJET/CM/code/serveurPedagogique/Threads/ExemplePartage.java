/**
	* \file exemplePartage.java
	* \version 1.0
	* petit exemple (incorrect) de partage de donnees entre
	* les threads. Le comportement al'execution est indefini
*/
public class ExemplePartage extends Thread {

  private static String chaineCommune = "";
  private String nom;

	/**
		* le constructeur se contente de recopier la reference de la chaine passee
		* en argument dans la variable nom
		*/
	public ExemplePartage ( String s ) {
		nom = s;
   }

	/**
		* a l'execution, le thread concatene son nom a la chaine commune
	*/
  public void run() {
  	chaineCommune = chaineCommune + nom;
  }

	/**
		* le main lance 2 threads qui partagent la meme variable qui est affectee
		* de la valeur T1 dans le premier, de la valeur T2 dans le second, puis
		* appelle start() et affiche le resultat
	*/
  public static void main(String args[]) {
  	Thread T1 = new ExemplePartage( "T1" );
  	Thread T2 = new ExemplePartage( "T2" );
  	T1.start();
  	T2.start();

	try {
	    // attendre la fin de T1 et T2
	    T2.join();
	    T1.join();
	}
	catch(InterruptedException e) {
	    System.out.println("interrompu");
	}

  	System.out.println( chaineCommune );
  }
}
