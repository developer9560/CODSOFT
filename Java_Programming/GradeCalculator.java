import java.util.Scanner;

public class GradeCalculator {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of subjects: ");
        int numSubjects = sc.nextInt();

        int marks[] = new int[numSubjects];
        int totalMarks = 0;

        for (int i = 0; i < numSubjects; i++) {
            System.out.println("Enter marks for subject " + (i + 1) + " out of 100 : ");
            marks[i] = sc.nextInt();

            if (marks[i] < 0 || marks[i] > 100) {
                System.out.println("Invalid marks entered. Please enter marks between 0 and 100.");
                i--;
                continue;
            }

            totalMarks += marks[i];
        }

        double average = (double) totalMarks / numSubjects;
        char Grade;

        if (average > 90) {
            Grade = 'A';
        } else if (average >= 75) {
            Grade = 'B';
        } else if (average >= 60) {
            Grade = 'C';
        } else if (average >= 50) {
            Grade = 'D';
        } else if (average > 34) {
            Grade = 'E';
        } else {
            Grade = 'F';
        }

        System.out.println("\n======Results======");
        System.out.println("Total marks out of " + (numSubjects * 100) + " : " + totalMarks);
        System.out.println("Average marks : " + average);
        System.out.println("Grade : " + Grade);

    }
}
