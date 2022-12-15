package org.centrale.objet.WoE;
import java.util.Random;


public class World {

    public Archer robin;
    public Paysan peon;
    public Lapin bugs1;
    public Lapin bugs2;
    public Archer guillaumeT;
    public Loup wolfie;
    public Guerrier grosBill;

    World() {}
    public static World creerMondeAlea() {
        World world = new World();
        world.robin = new Archer("Robin", 12, 3, 1, 60, 40, new Point2D(-1, -1), 5, 5);
        world.peon = new Paysan();
        world.bugs1 = new Lapin();
        world.bugs2 = new Lapin();
        world.wolfie = new Loup();
        world.grosBill = new Guerrier();
        Creature[] liste_Creature = {world.robin, world.peon, world.bugs1, world.bugs2};
        Point2D[] liste_position = {new Point2D(-1, -1), new Point2D(-1, -1), new Point2D(-1, -1), new Point2D(-1, -1)};

        Random rng_generator = new Random();
        for (Creature ent: liste_Creature) {
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
        world.guillaumeT = new Archer(world.robin);

        return world;
    }
    
}
