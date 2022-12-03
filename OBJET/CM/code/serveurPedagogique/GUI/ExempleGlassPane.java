/**
 * Classe présentant un exemple minimum de GUI
 * pour utiliser le glassPane
 * @author jmnormand
 * @version 1.0
 */

import javax.swing.*;
import java.awt.BorderLayout;

public class ExempleGlassPane {

   public static void main(String[] args) {
      JFrame f = new JFrame("Hello World!");
      f.getContentPane().add(new JButton("Un bouton"),BorderLayout.WEST);
      f.getContentPane().add(new JButton("Autre bouton"),BorderLayout.SOUTH);
      String[] s = {"a","bb","ccc","dd","e","ff","ggg","hhh","i","jj"};
      f.getContentPane().add(new JScrollPane(new JList(s)));
      //f.setSize(320,240);
      f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      f.setVisible(true);
   }

}