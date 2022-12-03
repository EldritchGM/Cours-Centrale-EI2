// Jean-Marie Normand

// Generation de nombres aléatoires en Java
import java.util.Random;
// I/O
import java.io.*;

// Ma classe qui illustre une matrice de Point
public class MatPoint{
    
    public static void main(String[] args){
    
        // Création de la graine du générat"ur de nombres pseudos-aléatoires
        Random generator = new Random(System.currentTimeMillis());
        
        // Déclaration d'une matrice de Points
        Point[][] matriceP;
        
        // il faut l'initialiser
        // stockons 150 Objets de type Point par exemple
        matriceP = new Point[10][15];
        
        // il faut donc penser à créer tous les Point!!!
        // parcours des lignes
        for(int l=0;l<matriceP.length;l++){
            // parcours de chaque colonne
            for(int c=0;c<matriceP[l].length;c++){
                
                int x = generator.nextInt(200);
                int y = generator.nextInt(200);
                                
                matriceP[l][c] = new Point(x,y);
                
                System.out.println("Matrice["+l+"]["+c+"] = new Point("+x+","+y+")");
                
            }
        }
    
    }
}