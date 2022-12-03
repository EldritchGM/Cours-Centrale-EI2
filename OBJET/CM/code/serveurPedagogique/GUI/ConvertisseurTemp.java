/*
 * Mini exemple de manipulation des widgets SWING et des listeners/events
 * Version issue d'un tutorial en ligne disponible sur le site de Java 
 * http://docs.oracle.com/javase/tutorial/uiswing/learn/index.html
 */


import java.awt.Dimension;
import java.awt.GridLayout;
import java.text.NumberFormat;
import javax.swing.JButton;
import javax.swing.JFormattedTextField;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 *
 * @author Jean-Marie Normand <jean-marie.normand@ec-nantes.fr>
 */
public class ConvertisseurTemp {
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Declaration d'une JFrame
        JFrame maFenetre = new JFrame("Convertisseur C° vers F°");

        // Creation d'un panneau
        JPanel monPanneau = new JPanel();
        
        // Création d'un grid layout de 2x2
        GridLayout layout = new GridLayout(2,2);
        // on applique le layout au panneau
        monPanneau.setLayout(layout);
        
        // Classe necessaire pour formatter notre champ de texte
        NumberFormat celsiusFormat = NumberFormat.getNumberInstance();
        celsiusFormat.setMaximumFractionDigits(8);
    
        // Creation d'un champ de texte formaté !
        JFormattedTextField celsius = new JFormattedTextField(celsiusFormat);
        celsius.setSize(100,20);
        celsius.setMinimumSize(new Dimension(100,20));
        celsius.setPreferredSize(new Dimension(100,20));
        celsius.setValue(new Double(0.0));
                
        // Création d'un label
        JLabel labelCelsius = new JLabel("Celsius");
        
        // Création d'un bouton
        JButton convert = new JButton("Conversion");
        
        // Création d'un deuxième label
        JLabel labelFahr = new JLabel("Fahrenheit");
        
        // On crée un objet spécial qui a pour but de gérer le clic
        // sur le bouton et de réaliser la conversion
        // en plus il devra modifier le texte du label Fahrenheit pour afficher
        // le résultat de la conversion
        ReactionBoutonConversion reacConv = new ReactionBoutonConversion(celsius,labelFahr);
        
        // On ajoute le listener au bouton !
        convert.addActionListener(reacConv);
        
        // On ajoute les composants au panneau
        monPanneau.add(celsius);
        monPanneau.add(labelCelsius);
        monPanneau.add(convert);
        monPanneau.add(labelFahr);
        
        // On finalise la fenetre
        maFenetre.setContentPane(monPanneau);
        maFenetre.pack();
        // on la rend visible
        maFenetre.setVisible(true);
        maFenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
