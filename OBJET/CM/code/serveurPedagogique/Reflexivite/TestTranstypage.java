import java.util.ArrayList;
import java.util.List;

public class TestTranstypage {

   public static final void main(String[] args) {
      Guerrier monG = new Guerrier("Jack", 100, 150, 4);
      Magicien monM = new Magicien("Bill", 100, 100, 2);
      List<Personnage> listP = new ArrayList<>();
      listP.add(monG);
      listP.add(monM);
      // Attention je triche !!
      for(Personnage p : listP) {
         if(p instanceof Guerrier) {
            ((Guerrier)p).frapper(monM);
         }
         else {
            p.rencontrer(monG);
         }
      }
   }

}