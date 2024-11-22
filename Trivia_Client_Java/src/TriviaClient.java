import java.io.*;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class TriviaClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 12345;

        try (Socket socket = new Socket(host, port);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
             BufferedWriter out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8));
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("Connected to server, waiting for questions...");

            String question;
            while ((question = in.readLine()) != null) {

                if (question.startsWith("Final score:")) {
                    System.out.println(question);
                    System.out.println("Game over. " + question);
                    break;
                }

                System.out.println("Question: " + question);

                System.out.print("Your answer: ");
                String answer = scanner.nextLine();
                out.write(answer + "\n");
                out.flush();

                String feedback = in.readLine();
                if (feedback != null) {
                    System.out.println(feedback);
                } else {
                    break;
                }
            }

            System.out.println("Connection to server has been closed.");

        } catch (IOException e) {
            System.out.println("Connection to server failed: " + e.getMessage());
        }
    }
}
