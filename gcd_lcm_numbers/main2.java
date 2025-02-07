import java.util.Scanner;

public class Main {

    public long GCD(long a, long b) {
        while (a > 0 && b > 0) {
            if (a > b) {
                a = a % b;
            } else {
                b = b % a;
            }
        }
        return Math.max(a, b);
    }

    public long LCM(long a, long b, long GCD) {
        return (a * b) / GCD;
    }

    public static void main(String[] args) {
        Main mainInstance = new Main();
        Scanner reader = new Scanner(System.in);
        long numberA = reader.nextLong();
        long numberB = reader.nextLong();
        System.out.println(mainInstance.LCM(numberA, numberB, mainInstance.GCD(numberA, numberB)));
    }
}