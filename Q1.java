import java.util.Scanner;

public class Q1 {
    public static char question1(String arr[], int n) {
        char firstch[] = new char[100];
        for (int i = 0; i < n; i++) {
            firstch[i] = arr[i].charAt(0);
        }
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (firstch[i] > firstch[j]) {
                    char temp;
                    temp = firstch[i];
                    firstch[i] = firstch[i + 1];
                    firstch[i + 1] = temp;
                }
            }
        }
        int count = 0, temp = 0, key = 0;
        for (int i = 0; i < n; i++) {
            if (firstch[i] == firstch[i + 1]) {
                temp = temp + 1;
            } else if (firstch[i] != firstch[i + 1]) {
                temp = 0;
            }
            if (temp > count) {
                count = temp;
                key = i;
            }
        }
        return firstch[key];
    }

    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);
        System.out.println("enter the number of strings");
        int n = scn.nextInt();
        String arr[] = new String[100];
        for (int i = 0; i < n; i++) {
            System.out.println("enter the string");
            arr[i] = scn.next();
        }
        char c = question1(arr, n);
        System.out.println("the most repeated character is " + c);

    }
}
