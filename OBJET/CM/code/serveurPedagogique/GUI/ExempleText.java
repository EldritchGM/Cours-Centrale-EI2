/**
 * Classe présentant un exemple minimum de GUI
 * en créant une fenetre JFrame avec des zones de texte
 * @author jmnormand
 * @version 1.0
 */
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class ExempleText {
   public static void main(String[] args) {
      JFrame maFrame = new JFrame("Zones de texte");
      
      JPanel panneau = new JPanel();
      // 3 colonnes et 2 lignes
      GridLayout gestionnaire = new GridLayout(3,2);
      // applique le gestionnaire de placement au panneau
      panneau.setLayout(gestionnaire);
      
      // Labels
      JLabel labelTextF = new JLabel("TextField: ");
      JLabel labelPassF = new JLabel("PasswordField: ");
      JLabel labelTextA = new JLabel("TextArea: ");

      // Zones de texte
      JTextField textF = new JTextField();
      JPasswordField passF = new JPasswordField();
      JTextArea textA = new JTextArea(10,20);
      
      // Ajout d'elements au panneau
      panneau.add(labelTextF);
      panneau.add(textF);
      panneau.add(labelPassF);
      panneau.add(passF);
      panneau.add(labelTextA);
      panneau.add(textA);
      
      // affecte le panneau a la fenetre
      maFrame.setContentPane(panneau);
      maFrame.pack();
      // rend la fenetre visible
      maFrame.setVisible(true);
      maFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
}