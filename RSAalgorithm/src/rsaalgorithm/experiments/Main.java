/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rsaalgorithm.experiments;

import java.io.IOException;

/**
 *
 * @author danielalvarado
 */
public class Main { 
    Main() {}
    public static void main(String[] args) throws IOException {
        //Experiment with 1 byte
        Experiment ex1 = new Experiment(1000,"D");
        System.out.println("Average time of 1 byte: " + ex1.avgTime/1000000.0);
        
        Experiment ex2 = new Experiment(1000,"DDDDDDDDDD");
        System.out.println("Average time of 10 byte: " + (ex2.avgTime/1000000.0));
        
        Experiment ex3 = new Experiment(1000,"DDDDDDDDDDDDDDDDDDDD");
        System.out.println("Average time of 20 byte: " + ex3.avgTime/1000000.0);
        
        Experiment ex4 = new Experiment(1000,"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD");
        System.out.println("Average time of 40 byte: " + ex4.avgTime/1000000.0);
        
        Experiment ex5 = new Experiment(1000,"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD");
        System.out.println("Average time of 80 byte: " + ex5.avgTime/1000000.0);
        
       
        Experiment ex6 = new Experiment(1000,"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD");
        System.out.println("Average time of 160 byte: " + ex6.avgTime/1000000.0);
        
        Experiment ex7 = new Experiment(1000,"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD");
        System.out.println("Average time of 200 byte: " + ex7.avgTime/1000000.0);
        
       
        
        
        
    
    }
    
}
