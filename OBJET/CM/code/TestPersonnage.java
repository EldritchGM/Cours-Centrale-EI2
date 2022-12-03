public class TestPersonnage {
   public static void main(String[] args)
   {
      PersonnageEx p = new PersonnageEx(100,25);
      System.out.println(p);
      
      PersonnageEx p1 = new PersonnageEx(150,99);
      PersonnageEx p2 = new PersonnageEx(150,99);
      if(p1 == p2) {
         System.out.println("Les personnages sont identiques");
      }
      else {
         System.out.println("Ces personnages sont differents");
      }
   }
}