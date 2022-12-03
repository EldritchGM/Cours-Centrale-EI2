class TestComparaison {

   public static void main(String[] args) {
      Personnage p1 = new Personnage("toto", 100, 100);
      Personnage p2 = new Personnage("toto", 100, 100);
      
      if(p1.equals(p2)) {
         System.out.println("Les personnages sont identiques !");
      }
      else {
         System.out.println("Ces personnages sont differents...");
      }
   }

}