// classe couple generique
public class CoupleHomogene<T> {
	private T a;
	private T b;
	
	public CoupleHomogene(T a,T b) {
		this.a = a;
		this.b = b;
	}
	
	public void echange() {
		T local = a;
		a = b;
		b = local;
	}
	
	public T getA() {
		return a;
	}
	
	public T getB() {
		return b;
	}
	
	public void setA(T a) {
		this.a = a;
	}
	
	public void setB(T b) {
		this.b = b;
	}
	
	public static void main(String[] args) {
		CoupleHomogene<Integer> c = new CoupleHomogene<Integer>(
			new Integer(22), new Integer(243));
		System.out.println(c.getA());
		c.echange();
		System.out.println(c.getA());
	}
}
