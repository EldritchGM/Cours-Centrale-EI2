/**
 * Classe présentant un exemple minimum de GUI
 * pour illustrer l'utilisation d'un "GridBagLayout"
 * voir http://docs.oracle.com/javase/tutorial/uiswing/examples/layout/GridBagLayoutDemoProject/src/layout/GridBagLayoutDemo.java
 * @author jmnormand
 * @version 1.0
 */

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class ExempleGridBagLayout {
   
   public static void main(String[] args) {
      JFrame maFrame = new JFrame("GridBagLayout!");
      
      JPanel panneau = new JPanel();
      // 3 colonnes et 2 lignes
      GridBagLayout gestionnaire = new GridBagLayout();
      // applique le gestionnaire de placement au panneau
      panneau.setLayout(gestionnaire);
      
      JButton button;
      GridBagConstraints c = new GridBagConstraints();
      //natural height, maximum width
      c.fill = GridBagConstraints.HORIZONTAL;
      
      button = new JButton("Button 1");
      c.weightx = 0.5;
      
      c.fill = GridBagConstraints.HORIZONTAL;
      c.gridx = 0;
      c.gridy = 0;
      panneau.add(button, c);
      
      button = new JButton("Button 2");
      c.fill = GridBagConstraints.HORIZONTAL;
      c.weightx = 0.5;
      c.gridx = 1;
      c.gridy = 0;
      panneau.add(button, c);
      
      button = new JButton("Button 3");
      c.fill = GridBagConstraints.HORIZONTAL;
      c.weightx = 0.5;
      c.gridx = 2;
      c.gridy = 0;
      panneau.add(button, c);
      
      button = new JButton("Long-Named Button 4");
      c.fill = GridBagConstraints.HORIZONTAL;
      c.ipady = 40;      //make this component tall
      c.weightx = 0.0;
      c.gridwidth = 3;
      c.gridx = 0;
      c.gridy = 1;
      panneau.add(button, c);
      
      button = new JButton("5");
      c.fill = GridBagConstraints.HORIZONTAL;
      c.ipady = 0;       //reset to default
      c.weighty = 1.0;   //request any extra vertical space
      c.anchor = GridBagConstraints.PAGE_END; //bottom of space
      c.insets = new Insets(10,0,0,0);  //top padding
      c.gridx = 1;       //aligned with button 2
      c.gridwidth = 2;   //2 columns wide
      c.gridy = 2;       //third row
      panneau.add(button, c);
      
      // affecte le panneau a la fenetre
      maFrame.setContentPane(panneau);
      maFrame.pack();
      
      // rend la fenetre visible
      maFrame.setVisible(true);
      maFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
   
}