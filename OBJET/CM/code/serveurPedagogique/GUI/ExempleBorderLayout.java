/**
 * Classe présentant un exemple minimum de GUI
 * pour illustrer l'utilisation d'un "BorderLayout"
 * @author jmnormand
 * @version 1.0
 */

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class ExempleBorderLayout {
   
   public static void main(String[] args) {
      JFrame maFrame = new JFrame("BorderLayout!");
      maFrame.setSize(400,400);
      
      JPanel panneau = new JPanel();
      BorderLayout gestionnaire = new BorderLayout();
      // applique le gestionnaire de placement au panneau
      panneau.setLayout(gestionnaire);
      
      // Ajout d'elements au panneau
      panneau.add(new JButton("Centre"), BorderLayout.CENTER);
      panneau.add(new JButton("Nord"), BorderLayout.NORTH);
      panneau.add(new JButton("Sud"), BorderLayout.SOUTH);
      panneau.add(new JButton("Est"), BorderLayout.EAST);
      panneau.add(new JButton("Ouest"), BorderLayout.WEST);
      
      // affecte le panneau a la fenetre
      maFrame.setContentPane(panneau);
      // rend la fenetre visible
      maFrame.setVisible(true);
      maFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
   
}