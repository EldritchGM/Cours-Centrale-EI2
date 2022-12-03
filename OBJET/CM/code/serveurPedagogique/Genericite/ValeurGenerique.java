// Classe adaptee depuis le cours d'OpenClassRooms : Apprenez a programmer en Java
public class ValeurGenerique<T> {
   // Variable d'instance (attribut)
   private T valeur;
   
   // Constructeur par defaut
   public ValeurGenerique(){
      this.valeur = null;
   }
   
   // Constructeur avec un parametre inconnu pour l'instant
   public ValeurGenerique(T val){
      this.valeur = val;
   }
   
   // Definit la valeur avec le parametre
   public void setValeur(T val){
      this.valeur = val;
   }
   
   // Retourne la valeur avec le bon type !
   public T getValeur(){
      return this.valeur;
   }
}