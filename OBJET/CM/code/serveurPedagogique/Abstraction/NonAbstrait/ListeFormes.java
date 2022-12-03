/**
 * Classe representant une liste de formes
 * @author Jean-Marie Normand
 */

import java.util.LinkedList;

public class ListeFormes {
   /**
    * la liste (utilise LinkedList<E>)
    */
   protected LinkedList<Forme> listeFormes;
	
   /**
    * constructeur
    */
   public ListeFormes() {
      listeFormes = new LinkedList<Forme>();
   }

   /**
    * ajoute une forme a la liste de forme
    * @param f reference sur la forme a ajouter
    */
   public void ajouter(Forme f) {
      listeFormes.add(f);
   }
   
   /**
    * translater l'ensemble des formes de la liste
    * @param dx abscisse de la translation
    * @param dy ordonnee de la translation
    */
   public void toutDeplacer(double dx,double dy) {
      for (Forme f : listeFormes) {
         f.deplacer(dx,dy);
      }
   }
   
   /* calcul de la surface totale : iteration sur les surfaces
    * @return la surface totale
    */
   public double surfaceTotale() {
      double s=0d;
      for (Forme f : listeFormes) {
         s += f.surface();
      }
      return s;
   }
}