#! /usr/bin/python

import sys, os, csv

"""
A program to get started with DnD character generation, leveling up, and PDF printout.
A Mint Jam Idea production.
12/7/17
"""
class Character(object):

    # class to represent a character
    name = ''
    d_description = {'age' : '', 'height' : '', 'weight' : '', 'eyes' : '', 'skin' : '', 'hair' : ''}
    player_name = ''
    char_class = ''
    level = ''
    background = ''
    alignment = ''
    exp = ''
    d_stats = {'strength' : '','dexterity' : '','constitution' : '','intelligence' : '','wisdom' : '','charisma' : '',}
    inspiration = ''
    prof_bonus = ''
    d_saves = {'str_save' : '', 'dex_save' : '', 'con_save' : '', 'int_save' : '', 'wis_save' : '', 'cha_save' : ''}
    d_skills = {'acrobatics' : '','animal_handling' : '', 'arcana' : '', 'athletics' : '', 'deception' : '', 'history' : '', 'insight' : '', 'intimidation' : '', 'investigation' : '', 'medicine' : '', 'nature' : '', 'perception' : '', 'performance' : '', 'persuasion' : '', 'religion' : '', 'sleight_of_hand' : '', 'stealth' : '', 'survival' : ''}
    passive_perception = ''
    armor_class = ''
    initiative = ''
    speed = ''
    hit_points = ''
    hit_dice = ''
    languages = []
    d_wealth = {'pp' : '', 'gp' : '','ep' : '','sp' : '','cp' : ''}
    wealth_other = []
    equipment = []
    d_weapons = {}
    spell_points = ''

    def __init__(self):
        #initialize a character.
        #self.name = name
        pass

    def __str__(self):
        #string representation of an object, for printing
        return self.name + "\n"

    def add_name(self, name):
        #add name to current character
        self.name = name

def read_file(filename):
    fhandle = open(filename, 'r')
    for line in fhandle:
            stats = line
    fhandle.close()
    return stats

def parse_csv(stats):
    # generator that splits the string twice and builds a dictionary, all in one line!
    d_stats = dict(item.split('|') for item in stats.split(','))
    return d_stats

def main():
    #get character data from user (break out into own function?)
    #this will include all data which are given by user, not calculated
    char = Character()
    char.name = raw_input("Enter character name: ")
    char.d_description['age'] = raw_input("Enter character age: ")
    #use csv module to build character data csv (break out into own function?)
    with open('char.csv', 'w') as csvfile:
        fieldnames = ['name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name': char.name, 'age': char.d_description})
    '''
    #obtain stat bonus from stats.csv file
    filename = 'stats.csv'
    stats = read_file(filename)
    d_stats = parse_csv(stats)
    stat = raw_input("What is your stat? ")
    # strip the effing leading space from the effing question.
    stat = stat.lstrip()
    # remove the \n character stored with the 20 from the file.
    print d_stats[stat].rstrip()
    '''


    '''
    d_char = {}
    while True:
        char_name = raw_input("Enter character name: ")
        char_race = raw_input("Enter character race: ")
        char_class = raw_input("Enter character class: ")
        char_level = raw_input("Enter character level: ")
        d_char[char_name]="\nRace: " + char_race + "\nClass: " + char_class + "\nLevel: " + char_level
        for key, value in d_char.iteritems():
            print "Name: ", key, value
    '''
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:  # try to ensure a clean exit
        print "Interrupted"
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)