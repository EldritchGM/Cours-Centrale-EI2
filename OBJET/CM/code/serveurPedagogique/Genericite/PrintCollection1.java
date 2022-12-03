import java.util.Collection;
import java.util.Iterator;

public class PrintCollection1 {

	// premiere version pour java <= 1.4.2
	public void printCollection(Collection c) {
		Iterator i = c.iterator();
		for (int k=0 ; k<c.size(); k++) {
			System.out.println(i.next());
		}
	}
   
	public static void main(String[] args) {
	}
}
