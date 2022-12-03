/**
 * Classe présentant un exemple minimum de GUI
 * pour illustrer l'utilisation d'un "GridLayout"
 * adapte de developpez.com :
 * http://java.developpez.com/faq/gui/?page=graphique_awt_swing_listeners#GRAPHIQUE_SWING_Listeners
 * @author jmnormand
 * @version 1.0
 */

import java.awt.event.ActionListener;

// Étape 1 : déclaration de la classe
public class ExempleActionListener1 implements ActionListener {
	// Étape 3 : Création de deux boutons
	JButton monBouton = new JButton("Mon Bouton");
	JButton monBouton2 = new JButton("Mon Bouton2");
   
   
	public MaClasse() {
		// Étape 4 : On ajoute « l'écouteur » sur le bouton « monBouton ».
		monBouton.addActionListener(this);
		// Puis sur monBouton2
		monBouton2.addActionListener(this);
	}
   
	/* Étape 2 :Cette méthode est déclarée dans l'interface ActionListener. Il nous faut l'implémenter. */
	public void actionPerformed(ActionEvent e) {
      // Étape 2bis
		if(e.getSource() == monBouton) {
			// Bouton 1 a été cliqué
		}else {
			// Bouton 2 a été cliqué
		}
	}
}