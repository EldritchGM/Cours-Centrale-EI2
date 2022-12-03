// Exemple d'utilisation de LinkedList

import java.util.LinkedList;

public class ExempleLinkedList {
   
   public static void main(String[] args) {
      LinkedList<Personnage> persoL = new LinkedList<>();
      
      Magicien m = new Magicien("Gandalf", 100, 200, 500);
      Personnage p = new Personnage("Bill", 50, 50);
      
      persoL.add(p);
      persoL.add(m);
      
      for(int i=0;i<persoL.size();i++) {
         System.out.println(persoL.get(i));
      }
   }
   
}