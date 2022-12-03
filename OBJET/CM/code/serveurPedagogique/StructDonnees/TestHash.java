// Use iterators with a Hashtable.
import java.util.*;

class TestHash {

    public static void main(String args[]) {
        HashMap<String,Double> balance = new HashMap<String,Double>();
        String str;
        double bal;
        Double prevValue;
        Double val;
        
        prevValue = balance.put("John Doe", new Double(3434.34));
        if(prevValue != null){
            System.out.println("Cette cle etait precedemment utilisee par "+prevValue);
        }
        
        balance.put("Tom Smith", new Double(123.22));
        balance.put("Jane Baker", new Double(1378.00));
        balance.put("Todd Hall", new Double(99.22));
        balance.put("Ralph Smith", new Double(-19.08));
       
       // TEST
       balance.put("Tom Smith", new Double(0.22));
       
        
        // Try to add again someone named Jane Baker
        prevValue = balance.put("Jane Baker",new Double(-258.24));
        if(prevValue != null){
            System.out.println("Cette cle etait precedemment utilisee par "+prevValue);
        }
        
        // show all balances in hashtable
        Set<String> setK = balance.keySet(); // get set-view of keys
        // get iterator
        Iterator itr = setK.iterator();
        while (itr.hasNext()) {
            str = (String) itr.next();
            System.out.println(str + ": " + balance.get(str));
        }
        System.out.println();
        
        
        // We can also parse the hashmap using the 'values' method
        // that gives us the set of values of the hashmap
        Collection<Double> arrValues = balance.values();
        Iterator itV = arrValues.iterator();
        while(itV.hasNext()){
            val = (Double)itV.next();
            System.out.println("On ne peut pas recuperer de cette facon la cle de la valeur: "+val);
        }
        
        // Yet another manner of parsing the hashmap
        Set<Map.Entry<String,Double>> couplesKV = balance.entrySet();
        for(Map.Entry<String,Double> e : couplesKV){
            System.out.println("La cle: "+e.getKey()+" correspond a la valeur: "+e.getValue());
        }
        
        // Deposit 1,000 into John Doe's account
        bal = ((Double) balance.get("John Doe")).doubleValue();
        balance.put("John Doe", new Double(bal + 1000));
        System.out.println("John Doe's new balance: "+ balance.get("John Doe"));
    }
}