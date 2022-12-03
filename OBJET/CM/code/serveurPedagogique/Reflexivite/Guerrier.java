/**
 * Classe representant un guerrier
 * @author jmnormand
 * @version 1.0
 */
public class Guerrier extends Personnage {
   // Attributs de la classe
   /**
    * Nom du personnage (protege)
    */
   protected Arme arme;

   // Constructeurs et methodes
   
   /**
    * Un constructeur avec une chaine de caracteres et trois entiers
    * en parametres.
    * @param n une chaine de caracteres contenant le nom du personnage
    * @param e un entier representant l'energie du personnage
    * @param pv un entier representant les points de vie du personnage
    * @param ap un entier representant la puissance de l'arme
    */
   public Guerrier(String n, int e, int pv, int ap) {
      super(n,e,pv);
      arme = new Arme(ap);
   }
   
   /**
    * Un constructeur avec une chaine de caracteres et deux entiers
    * en parametres.
    * @param n une chaine de caracteres contenant le nom du personnage
    * @param e un entier representant l'energie du personnage
    * @param pv un entier representant les points de vie du personnage
    */
   public Guerrier(String n, int e, int pv) {
      super(n,e,pv);
      arme = new Arme(1);
   }
   
   /**
    * Accesseur sur l'attribut 'arme'
    */
   public Arme getArme() {
      return arme;
   }
   
   /**
    * Modificateur de l'attribut 'arme'
    * attention on fait une recopie profonde
    * @param a la nouvelle arme du guerrier
    */
   public void setArme(Arme a) {
      arme = new Arme(a);
   }
   
   
   /**
    * Une méthode qui permet de rencontrer un autre personnage.
    * Redéfinition de la méthode 'rencontrer' de la classe 'Personnage'
    * @param autreP le personnage que l'on va rencontrer
    */
    public void rencontrer(Personnage autreP) {
      super.rencontrer(autreP);
      frapper(autreP);
   }
   
   
   public void frapper(Personnage autre) {
      System.out.println("Prends ca dans ta face !");
      autre.setPointsVie(autre.getPointsVie() - this.arme.getPuissance());
   }
   
   
}