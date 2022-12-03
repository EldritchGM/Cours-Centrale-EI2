/**
 * Classe representant une arme tres basique
 * @author jmnormand
 * @version 1.0
 */
public class Arme {
   // Attributs de la classe
   /**
    * Puissance de l'arme (prive)
    */
   private int puissance;
   
   public Arme(int p) {
      this.puissance = p;
   }
   
   public Arme(Arme a) {
      this.puissance = a.puissance;
   }
   
   public void setPuissance(int p) {
      this.puissance = p;
   }
   
   public int getPuissance() {
      return this.puissance;
   }
}