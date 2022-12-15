package org.centrale.objet.WoE;

public class Epee {

    private boolean equipee;
    private int degats;

    Epee() {}
    Epee(int deg) {}

    public void equipe(Creature c) {
        if (equipee) {
            equipee = false;
            c.setDegAtt(c.getDegAtt() - degats);
        } else {
            equipee = true;
            c.setDegAtt(c.getDegAtt() + degats);
        }
    }


    
}
