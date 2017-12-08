#! /usr/bin/python

"""
A program to get started with DnD character generation, leveling up, and PDF printout.
A Mint Jam Idea production.
12/7/17
"""

''' Player class from my Cribbage program...use it as a base for Character class?
class Player(object):

    # class to represent a player and keep track of all players
    # in the tournament.
    players = []
    def __init__(self, player):
        #initialize a player.
        self.name = player
        self.opponents = []

    def __str__(self):
        #string representation of an object, for printing
        return self.name + "\n" + str(self.opponents)

    def add_opponent(self, opponent):
        #add opponent to current player.
        self.opponents.append(opponent)
'''


def main():
    d_char = {}
    while True:
        char_name = raw_input("Enter character name: ")
        char_race = raw_input("Enter character race: ")
        char_class = raw_input("Enter character class: ")
        char_level = raw_input("Enter character level: ")
        d_char[char_name]="\nRace: " + char_race + "\nClass: " + char_class + "\nLevel: " + char_level
        for key, value in d_char.iteritems():
            print "Name: ", key, value

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:  # try to ensure a clean exit
    pass

