//: Evenement.java
// Classe simulant la notion d'événement
//	S. Szulman 1998
public class ExempleEvenement
{
	private Boolean Etat; // etat de l'evenement 
	public ExempleEvenement() {
		Etat = Boolean.FALSE;
	}
	public synchronized void set() {
		Etat = Boolean.TRUE;
        // debloque les threads qui attendent cet evenement:
		notifyAll(); 
	}
	public synchronized void reset() {
		Etat = Boolean.FALSE;
	}
	public synchronized void attente() {
		if(Etat==Boolean.FALSE) {
			try {
				wait(); // bloque jusqu'a un notify()
			}
			catch(InterruptedException e) {};
		}
	}// fin attente
}// fin classe
