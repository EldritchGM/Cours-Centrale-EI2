/**
 * Classe présentant un exemple minimum de GUI
 * pour illustrer l'utilisation d'un "GridLayout"
 * @author jmnormand
 * @version 1.0
 */

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class ExempleGridLayout {
   
   public static void main(String[] args) {
      JFrame maFrame = new JFrame("GridLayout!");
      
      JPanel panneau = new JPanel();
      // 3 colonnes et 2 lignes
      GridLayout gestionnaire = new GridLayout(3,2);
      // applique le gestionnaire de placement au panneau
      panneau.setLayout(gestionnaire);
      
      // Ajout d'elements au panneau
      panneau.add(new JButton("Bouton 1"));
      panneau.add(new JButton("Bouton 2"));
      panneau.add(new JButton("Bouton 3"));
      panneau.add(new JButton("Bouton 4"));
      panneau.add(new JButton("Bouton 5"));
      panneau.add(new JButton("Bouton 6"));
      
      // affecte le panneau a la fenetre
      maFrame.setContentPane(panneau);
      maFrame.pack();
      // rend la fenetre visible
      maFrame.setVisible(true);
      maFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
   
}