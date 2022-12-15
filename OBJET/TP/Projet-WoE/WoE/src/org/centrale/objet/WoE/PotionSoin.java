package org.centrale.objet.WoE;

public class PotionSoin {

    private int soin;

    PotionSoin() {}
    PotionSoin(int soin) {
        this.soin = soin;
    }

    public void soigne(Creature c) {
        c.setPtVie(c.getPtVie() + soin);
    }
    
}
