package org.centrale.objet.WoE;

import java.util.Random;;

public class Loup extends Monstre{
    Loup() {}
    Loup(int pV, int dA, int pPar, int paAtt, int paPar, Point2D p) {}
    Loup(Loup l) {}

    public void Combattre(Creature c) {
        double distance = Point2D.distance(this.getPos(), c.getPos());
        if (distance == 1) {
            this.CbtContact(c);
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

}
