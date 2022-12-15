package org.centrale.objet.WoE;
import java.util.Random;

public class Guerrier extends Personnage{

    Guerrier() {
        super();
    }
    Guerrier(String nom, int pV, int dA, int pPar, int paAtt, int paPar, Point2D p, int distAttMax, int nbProjectiles) {
        super(nom, pV, dA, pPar, paAtt, paPar, p, distAttMax, nbProjectiles);
    }
    Guerrier(Guerrier g) {
        super(g);
    }
    
    public void Combattre(Creature c) {
        double distance = Point2D.distance(this.getPos(), c.getPos());
        if (distance == 1) {
            this.CbtContact(c);
            return;
        }
        if (distance < this.distAttMax) {
            this.CbtDistance(c);
            return;
        }
        System.out.println("La créature est hors de portée");
    }

    public void CbtContact(Creature c) {
        Random RNG = new Random();
        int rand = RNG.nextInt(99) + 1;
        if (rand > this.pageAtt) {
            System.out.println("Attaque ratée");
        } else {
            System.out.println("Attaque réussie");
            int degats = this.degAtt;
            rand = RNG.nextInt(99) + 1;
            if (rand <= c.getPagePar()) {
                degats -= c.getPtPar();
            }
            System.out.println("La créature subit " + degats + " degats." );
            c.setPtVie(c.getPtVie() - degats);
            if (c.getPtVie() <= 0) {
                System.out.println("La créature est morte.");
            }
        }
    }

    public void CbtDistance(Creature c) {
        Random RNG = new Random();
        if (this.getNbProjectiles() <= 0) {
            System.out.print("Vous n'avez plus de projectiles");
        }
        this.setNbProjectiles(this.getNbProjectiles() - 1);
        int rand = RNG.nextInt(99) + 1;
        if (rand > pageAtt) {
            System.out.println("Attaque ratée");
        } else {
            System.out.println("Attaque réussie");
            int degats = this.degAtt;
            System.out.println("La créature subit " + degats + " degats." );
            c.setPtVie(c.getPtVie() - degats);
            if (c.getPtVie() <= 0) {
                System.out.println("La créature est morte.");
            }
        }
    }

}
