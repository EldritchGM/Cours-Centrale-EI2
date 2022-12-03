// Normand Jean-Marie
// Exemple de la classe Point

public class Point{
    // Attributs : Abscisse et Ordonnee d'un point 2D
    private int x;
    private int y;
    
    // Constructeur sans parametre
    // Initialisation des attributs a une valeur par defaut
    public Point(){
        x = 0;
        y = 0;
    }
    
    // Constructeur avec 2 arguments: les valeurs
    // des abscisses et des ordonnees
    public Point(int a, int b){
        x = a; // this.x = a;
        y = b; // this.y = b;
    }
    
    // Constructeur par recopie
    public Point(Point p){
        x = p.x; // this.x = p.getX(); // this.x = p.x;
        y = p.y; // this.y = p.getY(); // this.y = p.y;
    }
    
    // Accesseurs
    public int getX(){
        return x; // return this.x;
    }
    
    public int getY(){
        return y; // return this.y;
    }
    
    // Translation du point "courant" par un vecteur 2D
    public void translate(int vx, int vy){
        x = x + vx;
        y = y + vy;
    }
    
    // Methode d'affichage d'un point
    public void affichePoint(){
        System.out.println("Point de coordonnes: ["+x+","+y+"]");
    }
    
}
