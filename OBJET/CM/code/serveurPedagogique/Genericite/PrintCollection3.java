import java.util.Collection;
import java.util.Iterator;
import java.util.ArrayList;

public class PrintCollection3 {

	// seconde version pour java >= 5 avec wilcard
	public static void printCollection(Collection<?> c) {
		for (Object x : c) {
			System.out.println(x);
		}
	}
	
	
	public static void main(String[] args) {
		ArrayList<String> lls  = new ArrayList<String>();
		lls.add(new String ("a"));
		lls.add(new String ("b"));
		lls.add(new String ("c"));
		lls.add(new String ("D"));
		
		PrintCollection3.printCollection(lls);
	}
}
