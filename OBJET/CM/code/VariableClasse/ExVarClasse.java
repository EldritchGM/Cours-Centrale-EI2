public class ExVarClasse {
   public static void main(String[] args) {
      // creation d'un objet de type A
      A monObjA = new A(25);
      // appel de la methode d'increment des variables
      monObjA.incrVariables();
      // affichage de monObjA
      monObjA.affiche();
      
      A.maVarClasse = 0;
      
      // creation d'un objet de type A
      A monObjB = new A(1);
      // appel de la methode d'increment des variables
      monObjB.incrVariables();
      // affichage de monObjB
      monObjB.affiche();
      // appel de la methode d'increment des variables
      monObjA.incrVariables();
      // affichage de monObjA
      monObjA.affiche();
      // affichage de monObjB
      monObjB.affiche();
   }

}