/**
 * Classe présentant un exemple minimum de GUI
 * pour illustrer l'utilisation d'un "FlowLayout"
 * @author jmnormand
 * @version 1.0
 */

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class ExempleFlowLayout {
   
   public static void main(String[] args) {
      JFrame maFrame = new JFrame("FlowLayout!");
      
      JPanel panneau = new JPanel();
      FlowLayout gestionnaire = new FlowLayout();
      // applique le gestionnaire de placement au panneau
      panneau.setLayout(gestionnaire);
      
      // Ajout d'elements au panneau
      panneau.add(new JButton("Button 1"));
      panneau.add(new JButton("Button 2"));
      panneau.add(new JButton("Button 3"));
      panneau.add(new JButton("Long-Named Button 4"));
      panneau.add(new JButton("5"));
      
      // affecte le panneau a la fenetre
      maFrame.setContentPane(panneau);
      maFrame.pack();
      // rend la fenetre visible
      maFrame.setVisible(true);
      maFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
   
}