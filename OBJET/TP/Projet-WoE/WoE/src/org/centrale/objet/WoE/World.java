package org.centrale.objet.WoE;
import java.util.Random;


public class World {

    private Archer robin;
    private Paysan peon;
    private Lapin bugs1;
    private Lapin bugs2;

    World() {}
    public static World creerMondeAlea() {
        World world = new World();
        world.robin = new Archer();
        world.peon = new Paysan();
        world.bugs1 = new Lapin();
        world.bugs2 = new Lapin();
        Entite[] liste_entite = {world.robin, world.peon, world.bugs1, world.bugs2};
        Point2D[] liste_position = {new Point2D(-1, -1), new Point2D(-1, -1), new Point2D(-1, -1), new Point2D(-1, -1)};

        Random rng_generator = new Random();
        for (Entite ent: liste_entite) {
            boolean flag = true;
            int x, y;
            do {
                x = rng_generator.nextInt(100);
                y = rng_generator.nextInt(100);
                for (Point2D p: liste_position) {
                    if (p.getX() == x && p.getY() == y){
                        flag = false;
                    }
                }
            } while (!flag);
            
            ent.setPos(new Point2D(x, y));
        }

        return world;
    }
    
}
