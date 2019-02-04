from Scripts import player
from Scripts import dungeon
import socket
import time


class Game:

    def __init__(self):
        self.running = ''
        self.player = ''

        self.dungeon = ''

        self.exit_text = "Farewell Traveller..."

        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.my_socket.bind(("127.0.0.1", 8222))

        self.data = []

        self.seqID = 0

    def setup(self, dungeon_name):
        self.running = True

        self.player = player.Player("Player Name")
        self.dungeon = dungeon.Dungeon(dungeon_name, self.player)

        self.dungeon.setup_dungeon()

        self.player.setup(self.dungeon)

    def loop(self):

        self.my_socket.listen(5)

        client = self.my_socket.accept()
        # Print the dungeon description at beginning of game
        self.player.input.output = self.dungeon.dungeon_description

        while self.running:
            # If "quit_game" returned then close application
            if self.player.input.output == "quit_game":
                print(self.exit_text)
                self.running = False

            # The data received from client
            self.data = client[0].recv(4096)

            self.player.input.handle_input(user_input=self.data.decode("utf-8"))

            test_string = self.player.input.output

            client[0].send(test_string.encode())







