// Classe adaptee depuis le cours d'OpenClassRooms
// Apprenez a programmer en Java
public class Couple<T, S> {

   // Variable d'instance de type T
   private T valeur1;
   
   // Variable d'instance de type S
   private S valeur2;
   
   // Constructeur par defaut
   public Couple(){
      this.valeur1 = null;
      this.valeur2 = null;
   }
   
   // Constructeur avec parametres
   public Couple(T val1, S val2){
      this.valeur1 = val1;
      this.valeur2 = val2;
   }
   
   // Methodes d'initialisation des deux valeurs
   public void setValeurs(T val1, S val2){
      this.valeur1 = val1;
      this.valeur2 = val2;
   }
   
   // Retourne la valeur T
   public T getValeur1() {
      return valeur1;
   }
   
   // Definit la valeur T
   public void setValeur1(T valeur1) {
      this.valeur1 = valeur1;
   }
   
   // Retourne la valeur S
   public S getValeur2() {
      return valeur2;
   }
   
   // Definit la valeur S
   public void setValeur2(S valeur2) {
      this.valeur2 = valeur2;
   }
}