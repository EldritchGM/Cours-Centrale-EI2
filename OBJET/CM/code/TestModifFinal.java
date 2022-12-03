public class TestModifFinal {
   
   public static void modifier(final PersonnageEx pers) {
      pers.setEnergie(10);
      pers = new PersonnageEx(10,10);
   }
   
   public static void main(String[] args)
   {
      PersonnageEx p = new PersonnageEx(100,25);
      modifier(p);
   }
}