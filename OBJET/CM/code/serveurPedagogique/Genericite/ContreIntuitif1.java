import java.util.List;
import java.util.ArrayList;

public class ContreIntuitif1 {
	public static void main(String[] args) {
		List<String> l = new ArrayList<String>();
		List<Object> l2 = l; // alias pour la liste de chaines
		l2.add(new Object()); // ajout dans la liste d'objet
		String s = l.get(0);
	}
}
