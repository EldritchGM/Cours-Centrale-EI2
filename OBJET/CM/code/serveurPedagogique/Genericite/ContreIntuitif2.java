import java.util.List;
import java.util.ArrayList;

public class ContreIntuitif2 {
	public static void main(String[] args) {
		CoupleHomogene<Object> co = new CoupleHomogene<Object>(
			new Object(),new Object());
		CoupleHomogene<Integer> ci = new CoupleHomogene<Integer>(5,6);
		ci.echange();
		Integer i = ci.getA();
		co = ci;
	}
}
