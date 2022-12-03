/**
 * Classe representant une forme simple
 * possedant uniquement des corrdonnes de son "centre"
 * @author Jean-Marie Normand
 */

public class TestListeFormes {
   
   /**
    * un petit main de test qui se contente de creer 3 formes
    * de les ajouter dans une liste et de calculer la surface
    * totale de ces trois formes
    * @param args
    */
   public static void main(String[] args) {
      ListeFormes lf = new ListeFormes();
      Cercle c1 = new Cercle(1,2,4);
      Rectangle r1,r2;
      r1 = new Rectangle(2,5,2,3);
      r2 = new Rectangle(3,4,4,4);
      lf.ajouter(r1);
      lf.ajouter(r2);
      lf.ajouter(c1);
      
      System.out.println("surface totale : "+lf.surfaceTotale());
   }
}
