/**
 * Classe representant un cercle
 * @author Jean-Marie Normand
 */

public class Rectangle extends Forme {
   
   /// longueur du rectangle
   protected double longueur;

   /// largeur du rectangle
   protected double largeur;

   /**
    * Constructeur avec parametres
    * @param x : coordoonee "x" du centre du cercle
    * @param y : coordoonee "y" du centre du cercle
    * @param lo : longueur du rectangle
    * @param la : largeur du rectangle
    */
   public Rectangle(double x, double y, double lo, double la) {
      super(x,y);
      this.longueur = lo;
      this.largeur = la;
   }
   
   /**
    * Constructeur sans parametre
    */
   public Rectangle() {
      this(0,0,0,0);
   }
   
   /**
    * surface du rectangle
    * @return la surface du rectangle (dans la meme unite que longueur et largeur)
    */
   public double surface() {
      return longueur * largeur;
   }
   /**
    * perimetre du rectangle
    * @return le perimetre du rectangle (dans la meme unite que longueur et largeur)
    */
   public double perimetre() {
      return 2.0 * (longueur+largeur);
   }
}