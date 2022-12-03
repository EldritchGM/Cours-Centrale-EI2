/**
 * Classe representant un cercle
 * @author Jean-Marie Normand
 */

import java.util.*;

public class Cercle extends Forme {
   
   /// rayon du cercle
   protected double r;
   
   /**
    * Constructeur avec parametres
    * @param x : coordoonee "x" du centre du cercle
    * @param y : coordoonee "y" du centre du cercle
    * @param r : rayon du cercle
    */
   public Cercle(double x, double y, double r) {
      super(x,y);
      this.r = r;
   }
   
   /**
    * Constructeur sans parametre
    */
   public Cercle() {
      this(0,0,0);
   }
   
   /**
    * surface du cercle
    * @return la surface du cercle (dans la meme unite que le rayon)
    */
   public double surface() {
      return Math.PI * r * r;
   }
   /**
    * perimetre du cercle
    * @return le perimetre du cercle (dans la meme unite que le rayon)
    */
   public double perimetre() {
      return 2.0 * Math.PI * r;
   }
}