public class EntrepriseVI {

   public static void main(String[] args) {
      EmployeVI[] employes = new EmployeVI[5];
      employes[0] = new EmployeVI("John Doe", 65);
      employes[1] = new EmployeVI("Mary Lee", 65);
      employes[2] = new EmployeVI("Tim Johnson", 65);
      employes[3] = new EmployeVI("Elizabeth Steed", 65);
      employes[4] = new EmployeVI("Ashley Martin", 65);
      
      // Si un jour l'age de la retraite est modifie
      // il va falloir modifier la valeur de l'attribut
      // pour TOUS les objets !
      for(int i= 0;i<employes.length; i++) {
         employes[i].setAgeRetraite(67);
      }
      
   }
}