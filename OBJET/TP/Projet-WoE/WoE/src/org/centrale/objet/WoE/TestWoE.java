package org.centrale.objet.WoE;

public class TestWoE {
    public static void main(String[] args) {
        World world = World.creerMondeAlea();
        System.out.println("Avant déplacement:");
        System.out.println("Robin: ");
        world.robin.affiche();
        System.out.println("GuillaumeT: ");
        world.guillaumeT.affiche();
        System.out.println("Après déplacement: ");
        world.robin.deplace();
        System.out.println("Robin: ");
        world.robin.affiche();
        System.out.println("GuillaumeT: ");
        world.guillaumeT.affiche();
        System.out.println("Distance entre nos deux protagonistes: " + Point2D.distance(world.robin.getPos(), world.guillaumeT.getPos()));

        while (world.guillaumeT.getPtVie() > 0 && world.robin.getPtVie() > 0) {
            world.robin.Combattre(world.guillaumeT);
            if (world.guillaumeT.getPtVie() > 0) {
                world.guillaumeT.Combattre(world.robin);
            }
        }
        if (world.guillaumeT.getPtVie() <= 0)  {
            System.out.println("Guillaume Tell a été vaincu");
        }
        if (world.robin.getPtVie() <= 0)  {
            System.out.println("Robin a été vaincu");
        }

    }
    
}
