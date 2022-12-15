package org.centrale.objet.WoE;

public class Point2D {
    private int x, y;
    Point2D(){}
    Point2D(int x, int y) {
        this.x = x;
        this.y = y;
    }
    Point2D(Point2D p) {
        this.x = p.x;
        this.y = p.y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getX() {
        return x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getY() {
        return y;
    }    

    public void setPosition(int x, int y) {
        this.setX(x);
        this.setY(y);
    }

    public void translate(int dx, int dy) {
        x = x + dx;
        y = y + dy;
    }

    public void affiche() {
        System.out.println("Point (" + x + ", " + y + ")");
    }

    public double distance(Point2D p) {
        double deltaX = x - p.x;
        double deltaY = y - p.y;
        double distance = Math.sqrt(Math.pow(deltaX, 2) + Math.pow(deltaY, 2));
        return distance;
    } 

    public static double distance(Point2D p1, Point2D p2) {
        double deltaX = p1.x - p2.x;
        double deltaY = p1.y - p2.y;
        double distance = Math.sqrt(Math.pow(deltaX, 2) + Math.pow(deltaY, 2));
        return distance;
    }
}
