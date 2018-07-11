import textwrap

# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

commands = {
    "n s e w": "Use these directions to move.",
    "q or quit": "Quit the game.",
    "h or help": "Help!",
}

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "contents": [],
        "creatures": [],
        "description": "North of you, the cave mouth beckons.",
        "n_to": "cave entrance",
    },

    "cave entrance": {
        "name": "Cave Entrance",
        "contents": ["sword"],
        "creatures": [],
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "contents": [],
        "creatures": ["spider", "bird", "fox"],
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "cave entrance",
    },

    "narrow": {
        "name": "Narrow Passage",
        "contents": [],
        "creatures": [],
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w_to": "cave entrance",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "contents": ["treasure"],
        "creatures": [],
        "description": """You've found the long-lost treasure
chamber. The only exit is to the south.""",
        "s_to": "narrow",
    },

    "kittens": {
        "name": "Kitten Chamber",
        "contents": ["kittens"],
        "creatures": [],
        "description": """You've stumbled upon the fabulous KITTEN CHAMBER, where there is nothing but kittens as far as the eye can see.\n""",
        "s_to": "treasure",
    }

}

""" template room to copy into code
    "room": {
        "name": "",
        "contents": [],
        "creatures": [],
        "description": "",
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""

# Write a class to hold player information, e.g. what room they are in currently
class Player:
    def __init__(self, startRoom):
        self.curRoom = startRoom
        self.inventory = []

def tryDirection(d, curRoom):
    key = d + "_to"
    if key not in rooms[curRoom]:
        print:("You can't go that way!")
        return curRoom
    dest = rooms[curRoom][key]
    return dest

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player('outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

done = False

while not done:
    print("\n{}\n".format(rooms[p.curRoom]['name']))
    for line in textwrap.wrap(rooms[p.curRoom]['description']):
        print(line)
    if (rooms[p.curRoom]['contents'] != []):
        print("\nTHIS ROOM CONTAINS:")
        for item in rooms[p.curRoom]['contents']:
            print(item)
        print('\n')
    if(rooms[p.curRoom]['creatures'] != []):
        if(len(rooms[p.curRoom]['creatures']) == 1):
            print("There is a {} here.".format(rooms[p.curRoom]['creatures'][0]))
        if(len(rooms[p.curRoom]['creatures']) == 2):
            print("There is a {} and a {} here.".format(rooms[p.curRoom]['creatures'][0], rooms[p.curRoom]['creatures'][1]))
        else:
            print("You see the following creatures here:")
            for creature in rooms[p.curRoom]['creatures']:
                print(creature)

    
    if (p.curRoom == "kittens"):
        print("*You win the game!*\n")
        done = True
        break
    
    s = input("\nCommand> ").strip().lower()
    if (s == "q") or (s == "quit"):
        done = True
    elif (s == "h") or (s == "help"):
        print("LIST OF COMMANDS:")
        for command in commands:
            print(command, "\t", commands[command])
    elif (s[0:3] == "get"):
        if(s[4:12] == "treasure"):
            if ('treasure' in rooms[p.curRoom]['contents']):
                print("You got treasure!")
                rooms[p.curRoom]['contents'].remove('treasure')
                p.inventory.append('treasure')
                rooms['treasure']['n_to'] = "kittens"
                rooms['treasure']['description'] = """You've found the long-lost treasure chamber. A small doorway to the North catches your eye. That wasn't here before, was it?"""
            else:
                print("No treasure here, fool!")
        if(s[4:9] == "sword"):
            if('sword' in rooms[p.curRoom]['contents']):
                print("You have a sword now")
                rooms[p.curRoom]['contents'].remove('sword')
                p.inventory.append('sword')
            else:
                print("No swords here!")
    elif (s[0:4] == "kill"):
        if(s[5:11] == "spider"):
            if('spider' in rooms[p.curRoom]['creatures']):
                if('sword' in p.inventory):
                    print("Spider has been killed.")
                    rooms[p.curRoom]['creatures'].remove('spider')
                else:
                    print("With what?")
            else:
                print("No spider! Are you seeing things?")
    elif s in ["n", "s", "w", "e"]:
        p.curRoom = tryDirection(s, p.curRoom)
    else:
        print("Unknown command {}".format(s))