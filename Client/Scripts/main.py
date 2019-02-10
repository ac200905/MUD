import socket
import random
from time import sleep

running = True

def main():


    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.connect(("127.0.0.1", 8222))


    print("Connection to Server established.\n")

    print(  "\n                               THE ELEVENTH HOUR\n" \
            "--------------------------------------------------------------------------------------------\n" \
            "You step through the bubble surrounding the small town, cut off from the rest of the world. \n" \
            "As you do, you find yourself standing in a bright white void. \n" \
            "An old woman stands in front of you holding a small Chalice. \n" \
            "She whispers, 'It's you. Find me.' \n" \
            "The woman disappears and you find yourself standing at the entrance into town. \n" \
            "--------------------------------------------------------------------------------------------\n")

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
    next_option_4 = "What's your next move? : "
    list_next_option = [next_option_1, next_option_2, next_option_3, next_option_4]

    input_string = input(random.choice(list_next_option))
    input_string = input_string.lower()

    if input_string == "quit" or input_string == "q" or input_string == "exit":
        global running
        running = False
        raise SystemExit
    else:
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