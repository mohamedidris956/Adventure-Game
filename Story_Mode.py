
# Description: An adventure game where players can choose to play either detective or murderer,
# each with a unique storyline. Players interact
# with various characters and collect clues to advance the plot. The game utilises OOP principles,
# featuring classes for characters, rooms, and crime scenes. It showcases encapsulation, inheritance, polymorphism,
# and abstraction, creating an engaging and interactive gaming experience




from abc import ABC, abstractmethod

# Abstract base class for different characters in the game
class Character(ABC):
    """In this solution, the Character class has been transformed into an
    abstract class by using the ABC class.
    An abstract method named perform_action has been declared in the
    Character class. The Suspect and Witness subclasses then implement this
    abstract method with specific actions that demonstrate polymorphism. """

    # Construct initialising name, dialogue, and interacted status
    def __init__(self, name, dialogue):
        # Even in abstract classes we see encapsulation  as before.
        self._name = name
        self._dialogue = dialogue
        self._interacted = False

    @abstractmethod  # Declares an abstract method using a decorator.
    def perform_action(self):
        pass  # Abstract methods never contain any actual logic. The
        # transfer statement "pass" allows for this.

    # An abstract class must contain at least one abstract method.
    # However, "normal" methods may also be contained.
    # Method to handle interaction with the character
    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"{self._name} is no longer interested in talking."

        return interaction

# Subclass of Character representing a BarMan
class BarMan(Character):
    def __init__(self, name, dialogue):
        super().__init__(name, dialogue)

    # Method to return the name barman
    def get_name(self):
        return self._name

    # Overrides interact method to include a print statement
    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"{self._name} is no longer interested in talking."

        print(interaction)

    # Implementation of the performance_action abstract method
    def perform_action(self):
        print(f"Bar Man {self._name} is busy serving drinks.")

# Subclass of Character representing Boyfriend
class Boyfriend(Character):
    def __init__(self, name, dialogue):
        super().__init__(name, dialogue)

    def get_name(self):
        return self._name

    def re_interact(self):
        self._interacted = False

    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"{self._name} is no longer interested in talking."

        print(interaction)

    def perform_action(self):
        print (f"{self._name} is anxiously waiting for updates on the situation.")

# Subclass of Character representing Ex-Best friend
class ExBestFriend(Character):

    def __init__(self, name, dialogue):
        super().__init__(name, dialogue)

    def get_name(self):
        return self._name

    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"{self._name} is no longer interested in talking."

        print(interaction)

    def perform_action(self):

        print( f"{self._name} is trying to recall the last time they saw the victim.")


# Subclass of Character representing Receptionist
class Receptionist(Character):

    def __init__(self, name, dialogue):
        super().__init__(name, dialogue)

    def get_name(self):
        return self._name

    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"{self._name} is no longer interested in talking."

        print(interaction)

    def perform_action(self):
        print (f"Hotel Receptionist {self._name} is busy handling guests at the lodge entrance.")


# Definition of a Clue Class
class Clue:

    # Construct initialising name and description of a clue
    def __init__(self, name, description):
        self.name = name
        self.description = description


# Definition of a Tool Class
class Tool:

    # Constructor initialising name, description, and found status of the tool
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.found = False

    # Method to set the tool as found
    def add_tool(self):
        self.found = True


# Definition of a Room Class
class Room:

    # Construct initialising name, description, and examined status
    def __init__(self, name, description):
        self._examined = False
        self.name = name
        self.description = description

    # Method to set the room as examined
    def examine(self):
        self._examined = True

    # Method to check if the room has been examined
    def examined(self):
        return self._examined

    def not_examined(self):
        self._examined = False


