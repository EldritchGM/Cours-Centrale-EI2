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
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

/**
 *
 * @author Jean-Marie Normand <jean-marie.normand@ec-nantes.fr>
 */
public class ConvertisseurTempStat {
   
   // Attributs
   public static JFrame maFenetre;
   public static JPanel monPanneau;
   public static GridLayout layout;
   public static NumberFormat celsiusFormat;
   public static JFormattedTextField celsius;
   public static JLabel labelCelsius;
   public static JLabel labelFahr;
   
   
   public static void main(String[] args) {
      // Declaration d'une JFrame
      maFenetre = new JFrame("Convertisseur C° vers F°");
      
      // Creation d'un panneau
      monPanneau = new JPanel();
      
      // Création d'un grid layout de 2x2
      layout = new GridLayout(2,2);
      // on applique le layout au panneau
      monPanneau.setLayout(layout);
      
      // Classe necessaire pour formatter notre champ de texte
      celsiusFormat = NumberFormat.getNumberInstance();
      celsiusFormat.setMaximumFractionDigits(8);
      
      // Creation d'un champ de texte formaté !
      celsius = new JFormattedTextField(celsiusFormat);
      celsius.setSize(100,20);
      celsius.setMinimumSize(new Dimension(100,20));
      celsius.setPreferredSize(new Dimension(100,20));
      celsius.setValue(new Double(0.0));
      
      // Création d'un label
      labelCelsius = new JLabel("Celsius");
      
      // Création d'un deuxième label
      labelFahr = new JLabel("Fahrenheit");
      
      // Création d'un bouton
      JButton convert = new JButton("Conversion");
      convert.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            Number valeurFormattedText = (Number)celsius.getValue();
            double tempFahr = (valeurFormattedText.doubleValue() * 1.8 + 32);
            // on arrondit le résultat à deux chiffres apres la virgule
            tempFahr = (double)Math.round(tempFahr * 100) / 100;
            labelFahr.setText(tempFahr + " Fahrenheit");
         }
      });
      
      
      // On ajoute les composants au panneau
      monPanneau.add(celsius);
      monPanneau.add(labelCelsius);
      monPanneau.add(convert);
      monPanneau.add(labelFahr);
      
      // On finalise la fenetre
      maFenetre.setContentPane(monPanneau);
      maFenetre.pack();
      maFenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      maFenetre.setVisible(true);
   }
   
}
