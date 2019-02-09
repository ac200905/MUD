import socket
import random
from time import sleep

def main():


    running = True
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.connect(("127.0.0.1", 8222))

    connected = True
    print("Connection to Server established.")



    while running:

        try:
            send_data(my_socket)
            receive_data(my_socket)

        except socket.error:
            print("Server connection lost. Attempting reconnection...")
            connected = False


            while not connected:
                try:
                    #connect_to_server()
                    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    my_socket.connect(("127.0.0.1", 8222))
                    print("Re-established connection to Server.")

                    connected = True


                except socket.error:
                    print("Trying to connect...")
                    sleep(2)


            #input_string = input(random.choice(list_next_option))

            #my_socket.send(input_string.encode())

            #data = my_socket.recv(4096)
            #print(data.decode("utf-8"))





def send_data(my_socket):
    next_option_1 = "What shall you do now? : "
    next_option_2 = "What will you do next? : "
    next_option_3 = "What action do you take next? : "
    list_next_option = [next_option_1, next_option_2, next_option_3]

    input_string = input(random.choice(list_next_option))

    my_socket.send(input_string.encode())

def receive_data(my_socket):
    data = my_socket.recv(4096)
    print(data.decode("utf-8"))

def connect_to_server():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.connect(("127.0.0.1", 8222))
    print("Re-established connection to Server.")


if __name__ == '__main__':
    main()