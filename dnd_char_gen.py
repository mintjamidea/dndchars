#! /usr/bin/python

"""
A dummy program to get started with DnD character generation, leveling up, and PDF printout.
An AtCon production
ConWel? WelCon?
TimJam? JamCon?
Or perhaps an Anagram of our names?
https://new.wordsmith.org/anagram/anagram.cgi?anagram=atwell+connolly&language=english&t=500&d=&include=&exclude=&n=&m=&a=n&l=n&q=n&k=1
Frex (Tim and Jamie):
Time I Jam
I Emit Jam

Or (Atwell Connolly)
Alloy Clown Lent
Tall Nonce Lowly
Newly Tall Colon

Or (Cyclohexane and Fezik):
Chalice Key Zen Fox
Cafe Zilch Key Oxen
Zen Fecal Hickey Ox

11/18/17

12/2/17
Mint Jam Idea it is!  It's an anagram of Tim and Jamie.
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

