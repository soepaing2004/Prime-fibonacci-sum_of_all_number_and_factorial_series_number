package project;

import java.util.Scanner;

public class Finding_number_project {
    static Scanner s=new Scanner(System.in);

    static void fibonacci_number(){
        System.out.println("Enter a number you want his fibonacci serial number:");
        int fibonacci_serial=s.nextInt();
        int num1=0,num2=1,num3=0;
        for (int i=0;i<fibonacci_serial;i++){
            System.out.println(num1);
            num3=num1+num2;
            num1=num2;
            num2=num3;
        }
    }
    static void factorial_number(){
        System.out.println("Enter a number that you want his factorial series:");
        int factorial=s.nextInt();
        int number1=1;
        for (int i=2;i<=factorial;i++){
            number1=number1*i;
            System.out.println(number1);
        }
    }
    static void prime_number(){
        System.out.println("Enter a number that you want to check that's a prime number or not:");
        int prime=s.nextInt();
        int prime_unknown_number=0;
        if (prime==1){
            System.out.println(prime+" is not a prime number.");
        } else if (prime>1) {
            for (int i=2;i<prime;i++){
                if (prime%i==0){
                    prime_unknown_number=+1;
                    break;
                }
            }
            if (prime_unknown_number==1){
                System.out.println(prime+" is not a prime number.");
            }else {
                System.out.println(prime+" is a prime number.");
            }
        }

    }
    static void sum_all_number(){
        System.out.println("Enter a number you want his sum fom 0 to your input number:");
        int sum_number=s.nextInt();
        int unknown_number=0;
        for (int i=1;i<=sum_number;i++){
            unknown_number=unknown_number+i;
            System.out.println(unknown_number);

        }
    }
    public static void main(String[] args) {
        System.out.println("This is a program that is calculate the fibonacci number,factorial number,prime number and the sum of the all number from 1 to your input");
        System.out.println("Choice an option:");
        String user_input=s.next();
        switch (user_input){
            case "fibonacci":
                Finding_number_project.fibonacci_number();break;
            case "factorial":
                Finding_number_project.factorial_number();break;
            case "prime":
                Finding_number_project.prime_number();break;
            case "sum":
                Finding_number_project.sum_all_number();break;
            case "end":
                System.out.println("End the program");break;
            default:
                System.out.println("There's no operation that you enter.");break;
        }
    }
}
