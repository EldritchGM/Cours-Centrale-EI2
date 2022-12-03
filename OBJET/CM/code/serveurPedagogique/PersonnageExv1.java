/**
 * Classe exemple d'un personnage basique
 * ayant seulement un nombre maximum de points de vie
 * et un nombre de points d'action (energie)
 * @author jmnormand
 * @version 1.0
 */
public class PersonnageEx {
   
   // Attributs de la classe
   /**
    * Quantite d'energie du personnage (prive)
    */
   private int energie;
   
   /**
    * Nombre maximum de points de vie du personnage (prive)
    */
   private int ptVie;
   
   // Constructeurs et methodes
   /**
    * Un constructeur avec deux entiers
    * en parametres.
    * @param e un entier representant l'energie du personnage
    * @param pv un entier representant les points de vie du personnage
    */
   public PersonnageEx(int e, int pv) {
      energie = e;
      ptVie = pv;
   }
   
   /**
    * Methode publique affichant le type de l'objet
    */
   public void afficheType() {
      System.out.println("Classe PersonnageEx");
   }
   
   // Fin de la classe
}