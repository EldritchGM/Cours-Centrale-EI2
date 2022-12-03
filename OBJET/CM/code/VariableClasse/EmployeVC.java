public class EmployeVC {
   private String nom;
   public static int ageRetraite = 65; // on doit le mettre en public dans cet exemple !
   
   public EmployeVC(String n) {
      this.nom = n;
   }
   
   public void afficheEmploye() {
      System.out.println("L'employe "+nom+" part a la retraite a: "+ageRetraite);
   }
}