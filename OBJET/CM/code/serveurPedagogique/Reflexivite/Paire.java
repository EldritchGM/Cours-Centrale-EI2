public class Paire {
   private String val1;
   private String val2;
   
   public Paire() {
      val1 = "defaultV1";
      val2 = "defaultV2";
   }
   
   public Paire(String v1, String v2) {
      val1 = v1;
      val2 = v2;
   }
   
   public String toString() {
      String s;
      s = val1+" "+val2;
      return s;
   }
}