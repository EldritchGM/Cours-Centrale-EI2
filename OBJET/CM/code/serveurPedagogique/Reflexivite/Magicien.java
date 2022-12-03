/**
 * Classe representant un magicien
 * @author jmnormand
 * @version 1.0
 */
public class Magicien extends Personnage {
   // Attributs de la classe
   /**
    * Nom du personnage (protege)
    */
   protected Baguette baguette;
   
   // Constructeurs et methodes
   
   /**
    * Un constructeur avec une chaine de caracteres et trois entiers
    * en parametres.
    * @param n une chaine de caracteres contenant le nom du personnage
    * @param e un entier representant l'energie du personnage
    * @param pv un entier representant les points de vie du personnage
    * @param ap un entier representant la puissance de la baguette
    */
   public Magicien(String n, int e, int pv, int bp) {
      super(n,e,pv);
      baguette = new Baguette(bp);
   }
   
   /**
    * Un constructeur avec une chaine de caracteres et deux entiers
    * en parametres.
    * @param n une chaine de caracteres contenant le nom du personnage
    * @param e un entier representant l'energie du personnage
    * @param pv un entier representant les points de vie du personnage
    */
   public Magicien(String n, int e, int pv) {
      super(n,e,pv);
      baguette = new Baguette(1);
   }
   
   /**
    * Accesseur sur l'attribut 'baguette'
    */
   public Baguette getBaguette() {
      return baguette;
   }
   
   /**
    * Modificateur de l'attribut 'arme'
    * attention on fait une recopie profonde
    * @param a la nouvelle arme du guerrier
    */
   public void setBaguette(Baguette b) {
      baguette = new Baguette(b);
   }
   
}