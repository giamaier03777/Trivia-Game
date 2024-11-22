import socket
import threading
import time
import json
import random


class TriviaServer:
    def __init__(self, host='0.0.0.0', port=12345, question_file='questions.json'):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.questions = self.load_questions(question_file)
        print("Server started and waiting for connections...")

    def load_questions(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle_client(self, client_socket, client_address):
        print(f"Connected with {client_address}")
        score = 0

        selected_questions = random.sample(self.questions, 5)

        for q in selected_questions:
            print(f"Sending question: {q['question']}")
            client_socket.sendall((q["question"] + "\n").encode())
            print("Question sent, awaiting response...")

            try:
                response = client_socket.recv(1024).decode().strip()
                print(f"Response received: {response}")
                if response.lower() == q["answer"].lower():
                    score += 1
                    client_socket.sendall("Correct!\n".encode())
                else:
                    client_socket.sendall("Incorrect!\n".encode())
            except socket.error as e:
                print(f"Error receiving response: {e}")
                break

            time.sleep(1)

        client_socket.sendall(f"Final score: {score} out of 5\n".encode())
        client_socket.close()
        print(f"Connection with {client_address} has been closed")

    def run(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()


if __name__ == "__main__":
    server = TriviaServer()
    server.run()
