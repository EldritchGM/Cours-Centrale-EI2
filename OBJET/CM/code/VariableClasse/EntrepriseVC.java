public class EntrepriseVC {
   
   public static void main(String[] args) {
      EmployeVC[] employes = new EmployeVC[5];
      employes[0] = new EmployeVC("John Doe");
      employes[1] = new EmployeVC("Mary Lee");
      employes[2] = new EmployeVC("Tim Johnson");
      employes[3] = new EmployeVC("Elizabeth Steed");
      employes[4] = new EmployeVC("Ashley Martin");
      
      // Si un jour l'age de la retraite est modifie
      // il suffit de la modifier une seule fois pour tous les objets!
      EmployeVC.ageRetraite = 67;
      // ou bien
      employes[0].ageRetraite = 67; // c'est equivalent !
   }
}