// Classe de test avec une fonction main
// illustrant le fonctionnement d'une classe generique

public class TestValeurGenerique {
   // Main
   public static void main(String[] args) {
      // Une 'ValeurGenerique' instanciee avec la classe 'Integer'
      ValeurGenerique<Integer> v1 = new ValeurGenerique<Integer>(23);

      // Une 'ValeurGenerique' instanciee avec la classe 'String'
      ValeurGenerique<String> v2 = new ValeurGenerique<String>("Ma Valeur Générique");

      // Utilisation des methodes
      System.out.println("La valeur generique entiere est : "+v1.getValeur());
      System.out.println("La valeur generique chaine de caracteres est : "+v2.getValeur());
      
      // Modification
      v1.setValeur(58);
      v2.setValeur("Je change!");
      
      // Verification
      System.out.println("La valeur generique entiere est : "+v1.getValeur());
      System.out.println("La valeur generique chaine de caracteres est : "+v2.getValeur());
      
      // Interdit !
      v1.setValeur(2.5); // 2.5 n'est pas de type 'Integer' (c'est un 'double')
      v2.setValeur('a'); // 'a' n'est pas de type 'String' (c'est un 'char')
   }

}