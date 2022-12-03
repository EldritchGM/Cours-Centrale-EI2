class ControleComportementExecution {
	public static void main(String[] args) {
		// on suppose que le premier argument du programme est un entier
		int valeur=0;
		try {
			valeur = Integer.parseInt(args[0]);
		}
		catch (NumberFormatException e) {
			System.out.println("le programme doit etre appele avec un argument de type entier");
			return;
		}
		// suite du programme
		System.out.println("vous avez donne la valeur : "+valeur);
	}
}
