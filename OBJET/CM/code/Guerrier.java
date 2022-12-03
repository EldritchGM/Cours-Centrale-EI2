/**
 * Classe représentant un guerrier
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
   public Personnage(String n, int e, int pv, int ap) {
      nom = n;
      energie = e;
      ptVie = pv;
      arme = new Arme(ap);
   }
   
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
      arme = new Arme(100);
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
   public void setNom(Arme a) {
      arme = new Arme(a);
   }
   

  /**
    * Methode publique affichant le type de l'objet
    */
   @override
   public void afficheType() {
      System.out.println("Classe Guerrier");
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
   
}