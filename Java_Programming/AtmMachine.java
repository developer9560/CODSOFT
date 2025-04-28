import java.util.Scanner;

class ATM{
    private float balance = 0.0f;
    private int pin;
    public ATM(){
        System.out.println("Welcome to ATM Machine!");
        System.out.println("Create YOur Pin:");
        Scanner sc = new Scanner(System.in);
        this.pin = sc.nextInt();
        System.out.println("Pin Created Successfully!");
    }

    boolean validatePin(){
        System.out.println("Enter Your Pin:");
        Scanner sc = new Scanner(System.in);
        int pin = sc.nextInt();
        if(this.pin == pin){
            return true;
        }else{
            System.out.println("Invalid Pin!");
            return false;
        }
    }

    void checkBalance(){
        if(validatePin()){
            System.out.println("Your Current Balance is: " + balance);
        }
    }


    void deposit(){
        if(validatePin()){
            System.out.println("Enter Amount to Deposit:");
            Scanner sc = new Scanner(System.in);
            float amount = sc.nextFloat();
            balance += amount;
            System.out.println("Amount Deposited Successfully! , current balance is: " + balance);
            
        }
    }

    void withdraw(){
        if(validatePin()){
            System.out.println("Enter Amount to Withdraw:");
            Scanner sc = new Scanner(System.in);
            float amount = sc.nextFloat();
            if(amount > balance){
                System.out.println("Insufficient Balance!");
            }else{
                balance -= amount;
                System.out.println("Amount Withdrawn Successfully! , current balance is: " + balance);
            }
        }
    }
    void changePin(){
        if(validatePin()){
            System.out.println("Enter New Pin:");
            Scanner sc = new Scanner(System.in);
            int newPin = sc.nextInt();
            this.pin = newPin;
            System.out.println("Pin Changed Successfully!");
        }
    }

    void exit(){
        System.out.println("Thank You for Using ATM Machine!");
        System.exit(0);
    }

    void menu(){
        while (true) {
        System.out.println("\n1. Check Balance");
        System.out.println("2. Deposit");
        System.out.println("3. Withdraw");
        System.out.println("4. Change Pin");
        System.out.println("5. Exit");
        System.out.println("\nEnter Your Choice:");
        Scanner sc = new Scanner(System.in);
        int choice = sc.nextInt();
        
            switch (choice) {
                case 1:
                    checkBalance();
                    break;
                case 2:
                    deposit();
                    break;
                case 3:
                    withdraw();
                    break;
                case 4:
                    changePin();
                    break;
                case 5:
                    exit();
                    break;
                default:
                    System.out.println("Invalid Choice! Please try again.");
            }
        }
    }
}

public class AtmMachine{

    public static void main(String[] args){
        ATM atm = new ATM();
        // atm.menu();
    }
}
   