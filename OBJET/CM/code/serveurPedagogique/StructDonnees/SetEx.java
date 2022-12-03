// Example of set implementation in Java
import java.util.HashSet;
import java.util.Iterator;
import java.io.*;

public class SetEx {
    
    public static void main(String[] args){
        // 1st HashSet
        HashSet<Character> set1 = new HashSet<Character>();
        // 2nd HashSet
        HashSet<Character> set2 = new HashSet<Character>();
        
        // Adding a couple of objects
        set1.add(new Character('a'));
        set1.add(new Character('b'));
        set1.add(new Character('c'));
        set1.add(new Character('d'));
        set1.add(new Character('d'));
        
        // Outputting set1
        Iterator setIt = set1.iterator();
        System.out.println("Set1 contains: ");
        while(setIt.hasNext()){
            System.out.println(setIt.next());
        }
        System.out.println();
        
        // Adding a couple of elements to set2
        set2.add(new Character('d'));
        set2.add(new Character('e'));
        set2.add(new Character('f'));
        set2.add(new Character('g'));
        
        // Outputting set2
        setIt = set2.iterator();
        System.out.println("Set2 contains: ");
        while(setIt.hasNext()){
            System.out.println(setIt.next());
        }
        System.out.println();
        
        // Testing operations on sets
        HashSet<Character> set3 = new HashSet<Character>(set1);
        // Set3 = Set1 U Set2
        set3.addAll(set2);
        
        // Outputting set3
        setIt = set3.iterator();
        System.out.println("Set3 contains: ");
        while(setIt.hasNext()){
            System.out.println(setIt.next());
        }
        System.out.println();
       
        
        // Set3 = Set3 - Set2 == ?
        set3.removeAll(set2);
        // Outputting set3
        setIt = set3.iterator();
        System.out.println("Set3 contains: ");
        while(setIt.hasNext()){
            System.out.println(setIt.next());
        }
        System.out.println();
        
        
        // Set1 = Set1 INTER Set2
        set1.retainAll(set2);
        // Outputting set1
        setIt = set1.iterator();
        System.out.println("Set1 contains: ");
        while(setIt.hasNext()){
            System.out.println(setIt.next());
        }
        System.out.println();
    }
    
}