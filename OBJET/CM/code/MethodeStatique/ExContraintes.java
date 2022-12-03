public class A {
   private int monAttrib;
   private static int maVarStatique;
   
   public void methodeClassique() {
      System.out.println(i);  // OK
      System.out.println(j);  // OK
      methodeStatique();      // OK
   }
   
   public static void methodeStatique() {
      System.out.println(i);  // Erreur !
      System.out.println(j);  // OK
      methodeClassique();     // Erreur !
      methodeStatique();      // Autorise mais idiot
      
      A mA = new A();
      mA.methodeClassique();  // OK
   }
}