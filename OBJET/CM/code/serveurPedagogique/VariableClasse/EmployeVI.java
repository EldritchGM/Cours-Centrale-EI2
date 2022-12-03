public class EmployeVI {
   private String nom;
   private int ageRetraite;
   
   public EmployeVI(String n, int ar) {
      this.nom = n;
      this.ageRetraite = ar;
   }
   
   public void setAgeRetraite(int nar) {
      this.ageRetraite = nar;
   }
   
   public void afficheEmploye() {
      System.out.println("L'employe "+nom+" part a la retraite a: "+ageRetraite);
   }
}