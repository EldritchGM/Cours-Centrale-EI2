/**
 * Classe présentant un exemple minimum de GUI
 * en créant une fenetre JFrame vide
 * @author jmnormand
 * @version 1.0
 */

import javax.swing.*;

public class ExempleLabel {
   public static void main(String[] args) {
      JFrame maFrame = new JFrame();
      maFrame.setTitle("Exemple de JFrame");
      JPanel panneau = new JPanel();
      JLabel lab = new JLabel("Je suis une etiquette!");
      panneau.add(lab);
      maFrame.setContentPane(panneau);
      maFrame.setVisible(true);
      maFrame.pack();
      maFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
}