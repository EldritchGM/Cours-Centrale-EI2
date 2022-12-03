/*
 * Classe permettant d'intercepter et de gerer la reaction
 * a l'interaction de l'utilisateur sur le bouton de conversion
 * i.e. quand l'utilsateur clique sur le bouton de conversion
 * on doit calculer le resultat de la conversion et afficher
 * le resultat dans le JLabel cree a cet effet.
 */

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFormattedTextField;
import javax.swing.JLabel;


/**
 *
 * @author Jean-Marie Normand <jean-marie.normand@ec-nantes.fr>
 */
public class ReactionBoutonConversion implements ActionListener {
    // Attributs
    
    // Le champ de texte contenant la valeur de la température
    private JFormattedTextField celsiusValue;
        
    // La reference vers le Label dont on veut modifier le nom
    private JLabel affichageFahr;
    
    // Constructeur
    public ReactionBoutonConversion(JFormattedTextField celsiusText, JLabel lab) {
        this.celsiusValue = celsiusText;
        this.affichageFahr = lab;
    }
    
    // On implemente ActionListener --> on doit redéfinir actionPerformed !
    @Override
    public void actionPerformed(ActionEvent e) {
        Number valeurFormattedText = (Number)this.celsiusValue.getValue();
        double tempFahr = (valeurFormattedText.doubleValue() * 1.8 + 32);
        // on arrondit le résultat à deux chiffres apres la virgule
        tempFahr = (double)Math.round(tempFahr * 100) / 100;
        affichageFahr.setText(tempFahr + " Fahrenheit");
    }
    
}
