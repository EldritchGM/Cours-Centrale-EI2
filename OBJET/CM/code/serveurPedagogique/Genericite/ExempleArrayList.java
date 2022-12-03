// Exemple d'utilisation de ArrayList

import java.util.ArrayList;

public class ExempleArrayList {

   public static void main(String[] args) {
      ArrayList<Personnage> persoL = new ArrayList<>();
      
      Magicien m = new Magicien("Gandalf", 100, 200, 500);
      Personnage p = new Personnage("Bill", 50, 50);
      
      persoL.add(p);
      persoL.add(m);
      
      for(int i=0;i<persoL.size();i++) {
         System.out.println(persoL.get(i));
      }
   }

}