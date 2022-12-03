/**
 * Classe représentant un Magicien basique
 * ayant seulement un nombre maximum de points de vie
 * et un nombre de points d'action (energie)
 * @author jmnormand
 * @version 1.0
 */
public class Magicien extends Personnage {
 
   /**
    * Quantite de magie du magicien
    */
   private int ptMagie;
   
   /**
    * Un constructeur
    */
   public Magicien(String n, int e, int pv, int pm) {
      super(n,e,pv);
      this.ptMagie = pm;
   }
   
   /**
    * Fonction d'affichage
    */
   public String toString() {
      String res;
      res = super.toString();
      res += ", "+ptMagie+" points de magie";
      return res;
   }
}