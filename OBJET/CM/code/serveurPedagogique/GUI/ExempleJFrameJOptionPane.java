/**
 * Classe présentant un exemple minimum de GUI
 * en créant une fenetre JFrame vide
 * @author jmnormand
 * @version 1.0
 */

import javax.swing.*;

public class ExempleJFrameJOptionPane {
   public static void main(String[] args) {
      JFrame maFrame = new JFrame();
      maFrame.setTitle("Exemple de JFrame");
      maFrame.setSize(500,500);
      maFrame.setVisible(true);
      maFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      
      JOptionPane.showMessageDialog(maFrame, "Je suis une boite de dialogue !");
      JOptionPane.showMessageDialog(maFrame, "Un message d'avertissement", "Avertissement !", JOptionPane.WARNING_MESSAGE);
      JOptionPane.showMessageDialog(maFrame, "Un message d'erreur", "Erreur !", JOptionPane.ERROR_MESSAGE);
      
      int confirm = JOptionPane.showConfirmDialog(maFrame, "Vous êtes surs ?");
      
      if(confirm == JOptionPane.YES_OPTION) {
         // on a dit oui
      }
      else if(confirm == JOptionPane.NO_OPTION) {
         // on a dit non
      }
      else if(confirm == JOptionPane.CANCEL_OPTION){
         // on a annule
      }
      
      String str = JOptionPane.showInputDialog(maFrame,"Entrez votre nom svp");
      // traitement de str
   }
}