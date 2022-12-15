package org.centrale.objet.WoE;

public class Personnage  extends Creature{
    protected String nom;
    protected int distAttMax;
    private int nbProjectiles;


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getDistAttMax() {
        return distAttMax;
    }

    public void setDistAttMax(int distAttMax) {
        this.distAttMax = distAttMax;
    }

    public int getNbProjectiles() {
        return nbProjectiles;
    }

    public void setNbProjectiles(int nbProjectiles) {
        this.nbProjectiles = nbProjectiles;
    }

    Personnage() {
        super();
    }
    Personnage(String nom, int pV, int dA, int pPar, int paAtt, int paPar, Point2D p, int distAttMax, int nbProjectiles) {
        super(pV, dA, pPar, paAtt, paPar, p);
        this.nom = nom;
        this.distAttMax = distAttMax;
        this.nbProjectiles = nbProjectiles;
    }
    Personnage(Personnage p) {
        super(p);
    }
    
}
