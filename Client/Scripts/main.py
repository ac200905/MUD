import socket
import random

if __name__ == '__main__':
    running = True
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.connect(("127.0.0.1", 8222))

    next_option_1 = "What shall you do now? : "
    next_option_2 = "What will you do next? : "
    next_option_3 = "What action do you take next? : "
    list_next_option = [next_option_1, next_option_2, next_option_3]

    while running:

        input_string = input(random.choice(list_next_option))

        my_socket.send(input_string.encode())

        data = my_socket.recv(4096)
        print(data.decode("utf-8"))
