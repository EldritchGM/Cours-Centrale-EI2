// Classe de test avec une fonction main
// illustrant le fonctionnement d'une classe generique

public class TestCouple {
   // Main
   public static void main(String[] args) {
      
      Couple<String, Boolean> dual = new Couple<String, Boolean>("toto", true);
      System.out.println("Valeur de l'objet dual : val1 = " + dual.getValeur1() + ", val2 = " + dual.getValeur2());
      
      Couple<Double, Character> dual2 = new Couple<Double, Character>(12.2585, 'C');
      System.out.println("Valeur de l'objet dual2 : val1 = " + dual2.getValeur1() + ", val2 = " + dual2.getValeur2());
   }
}