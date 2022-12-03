/**
 * Classe representant une baguette magique basique
 * @author jmnormand
 * @version 1.0
 */
public class Baguette {
   // Attribut de la classe
   /**
    * Puissance de la baguette (prive)
    */
   private int puissance;
   
   public Baguette(int p) {
      this.puissance = p;
   }
   
   public Baguette(Baguette a) {
      this.puissance = a.puissance;
   }
   
   public void setPuissance(int p) {
      this.puissance = p;
   }
   
   public int getPuissance() {
      return this.puissance;
   }
}