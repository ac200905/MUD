
class Room:

    def __init__(self, name, description, look_description, north="", south="", east="", west=""):
        self.name = name
        self.description = description
        self.look_description = look_description

        # Create a dictionary with up to four connections
        self.connections = dict()
        # Each direction key can be assigned a room name key that
        # can be accessed in order to change rooms later
        self.connections["north"] = north
        self.connections["south"] = south
        self.connections["east"] = east
        self.connections["west"] = west


class DungeonRooms:

    def __init__(self):
        # Create a basic dungeon using the Room Class
        self.room_1 = Room("Entry Gate", "You stand at the entrance to town...\n",
                           "\nYou are at the Entry Gate.\n"
                           "You see a street to the north.\n",
                           north="Main Street South",
                           south="",
                           east="",
                           west="")

        self.room_2 = Room("Clock Tower", "You marvel at the giant clock above you...\n",
                           "\nYou are at the Clock Tower.\n"
                           "You see a Tavern north of you.\n"
                           "There is a street to the east.\n",
                           north="The Smiling Goat",
                           south="",
                           east="Main Street South",
                           west="")

        self.room_3 = Room("Main Street South", "You stand at the south end of a busy street...\n",
                           "\nYou are at the Southern Street.\n"
                           "There is a street north of you. \n"
                           "You see the Entry Gate south of you. \n"
                           "There is a Large Well to the east. \n"
                           "There is a Clock Tower west. \n",
                           north="Main Street North",
                           south="Entry Gate",
                           east="Large Well",
                           west="Clock Tower")

        self.room_4 = Room("Large Well", "You gaze into the deepest, darkest well you have ever seen...\n",
                           "\nYou are at the Large Well.\n"
                           "You see a Bank to the north of you. \n"
                           "There is a street to the west. \n",
                           north="Bank",
                           south="",
                           east="",
                           west="Main Street South")

        self.room_5 = Room("The Smiling Goat", "You enter a dingy tavern full of drunkards...\n",
                           "\nYou are at the Tavern, 'The Smiling Goat'.\n"
                           "There is the giant Clock Tower south of you. \n"
                           "You see a street to the east. \n",
                           north="",
                           south="Clock Tower",
                           east="Main Street North",
                           west="")

        self.room_6 = Room("Main Street North", "You stand at the north end of a long street...\n",
                           "\nYou are at the Northern Street.\n"
                           "You see a Bank to the east of you. \n"
                           "There is a street south of you. \n"
                           "You can see a crumbling Temple to the north. \n"
                           "There is a cheerless Tavern to the west. \n",
                           north="Fallen Temple",
                           south="Main Street South",
                           east="Bank",
                           west="The Smiling Goat")

        self.room_7 = Room("Bank", "You enter a small Bank...\n",
                           "\nYou are at the Bank.\n"
                           "You see a Large Well to the south. \n"
                           "There is a street to the west. \n",
                           north="",
                           south="Large Well",
                           east="",
                           west="Main Street North")

        self.room_8 = Room("Fallen Temple", "You see a large Temple that's seen better days...\n",
                           "\nYou are at the Fallen Temple.\n"
                           "You see a street just south of your position. \n",
                           north="",
                           south="Main Street North",
                           east="",
                           west="")

