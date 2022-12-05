package org.centrale.objet.WoE;

public class Personnage  extends Entite{
    String nom;

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    Personnage() {}
    Personnage(String nom, int pV, int dA, int pPar, int paAtt, int paPar, Point2D p) {
        this.nom = nom;
    }
    Personnage(Personnage p) {}
    
}
