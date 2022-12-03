/**
 * Classe représentant un personnage basique
 * ayant seulement un nombre maximum de points de vie
 * et un nombre de points d'action (energie)
 * @author jmnormand
 * @version 1.0
 */
public class Personnage {
   
   // Attributs de la classe
   /**
    * Nom du personnage (protege)
    */
   protected String nom;
      
   /**
    * Quantite d'energie du personnage (protege)
    */
   protected int energie;
   
   /**
    * Nombre maximum de points de vie du personnage (protege)
    */
   protected int ptVie;
   
   // Constructeurs et methodes
   /**
    * Un constructeur avec une chaine de caracteres et deux entiers
    * en parametres.
    * @param n une chaine de caracteres contenant le nom du personnage
    * @param e un entier representant l'energie du personnage
    * @param pv un entier representant les points de vie du personnage
    */
   public Personnage(String n, int e, int pv) {
      nom = n;
      energie = e;
      ptVie = pv;
   }
   
   /**
    * Methode publique affichant le type de l'objet
    */
   public void afficheType() {
      System.out.println("Classe Personnage");
   }
   
   
   // Accesseurs et modificateurs
   
   /**
    * Accesseur sur l'attribut 'nom'
    */
   public String getNom() {
      return nom;
   }
   
   /**
    * Accesseur sur l'attribut 'energie'
    */
   public int getEnergie() {
      return energie;
   }
   
   /**
    * Accesseur sur l'attribut 'ptVie'
    */
   public int getPointsVie() {
      return ptVie;
   }
   
   /**
    * Modificateur de l'attribut 'nom'
    * @param n une chaine de caracteres contenant le nom du personnage
    */
   public void setNom(String n) {
      nom = n;
   }
   
   /**
    * Modificateur de l'attribut 'energie'
    * @param e un entier representant l'energie du personnage
    */
   public void setEnergie(int e) {
      energie = e;
   }
   
   /**
    * Modificateur de l'attribut 'ptVie'
    * @param pv un entier representant les points de vie du personnage
    */
   public void setPointsVie(int pv) {
      ptVie = pv;
   }
   
   
   public String toString()
   {
      String res;
      res = nom + " est un personnage avec "+ptVie+" points de vie, et "+energie+" points d'energie";
      return res;
   }
   
   /**
    * Surcharge de equals
    * @param p l'objet Personnage avec qui on veut comparer l'objet courant
    */
   public boolean equals(Personnage p) {
      if(p == null) {
         return false;
      }
      else {
         return (p.nom.equals(this.nom) && (p.energie == this.energie) && (p.ptVie == this.ptVie) );
      }
   }
   
   // Fin de la classe
}