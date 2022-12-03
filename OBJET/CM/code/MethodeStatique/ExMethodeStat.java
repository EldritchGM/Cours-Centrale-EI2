public class ExMethodeStat {
   public static void main(String[] args) {
      A.methodeStatique(); // OK
      A.methodeClassique(); // Erreur de compilation
      
      A monObjA = new A();
      monObjA.methodeStatique(); // OK (alternative)
      monObjA.methodeClassique(); // OK (comme d'habitude)
   }
}