# Main Class for the Game
class Game:

    # Constructor initialising game states and attributes
    def __init__(self):

        # Initialising various attributes related to game state
        self.__running = True  # Indicates if the game is running
        self.__game_started = False  # Flag to check if the game has started
        self.__characters_interacted = False  # Ensures there is no double interactions
        self.__room_examined = False  # Flag for room examination status
        self.__game_choice = ""  # Detective = 1 Murderer = 2
        self.__tool_found = False
        self.__name = ""  # Players character name
        self.__role = ""  # Player's role in the game
        self.__bar_man = None
        self.__boyfriend = None
        self.__ex_bestfriend = None
        self.__receptionist = None
        self.__girlfriend = None
        self.__safe_opened = False
        self.__caught = 3  # Counter for the player being caught
        self.__valerie_dead = False  # Flag to check if the Valerie is dead
        self.__valerie_choked = False
        self.__flashlight = False
        self.__berry2 = False

        # List to store clues that have been examined
        self.__examined_clues = []
        # List to store tools that have been found
        self.__examined_tools = []

        # Mapping locations to tools available in those locations
        self.__lodge_rooms_tools = {

            # TOOLS FOR LODGE
            "Lonely Lodge": {
                # Mapping room numbers to Tool objects
                5: Tool("Kitchen knife","A perfect weapon for murdering"),
                4: Tool("Flashlight","Can be used in dark places"),
                3: Tool("Poisonous berry","Can be used to spike drinks"),
                0: Tool("Car keys","Keys to a strangers car")
            },
        }

        # Mapping locations to clues available in those locations
        self.__lodge_rooms_clues = {
            # CLUES FOR LODGE
            "Lonely Lodge": {
                # Mapping room numbers to Clue objects
                1: Clue("Dead body of Valerie(Girlfriend)","Found in the Porta Potty with visible stab wounds."),
                2: Clue("Bracelet","Found on the Bar floor with a 4 digit number with 1 number illegible 22*4. "
                                   "Maybe John(Boyfriend) could know about it?"),
                3: Clue("Number of Footprints","Found in the woods leading back to the lodge."),
                5: Clue("Safe","Found in the Couple's Room, examine the room again to enter 4 digit code."),
                6: Clue("Bloody Knife","Found in the couple's room inside a safe.")
            },
        }

        # List of Room objects for the Lonely Lodge
        self.__lodge_rooms = [
            # 0
            Room("Slippery Slope", "The party takes place here."),
            # 1
            Room("Porta-Potty", "A Tightly confined cubicle."),
            # 2
            Room("Bar", "An old fashioned Bar."),
            # 3
            Room("Woods", "Dark and mysterious."),
            # 4
            Room("Lonely Lodge", "A cosy and warm welcoming lodge."),
            # 5
            Room("The Couple's Room", "A nice spacious room.")

            ]

    # Method to start running the Game
    def run(self):

        # Implementation for starting the game
        self.__game_started = False

        # Welcome message and game setup
        print("Welcome to 'Name of Game'")
        print("You are about to embark on a thrilling adventure as a Detective or Murderer.")
        print("Both Choices will lead you down a different path")
        print("So Choose Wisely...")
        self.__game_choice = input("Press '1' to choose Detective or '2' for Murderer:")

        # INITIALISING

        # DETECTIVE CHARACTERS
        if self.__game_choice == "1":
            self.__role = "Detective"
            self.__bar_man = BarMan("Ned(Bartender)", "He saw Valerie(Girlfriend) kissing another guy")
            self.__boyfriend = Boyfriend("John(Boyfriend)", "I can't believe she's missing.")
            self.__ex_bestfriend = ExBestFriend("Samantha(Ex Best Friend)", "I seen her drop her bracelet at the bar")
            self.__receptionist = Receptionist("Linda(Receptionist)","She didn't notice anything suspicious"
                                                                     " around the time of the murder.")
        # MURDERER TOOLS AND ROOMS
        # This needs to be done to achieve re-playability
        elif self.__game_choice == "2":
            self.__role = "Murderer"
        self.__lodge_rooms[0].not_examined()
        self.__lodge_rooms[1].not_examined()
        self.__lodge_rooms[2].not_examined()
        self.__lodge_rooms[3].not_examined()
        self.__lodge_rooms[4].not_examined()
        self.__lodge_rooms[5].not_examined()

        self.__safe_opened = False
        self.__caught = 3  # Counter for the player being caught
        self.__valerie_dead = False  # Flag to check if the Valerie is dead
        self.__valerie_choked = False
        self.__flashlight = False
        self.__berry2 = False

        # List to store clues that have been examined
        self.__examined_clues = []
        # List to store tools that have been examined
        self.__examined_tools = []

        # Initialise Tools
        knife = self.__lodge_rooms_tools["Lonely Lodge"].get(5)
        flashlight = self.__lodge_rooms_tools["Lonely Lodge"].get(4)
        berry = self.__lodge_rooms_tools["Lonely Lodge"].get(3)
        car_keys = self.__lodge_rooms_tools["Lonely Lodge"].get(0)
        knife.found = False
        flashlight.found = False
        berry.found = False
        car_keys.found = False

        # Enter the players name
        player_name = input(f"Enter your {self.__role}'s name: ")
        self.__name = player_name
        self.main_menu()

    # Method to display the Main Menu
    def main_menu(self):

        print("\n- - Main Menu - -\n")
        if not self.__game_started:
            player_input = input("Press 'q' to quit or 's' to start: ")
            if player_input.lower() == "q":
                self.__running = False
            elif player_input.lower() == "s":
                self.__game_started = True
                self.start_game()

        else:

            print("Game Info: ")
            print("- Role - ", self.__role)
            print("- Name -", self.__name)
            print("- Location - Lonely Lodge")
            print("- Current room -", self.__lodge_rooms[self.current_room].name)
            print("- Room Description -",self.__lodge_rooms[self.current_room].description)

    # DETECTIVE
        if self.__game_choice == "1":

            player_input = input("Press 'q' to quit, 'c' to continue, 'r' to review clues or 'n' for new game: ")

            if player_input.lower() == "q":
                self.__running = False

            elif player_input.lower() == "c":
                    self.continue_game()

            elif player_input.lower() == "r":
                self.review_clues()

            elif player_input.lower() == "n":
                self.run()

    # MURDERER
        if self.__game_choice == "2":
            player_input = input("Press 'q' to quit, 'c' to continue, or 'n' for new game: ")

            if player_input.lower() == "q":
                self.__running = False

            elif player_input.lower() == "c":
                self.continue_game()

            elif player_input.lower() == "n":
                self.run()

    # Method to handle game updates based on players choices
    def update(self):

            if self.__game_choice == "1":
                player_input = input(
                    "\nPress 'q' to quit to menu, 'i' to interact, "
                    "'e' to examine, 'r' to review clues 'm' to move room or 'a' to arrest someone:")

                if player_input.lower() == "q":
                    self.main_menu()

                elif player_input.lower() == "i":
                    self.interact_with_characters()

                elif player_input.lower() == "e":
                    self.examine_room()

                elif player_input.lower() == "r":
                    self.review_clues()

                elif player_input.lower() == "m":
                    self.move_to_room()

                elif player_input.lower() == "a":
                    self.arrest()
                else:
                    print("Invalid choice.")
                    self.update()

            elif self.__game_choice == "2":
                player_input = input(
                    "\nPress 'q' to quit to menu,"
                    "'e' to examine room, 'u' to use tool,'f' to move forward or 'b to go back:")
                if player_input.lower() == "q":
                    self.main_menu()

                elif player_input.lower() == "e":
                    self.examine_room()

                elif player_input.lower() == "u":
                    self.use_tool()

                elif player_input.lower() == "f":
                    self.move_forward()

                elif player_input.lower() == "b":
                    self.move_back()

                else:
                    print("Invalid choice.")
                    self.update()

    # Method to start the game
    def start_game(self):
        if self.__game_choice == "1":
            print(f"Welcome {self.__role} {self.__name} to the Lonely Lodge")
            self.current_room = 0  # Starting room
            print(f"You Enter {self.__lodge_rooms[self.current_room].name}."
                  f" {self.__lodge_rooms[self.current_room].description}")
            print("Your goal as Detective is to find clues and interact with people to solve the mystery, Good Luck..")
            self.update()

        elif self.__game_choice == "2":
            print(f"Welcome {self.__role} {self.__name} to the Lonely Lodge")
            self.current_room = 5  # Starting room
            print(f"You Enter {self.__lodge_rooms[self.current_room].name}."
                  f" {self.__lodge_rooms[self.current_room].description}")
            print("Your goal as Murderer is to kill your girlfriend named Valerie without getting caught")
            print("She has just left your room to go to a party down the road.")
            print("Use tools that you find to navigate rooms and to kill Valerie, Good luck..")
            self.update()

    # Method to allow the detective to move to any room
    def move_to_room(self):
        print("You decide to move to a different room.")
        print("Available rooms:")

        # Enumerate through each room in the lodge, starting from index 1
        for i, room in enumerate(self.__lodge_rooms, start=1):
            # Print the room number and name
            print(f"{i}. {room.name}")

        # Take user input for the room choice
        room_choice = int(input("Enter the number of the room you want to move to: "))

        # Check if the user input is a valid room number
        if 0 < room_choice <= len(self.__lodge_rooms):
            # Adjust for 0-based indexing and set the current room
            self.current_room = room_choice - 1
            # Print information about the chosen room
            print(f"You enter the {self.__lodge_rooms[self.current_room].name}. "
                  f"Description: {self.__lodge_rooms[self.current_room].description}")

        else:
            print("Invalid room choice.")

        if self.current_room == 0:
            self.__boyfriend.perform_action()
            self.__ex_bestfriend.perform_action()

        elif self.current_room == 2:
            self.__bar_man.perform_action()

        elif self.current_room == 4:
            self.__receptionist.perform_action()

        self.update()

    # Method for interacting with characters
    def interact_with_characters(self):

        print("You decide to interact with the characters in the room.")

        if self.current_room == 0:  # Slippery Slope room
            print("Characters in room:")
            print(f"1.{self.__boyfriend.get_name()}")
            print(f"2.{self.__ex_bestfriend.get_name()}")
            selection = input("Please enter a number to select a character to interact with:")
            if selection == "1":
                self.__boyfriend.interact()
            elif selection == "2":
                self.__ex_bestfriend.interact()
            else:
                print("invalid option")

        elif self.current_room == 2: # Bar Room
            print("Characters in room:")
            print(f"1.{self.__bar_man.get_name()}")
            selection = input("Please enter a number to select a character to interact with:")
            if selection == "1":
                self.__bar_man.interact()
            else:
                print("invalid option")

        elif self.current_room == 4: # Lonely Lodge Entrance
            print("Characters in room:")
            print(f"1.{self.__receptionist.get_name()}")
            selection = input("Please enter a number to select a character to interact with:")
            if selection == "1":
                self.__receptionist.interact()
            else:
                print("invalid option")

        elif self.current_room == 1 or 3 or 5: # The Woods or the couples room

            print("No Characters to interact with")

        self.update()

    def examine_room (self):
        if self.__lodge_rooms[self.current_room].examined():
            if self.current_room == 5 and self.__safe_opened == False and self.__game_choice == "1":
                safe_choice = input("Do you want to enter the code for the safe? Yes/No:")

                if safe_choice.lower() == "yes":
                    code = input("Please enter a 4 digit code:")

                    if code == "2204":
                        clue = self.__lodge_rooms_clues["Lonely Lodge"].get(6)
                        print("You opened the safe")
                        print(f"You found a {clue.name}")
                        self.__examined_clues.append(clue)
                        self.__safe_opened = True
                        self.update()

                elif safe_choice.lower() == "no":
                    self.update()

                else:
                    print("Invalid Input")
                    self.update()
            if self.__game_choice == "1":
                print("You have already examined this room, review your clues")

            elif self.__game_choice == "2":
                print("You have already examined this room")

        else:
            print("You Examine the Room")

            # DETECTIVE
            if self.__game_choice == "1":
                clue = self.__lodge_rooms_clues["Lonely Lodge"].get(self.current_room)

                if clue:

                    if self.current_room == 2:
                        self.__boyfriend = Boyfriend("John(Boyfriend)", "I gave the bracelet to Valerie as an"
                                                                        " anniversy gift\n for when we met on the 22nd of April")
                        self.__boyfriend.re_interact()
                    print(f"You found a {clue.name}")
                    self.__examined_clues.append(clue)
                    self.__lodge_rooms[self.current_room].examine()

                else:
                    print("You find nothing in this room.")

                # MURDERER
            elif self.__game_choice == "2":
                tool = self.__lodge_rooms_tools["Lonely Lodge"].get(self.current_room)
                flashlight = self.__lodge_rooms_tools["Lonely Lodge"].get(4)

                if tool:
                    print(f"You found a {tool.name}")
                    self.__examined_tools.append(tool)
                    tool.add_tool()
                    self.__lodge_rooms[self.current_room].examine()

        self.update()

    def move_forward(self):

        knife = self.__lodge_rooms_tools["Lonely Lodge"].get(5)
        flashlight = self.__lodge_rooms_tools["Lonely Lodge"].get(4)
        berry = self.__lodge_rooms_tools["Lonely Lodge"].get(3)
        car_keys = self.__lodge_rooms_tools["Lonely Lodge"].get(0)

        if self.current_room == 5 and not knife.found:
            print("You need to find a weapon before continuing")
            self.update()

        elif self.current_room == 3 and not self.__flashlight:
            print("The woods are too dark to navigate,you need to use a flashlight")
            self.update()


        if self.current_room == 0:
            print("You cannot move forward a room")

        else:

            if self.current_room == 2 and not (self.__valerie_dead or self.__valerie_choked):
                print("You decide to wait for Valerie, maybe you can use one of your tools while she is gone")
                self.update()

            elif self.current_room == 2 and (self.__valerie_dead or self.__valerie_choked):
                self.current_room -= 1

            # Decrement the current room
            self.current_room -= 1
            print(f"You enter the {self.__lodge_rooms[self.current_room].name}. "
                  f"Description:{self.__lodge_rooms[self.current_room].description}")

            if self.current_room == 3 and not flashlight.found:
                # Allows for the flashlight to either be in tool slot 2 or 3
                self.__berry2 = True

            elif self.current_room == 3 and flashlight.found:
                self.__berry2 = False

            if self.current_room == 2:
                print("You see Valerie Kiss another guy, You get really angry")
                print("She then walks away to use the bathroom.")
                val_choice = input("Do you want to pursue her? Yes/No:")

                # Pursue Valerie to the next room
                if val_choice.lower() == "yes":
                    self.current_room -=1
                    print(f"You enter the {self.__lodge_rooms[self.current_room].name}. "
                          f"Description:{self.__lodge_rooms[self.current_room].description}")
                    print("Valerie is shocked to see you as you enter the Porta Potty behind her")
                    self.use_tool()

                # You stay in the bar
                else:
                    print("You decide not to pursue Valerie")

            elif self.current_room == 0:
                print("You must now escape using one of your tools.")

        self.update()

    def move_back(self):
        # Checks if Valerie is dead and removes catching feature
        if self.__valerie_dead or self.__valerie_choked:
            self.__caught = -1
        # if you move back 3 times you get caught
        elif self.__caught == 0:
            self.caught()

        elif not self.__valerie_dead or not self.__valerie_choked:
            # Print how many times you can move back before being caught
            print(f"You can move back {self.__caught - 1} times before getting caught")

        if self.current_room == 5:
            # Doesn't allow user to go beyond the length of the array of rooms
            print("You cannot move back a room")
            self.update()

        elif self.current_room == 0 and (self.__valerie_dead or self.__valerie_choked):
            print(f"You enter the {self.__lodge_rooms[self.current_room].name}. "
                  f"Description:{self.__lodge_rooms[self.current_room].description}")
            self.caught()
        elif self.current_room == 5 and (self.__valerie_dead or self.__valerie_choked):
            self.escape()


        else:
            if not self.__valerie_dead or not self.__valerie_choked:
                # If valerie isn't dead decrement the caught variable
                self.__caught -= 1

            # Increment the current room
            self.current_room += 1
            print(f"You enter the {self.__lodge_rooms[self.current_room].name}. "
                  f"Description:{self.__lodge_rooms[self.current_room].description}")
            if self.current_room == 5 and (self.__valerie_dead or self.__valerie_choked):
                self.__running = False
                self.escape()
            self.update()

    # Method for using murderers tools
    def use_tool(self):
        car_keys = self.__lodge_rooms_tools["Lonely Lodge"].get(0)
        berry = self.__lodge_rooms_tools["Lonely Lodge"].get(3)
        if self.__examined_tools:
            for i, tool in enumerate(self.__examined_tools, start=1):
                print(f"{i}. {tool.name}: {tool.description}")

            tool_choice = input("\nSelect the tool you would like to use:")
            if self.current_room == 1:
                if tool_choice == "1" and not self.__valerie_dead:
                    print("You stab Valerie Multiple times now you must escape")
                    self.__valerie_dead = True

                else:
                    print("You have no tools to kill Valerie with..")
                    self.caught()

            elif tool_choice == "2" and self.current_room == 3 and not self.__berry2:

                print("You can now navigate through the woods")
                self.__flashlight = True

            elif tool_choice == "3" and self.current_room == 3 and self.__berry2:

                print("You can now navigate through the woods")
                self.__flashlight = True

            # allows for the berry to be in slot 2 or 3
            elif tool_choice == "3" and self.current_room == 2 and not self.__berry2:
                print("You have spiked Valerie's drink")
                print("Valerie comes back and starts choking on her drink, you must escape")
                self.__valerie_choked = True

            elif tool_choice == "2" and self.current_room == 2 and self.__berry2:
                print("You have spiked Valerie's drink")
                print("Valerie comes back and starts choking on her drink, you must escape")
                self.__valerie_choked = True

            # You can only use the car keys in the last room to escape after valerie has been killed
            elif (tool_choice == "4" or tool_choice == "3") and self.current_room == 0 and (self.__valerie_dead or self.__valerie_choked) and car_keys.found:
                print("You use the keys to start the strangers car")
                self.escape()

            else:
                print("Tool cannot be used")

        self.update()

    # Method for detective to review clues found
    def review_clues(self):
        print("\nExamined Clues:")
        if self.__examined_clues:
            for clue in self.__examined_clues:
                print(f"{clue.name}: {clue.description}")

        else:
            print("No clues have been examined yet.")

        self.update()

    # Method for murderer to escape
    def escape(self):
        choice = input("You have Escaped!\nDo you want to start a new game? Yes/No:")
        if choice.lower() == "yes":
            self.__game_started = False
            self.run()

        elif choice.lower() == "no":
            self.__game_started = False
            self.__running = False

        else:
            self.__game_started = False
            self.run()

    # Method for murderer to be caught
    def caught(self):
        choice = input("You have been caught!\nDo you want to start a new game? Yes/No:")
        if choice.lower() == "yes":
            self.__game_started = False
            self.run()
        elif choice.lower() == "no":
            self.__game_started = False
            self.__running = False

        else:
            self.__game_started = False
            self.run()

    def arrest(self):
        # you have to at least examine 4 clues before making an arrest
        if len(self.__examined_clues) >= 4:
            print(f"1.{self.__boyfriend.get_name()}")
            print(f"2.{self.__ex_bestfriend.get_name()}")
            print(f"3.{self.__bar_man.get_name()}")
            print(f"4.{self.__receptionist.get_name()}")
            selection = input("Choose a Character to arrest:")

            if selection == "1":
                print(f"You arrest John(Boyfriend) for the murder of Valerie")
                print("Great Work!, Case closed!")
                choice = input("Do you want to start a new game? Yes/No :")
                if choice.lower() == "yes":
                    self.__game_started = False
                    self.run()

                elif choice.lower() == "no":
                    self.__game_started = False
                    self.__running = False

                else:
                    self.__game_started = False
                    self.run()

            elif selection == "2" or "3" or "4":
                print("You have arrested the wrong person and the murderer has escaped!")
                choice = input("Do you want to start a new game? Yes/No :")
                if choice.lower() == "yes":
                    self.__game_started = False
                    self.run()

                elif choice.lower() == "no":
                    self.__game_started = False
                    self.__running = False

                else:
                    self.__game_started = False
                    self.run()
        else:
            print("You need to find more clues before you arrest someone")
            self.update()

    # Method to continue current game after going back to the menu
    def continue_game(self):
        if self.__game_choice == "1":

            print("You continue your investigation, determined to solve the mystery...")
            self.update()

        elif self.__game_choice == "2":
            print("You continue your hunt, determined to catch your prey...")
            self.update()
        # Additional game content and interactions could go here


# Running the game in main
if __name__ == "__main__":
    game = Game()
    game.run()
