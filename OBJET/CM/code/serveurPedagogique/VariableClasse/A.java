public class A {
   // variable d'instance
   private int monAttrib;
   // variable de classe
   // /!\ initialisation en dehors d'une methode
   static public int maVarClasse = 100;
   
   // constructeur
   public A(int a) {
      monAttrib = a;
   }
   
   public void incrVariables() {
      monAttrib++;
      maVarClasse++;
   }
   
   public void affiche() {
      System.out.println("monAttrib: "+monAttrib+" - maVarClasse: "+maVarClasse);
   }

}