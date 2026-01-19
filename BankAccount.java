import java.util.ArrayList;
import java.util.List;

public class BankAccount {
    private String accountNumber;
    private String ownerName;
    private double balance;
    private List<String> transactionHistory;

    public BankAccount(String accountNumber, String ownerName) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = 0;
        this.transactionHistory = new ArrayList<>();
    }

    public void deposit(double amount) {
        balance += amount;
        transactionHistory.add("Deposited: $" + amount);
    }

    public void withdraw(double amount) {
        balance -= amount;
        transactionHistory.add("Withdrew: $" + amount);
    }

    public double getBalance() {
        return balance;
    }

    public void transfer(BankAccount targetAccount, double amount) {
        this.withdraw(amount);
        targetAccount.deposit(amount);
        transactionHistory.add("Transferred: $" + amount + " to " + targetAccount.accountNumber);
    }

    public void printTransactionHistory() {
        System.out.println("Transaction History for " + accountNumber);
        for (int i = 0; i < transactionHistory.size(); i++) {
            System.out.println(transactionHistory.get(i));
        }
    }

    public double calculateInterest(double rate, int years) {
        return balance * rate * years;
    }

    public static void main(String[] args) {
        BankAccount account1 = new BankAccount("123456", "Alice");
        BankAccount account2 = new BankAccount("789012", "Bob");

        account1.deposit(1000);
        account1.withdraw(200);
        account1.transfer(account2, 300);

        System.out.println("Account 1 Balance: $" + account1.getBalance());
        System.out.println("Account 2 Balance: $" + account2.getBalance());

        account1.printTransactionHistory();
    }
}
