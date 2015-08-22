"""
This is a physics game where you chuck mudballs at people. 
You and another friend input the psi and angle in degrees that you want your cannon to be set to

"""
 
import math
import random
 
 
def print_instructions():
    """ This function prints the instructions. """
 
    # You can use the triple-quote string in a print statement to
    # print multiple lines.
    print("""
Welcome to Mudball! You win by hitting the other player with a mudball.
Enter your angle (in degrees) and the amount of PSI to charge your canon
with.
        """)
 
 
def calculate_distance(psi, angle_in_degrees):
    """ Calculate the distance the mudball flies. """
    angle_in_radians = math.radians(angle_in_degrees)
    distance = psi * math.sin(angle_in_radians) * 15
    return distance
 
 
def get_user_input(name):
    """ Get the user input for psi and angle. Return as a list of two
    numbers. """
    # Later on in the 'exceptions' chapter, we will learn how to modify
    # this code to not crash the game if the user types in something that
    # isn't a valid number.
    psi = float(input(name + " charge the gun with how many psi? "))
    angle = float(input(name + " move the gun at what angle? "))
    return psi, angle
 
 
def get_player_names():
    """ Get a list of names from the players. """
    print("Enter player names. Enter as many players as you like.")
    done = False
    players = []
    while not done:
        player = input("Enter player (hit enter to quit): ")
        if len(player) > 0:
            players.append(player)
        else:
            done = True
 
    print()
    return players
 
 
def process_player_turn(player_name, distance_apart):
    """ The code runs the turn for each player.
    If it returns False, keep going with the game.
    If it returns True, someone has won, so stop. """
    psi, angle = user_input = get_user_input(player_name)
 
    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart
 
    # By looking ahead to the chapter on print formatting, these
    # lines could be made to print the numbers is a nice formatted
    # manner.
    if difference > 1:
        print("You went", difference, "yards too far!")
    elif difference < -1:
        print("You were", difference * -1, "yards too short!")
    else:
        print("Hit!", player_name, "wins!")
        return True
 
    print()
    return False
 
 
def main():
    """ Main program. """
 
    # Get the game started.
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)
 
    # Keep looking until someone wins
    done = False
    while not done:
        # Loop for each player
        for player_name in player_names:
            # Process their turn
            done = process_player_turn(player_name, distance_apart)
            # If someone won, 'break' out of this loop and end the game.
            if done:
                break
 
if __name__ == "__main__":
    main()