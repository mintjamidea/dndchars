#! /usr/bin/python

"""
A dummy program to get started with DnD character generation, leveling up, and PDF printout.
A Mint Jam Idea production.
12/2/17
"""

# a dumb pun function
def leppard():
    print "rock it!"


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
        leppard()

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:  # try to ensure a clean exit
    pass

