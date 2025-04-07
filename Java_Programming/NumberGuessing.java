import java.util.Random;
import java.util.Scanner;

public class NumberGuessing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();
        int MaxRound = 5;
        int TotalScore = 0;
        System.out.println("===== Welcome to The Number Guessing Game !=====");

        for(int round = 1; round <= MaxRound ; round++){
            int numberToGuess = random.nextInt(100)+1;
            int TotalAttempet = 7;
            boolean correct = false;

            System.out.println("\n Round "+ round);
            System.out.println("Guess the number between 1 and 100, you have :"+ TotalAttempet);

            while(TotalAttempet>0){
                System.out.println("Enter you Guess: ");
                int userGuess = sc.nextInt();

                if(userGuess==numberToGuess){
                    System.out.println("You Guess the Correct Number ! ");
                    correct = true;
                    TotalScore+=10;
                    break;

                }else if( userGuess>numberToGuess ){
                    System.out.println("Too High!");

                }else{
                    System.out.println("Too Low!");
                }

                TotalAttempet--;
                System.out.println("total Attempts are left :"+ TotalAttempet);
            }

            if (!correct) {
                System.out.println("Sorry! The correct number was: " + numberToGuess);
            }
            System.out.println("Do you want to Play Next Round (yes)/(no): ");
            sc.nextLine();
            String response = sc.nextLine();
            if(!response.equalsIgnoreCase("yes")){
                break;
            }
        }

        System.out.println("====Game Over=====");
        System.out.println("Your Totol Score is :" + TotalScore);
        System.out.println("Thanks for Playing");

    }
}
