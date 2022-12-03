import java.util.ArrayList;

public class ArrayListObject {
   
   public static void main(String[] args)
   {
      ArrayList l = new ArrayList(); // attention syntaxe non recommandee ! voir cours
      l.add(new Integer(34));
      l.add(new String("essai"));
      l.add(new Float(34.4));
      String c = (String) l.get(1);
      for (int i=0 ; i<l.size() ; i++) {
         System.out.println("l'element ("+i+") est de type "+l.get(i).getClass().getName());
      }
   }
   
}