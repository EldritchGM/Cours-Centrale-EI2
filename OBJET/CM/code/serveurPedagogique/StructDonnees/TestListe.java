// Test Liste et Tableau
import java.util.*;

class TestListe {
    
    public static void main(String[] args){
        
        LinkedList<Integer> list = new LinkedList<Integer>();
        ArrayList<Integer> tab = new ArrayList<Integer>();
        
        // On remplit la liste et le tableau de trucs
        for(int i= 0;i<10000;i++){
            list.add(new Integer(i));
            tab.add(new Integer(i));
        }
        
        // puis on les affiche
        System.out.println("Affichage de la liste");
        long startTimeList = System.currentTimeMillis();

        for(int j =0; j<list.size();j++){
            System.out.println(list.get(j));
        }
        
        long stopTimeList = System.currentTimeMillis();
        long elapsedTimeList = stopTimeList - startTimeList;
        
        System.out.println("Affichage du tableau");
        long startTimeTab = System.currentTimeMillis();

        for(int j =0; j<tab.size();j++){
            System.out.println(tab.get(j));
        }
        
        long stopTimeTab = System.currentTimeMillis();
        long elapsedTimeTab = stopTimeTab - startTimeTab;
        System.out.println("Affichage de la liste en : "+elapsedTimeList+ "ms");
        System.out.println("Affichage de la tableau en : "+elapsedTimeTab+ "ms");
       
       // get(int index) est tres mauvais pour les LinkedList car pour chaque appel
       // a get refait le parcours de la liste depuis le début !
       
       Scanner scan = new Scanner(System.in);
       int i = scan.nextInt();
       
       // Essayons avec un iterateur pour voir
       System.out.println("Affichage avec iterateur de la liste");
       long startTimeListIt = System.currentTimeMillis();
       Iterator listIt = list.iterator();
       while(listIt.hasNext()) {
          System.out.println(listIt.next());
       }
       
       long stopTimeListIt = System.currentTimeMillis();
       long elapsedTimeListIt = stopTimeListIt - startTimeListIt;
       
       System.out.println("Affichage avec iterateur du tableau");
       long startTimeTabIt = System.currentTimeMillis();
       
       Iterator tabIt = tab.iterator();
       while(tabIt.hasNext()) {
          System.out.println(tabIt.next());
       }
       
       long stopTimeTabIt = System.currentTimeMillis();
       long elapsedTimeTabIt = stopTimeTabIt - startTimeTabIt;
       System.out.println("Affichage de la liste avec iterateur en : "+elapsedTimeListIt+ "ms");
       System.out.println("Affichage de la tableau avec iterateur en : "+elapsedTimeTabIt+ "ms");
       
    }
    
}