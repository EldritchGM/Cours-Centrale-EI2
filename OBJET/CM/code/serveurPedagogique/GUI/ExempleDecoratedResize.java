/**
 * Classe présentant un exemple minimum de GUI
 * pour illustrer la décoration et redimensionnement
 * @author jmnormand
 * @version 1.0
 */

import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class ExempleDecoratedResize {
   
   public static void main(String[] args) {
      final JFrame f = new JFrame("Hello World!");
      JCheckBox b = new JCheckBox("Resizable", true);
      JCheckBox b2 = new JCheckBox("Decorated", true);
      f.getContentPane().add(b, BorderLayout.WEST);
      f.getContentPane().add(b2, BorderLayout.EAST);
      
      
      b2.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
            JCheckBox bo=(JCheckBox)e.getSource();
            f.dispose();
            f.setUndecorated(!bo.isSelected());
            System.out.println("Resizable ?"+f.isResizable());
            f.setVisible(true);
         }
      });
      
      b.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
            JCheckBox bo=(JCheckBox)e.getSource();
            f.dispose();
            f.setResizable(bo.isSelected());
            f.setVisible(true);
         }
      });
      
      f.setSize(320,240);
      f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      f.setVisible(true);
   }
   
}