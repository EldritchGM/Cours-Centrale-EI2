import java.lang.Class;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

public class TestPaire {
   public static void main(String[] args) {
      // Creation d'instance sans parametre
      try {
         Class clPaire = Class.forName("Paire");
         Object o1 = clPaire.newInstance();
         
         // Creation d'instance avec parametres
         Class[] types = new Class[] {String.class, String.class};
         Constructor ctPaireParam = clPaire.getConstructor(types);
         Object o2 = ctPaireParam.newInstance((Object[])new String[]{"toto","titi"});
         
         // Appel de methodes
         Method m = clPaire.getMethod("toString");
         // toString n'a pas de parametre
         System.out.println("o1: "+m.invoke(o1));
         Paire p2 = (Paire)o2; // transtypage
         System.out.println("o2: "+o2);
      }
      catch(ClassNotFoundException e) {
         System.out.println(e.getMessage());
         return;
      }
      catch(InstantiationException e) {
         System.out.println(e.getMessage());
         return;
      }
      catch(NoSuchMethodException e) {
         System.out.println(e.getMessage());
         return;
      }
      catch(InvocationTargetException e) {
         System.out.println(e.getMessage());
         return;
      }
      catch(IllegalAccessException e) {
         System.out.println(e.getMessage());
         return;
      }

   }
}