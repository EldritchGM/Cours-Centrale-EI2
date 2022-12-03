/**
 * Classe representant une forme simple
 * possedant uniquement des corrdonnes de son "centre"
 * @author Jean-Marie Normand
 */

public class Forme {
   
   /**
    * abscisse du "centre"
    */
   protected double x;
	
   /**
    * ordonnee du "centre"
    */
   protected double y;
   
   /**
    * Constructeur avec parametres
    * @param x : coordoonee "x" du centre
    * @param y : coordoonee "y" du centre
    */
   public Forme(double x, double y) {
      this.x = x;
      this.y = y;
   }
   
   /**
    * Constructeur sans parametre
    */
   public Forme() {
      this(0,0);
   }
   
   /**
    * Methode de deplacement de la forme
    */
   public void deplacer(double dx,double dy) {
      x += dx;
      y += dy;
   }
}