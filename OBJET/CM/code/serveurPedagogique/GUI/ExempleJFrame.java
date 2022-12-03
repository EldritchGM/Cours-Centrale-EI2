/**
 * Classe présentant un exemple minimum de GUI
 * en créant une fenetre JFrame vide
 * @author jmnormand
 * @version 1.0
 */

import javax.swing.*;

public class ExempleJFrame {
   public static void main(String[] args) {
      JFrame maFrame = new JFrame();
      maFrame.setTitle("Exemple de JFrame");
      maFrame.setSize(500,500);
      maFrame.setVisible(true);
      maFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
}