package org.centrale.objet.WoE;
import java.util.Random;

public class Creature {
    protected int ptVie, degAtt, ptPar, pageAtt, pagePar;
    protected Point2D pos;

    Creature() {}
    Creature(int pV, int dA, int pPar, int paAtt, int paPar, Point2D p) {
        ptVie = pV;
        degAtt = dA;
        ptPar = pPar;
        pageAtt = paAtt;
        pagePar = paPar;
        pos = p;
    }
    Creature(Creature e) {
        this.ptVie = e.ptVie;
        this.degAtt = e.degAtt;
        this.ptPar = e.ptPar;
        this.pageAtt = e.pageAtt;
        this.pagePar = e.pagePar;
        this.pos = new Point2D(e.pos.getX(), e.pos.getY());
    }

    public int getPtVie() {
        return ptVie;
    }

    public void setPtVie(int ptVie) {
        this.ptVie = ptVie;
    }

    public int getDegAtt() {
        return degAtt;
    }
    
    public void setDegAtt(int degAtt) {
        this.degAtt = degAtt;
    }

    public int getPtPar() {
        return ptPar;
    }

    public void setPtPar(int ptPar) {
        this.ptPar = ptPar;
    }

    public int getPageAtt() {
        return pageAtt;
    }

    public void setPageAtt(int pageAtt) {
        this.pageAtt = pageAtt;
    }

    public int getPagePar() {
        return pagePar;
    }

    public void setPagePar(int pagePar) {
        this.pagePar = pagePar;
    }

    public Point2D getPos() {
        return pos;
    }

    public void setPos(Point2D pos) {
        this.pos = pos;
    }

    public void deplace() {
        Random rng_generator = new Random();
        int dx, dy;
        do {
            dx = rng_generator.nextInt(2) - 1;
            dy = rng_generator.nextInt(2) - 1;
        } while (dx == 0 && dy == 0); 
        
        this.pos.translate(dx, dy);
    }

    public void affiche() {
        System.out.println("Position: (" + this.pos.getX() + ", " + this.pos.getY() + ")");
    }

}
