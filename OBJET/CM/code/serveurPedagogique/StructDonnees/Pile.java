// Classe implémentant l'algorithm de verification
// du parenthesage d'une expression 

import java.io.*;
import java.util.Stack;
import java.util.EmptyStackException;

enum ResultatParenthesage {_ERROR_UNDEFINED, _MISSING_OPEN_PAR, _MISSING_CLOSE_PAR, _OK};

public class Pile {
    
    public static ResultatParenthesage verificationExpression(String expr){
        // Declaration d'une stack
        Stack<Character> myPile = new Stack<Character>();
    
        // Resultat : 
        ResultatParenthesage result = ResultatParenthesage._ERROR_UNDEFINED;
        
        // Parcours de l'expression
        for(int i=0;i<expr.length();i++){
            Character curChar = expr.charAt(i);
            //System.out.println("curChar: "+curChar);
            if(curChar == '('){
                myPile.push(curChar);
                //System.out.println("Parenthese ouvrante detectee");
            }
            
            if(curChar == ')'){
                //System.out.println("Parenthese fermante detectee");
                try{
                    myPile.pop();
                }
                catch(EmptyStackException e){
                    //System.out.println("Il manque une parenthèse ouvrante!");
                    return ResultatParenthesage._MISSING_OPEN_PAR;
                }
            }
        }
        // Si la pile est vide alors l'expression est bien parenthesee
        if(myPile.empty())
            result = ResultatParenthesage._OK;
        else{
            // Si la pile n'est pas vide alors il manque une parenthese fermante
            result = ResultatParenthesage._MISSING_CLOSE_PAR;
        }
        
        return result;
    }
    
    public static void afficheResultatParenthesage(String expr, ResultatParenthesage r){
        System.out.print("L'expression: "+expr+ " ");
        
        switch(r){
            case _MISSING_OPEN_PAR:
                System.out.println(" est mal parenthesee, il manque une parenthese ouvrante!");
            break;
            
            case _MISSING_CLOSE_PAR:
                System.out.println(" est mal parenthesee, il manque une parenthese fermante!");
            break;
            
            case _OK:
                System.out.println(" est bien parenthesee!");
            break;
            default:
                System.out.println(" a rencontrée une erreur identifiée.");
            break;
        }
    }
    
    public static void main(String[] args){
    
        // Expression a tester
        String expr1 = "((3+2)*(2-4))";
        String expr2 = "2+(6-(4*5))";
        String expr3 = "5+(1-2)+6)";
        String expr4 = ")2+3)";
    
        // Testons nos methodes
        ResultatParenthesage testExpr;
        
        // Expresson 1
        testExpr = verificationExpression(expr1);
        afficheResultatParenthesage(expr1, testExpr);
        System.out.println();
        
        // Expresson 2
        testExpr = verificationExpression(expr2);
        afficheResultatParenthesage(expr2, testExpr);
        System.out.println();
        
        // Expression 3
        testExpr = verificationExpression(expr3);
        afficheResultatParenthesage(expr3, testExpr);
        System.out.println();
        
        // Expression 4
        testExpr = verificationExpression(expr4);
        afficheResultatParenthesage(expr4, testExpr);
        System.out.println();
                
    }
    
    
}