#! /usr/bin/python

import sys, os, csv, pickle
from random import randint
from calc_level import calculate

"""
A program to get started with DnD character generation, leveling up, and PDF printout.
A Mint Jam Idea production.
12/7/17
"""

abilities = ["strength", "dexterity", "constitution", "intelligence", \
             "wisdom", "charisma"]

class Character(object):
    # class to represent a character

    name = ''
    age = ''
    height = ''
    weight = ''
    eyes = ''
    skin = ''
    hair = ''
    player_name = ''
    char_race = ''
    char_class = ''
    level = ''
    background = ''
    alignment = ''
    exp = ''

    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0           
    inspiration = ''
    prof_bonus = ''
    
    str_save = 0
    dex_save = 0
    con_save = 0
    int_save = 0
    wis_save = 0
    cha_save = 0
    
    skill_acrobatics = 0
    skill_animal_handling = 0
    skill_arcana = 0
    skill_athletics = 0
    skill_deception = 0
    skill_history = 0
    skill_insight = 0
    skill_intimidation = 0
    skill_investigation = 0
    skill_medicine = 0
    skill_nature = 0
    skill_perception = 0
    skill_performance = 0
    skill_persuasion = 0
    skill_religion = 0
    skill_sleight_of_hand = 0
    skill_stealth = 0
    skill_survival = 0

    passive_perception = 10 + skill_perception
    armor_class = 0
    initiative = 0
    speed = 0
    hit_points = 0
    hit_dice = 0
    spell_points = 0
    languages = []
    wealth_pp = 0
    wealth_gp = 0
    wealth_ep = 0
    wealth_sp = 0
    wealth_cp = 0
    wealth_other = []
    equipment = []
    weapons = []


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

def generate_stats():
    #generate 6 random numbers for use as char stats, store in list
    stat_list=[]
    for x in range(6):
        #roll 4 dice, remove lowest roll
        dice = []
        for die in range(4):
            dice.append(randint(1,6))
        dice.sort()
        del dice[0]
        stat_list.append(sum(dice))
    return stat_list

def assign_stats(pool):
    #takes a pool of 6 ability scores, asks user to assign each to an ability
    ordered_stats = []
    for ability in abilities:
        print "Available scores are: ", pool
        print "Assign one score to", ability, ":"
        selected_score = int(raw_input(">>"))
        while selected_score not in pool:
            print "Please choose a score from the list"
            selected_score = int(raw_input(">>"))
        ordered_stats.append(selected_score)
        pool.remove(selected_score)
    return ordered_stats

def get_racial_modifiers(race):
    filename = "race_" + race + "_traits.csv"
    stat_bonuses = {}
    for ability in abilities:
        stat_bonuses[ability] = obtain_stat_bonus(filename, ability)
    return stat_bonuses
    

def build_character():

    #get character data from user
    #this will include all data which are given by user, not calculated
    char = Character()
    char.name = raw_input("Enter character name: ")
    char.age = raw_input("Enter age: ")
    char.height = raw_input("Enter height: ")
    char.weight = raw_input("Enter weight: ")
    char.eyes = raw_input("Enter eye color: ")
    char.skin = raw_input("Enter skin color: ")
    char.hair = raw_input("Enter hair color: ")
    char.player_name = raw_input("Enter player name: ")
    char.char_class = raw_input("Enter player class: ")
    char.char_race = raw_input("Enter player race: ")
    char.background = raw_input("Enter character background: ")
    #maybe change alignment to menu, where choices are restricted based on class
    char.alignment = raw_input("Enter character alignment: ")
    char.exp = int(raw_input("Enter experience points: "))
    char.inspiration = int(raw_input("Enter current inspiration amount: "))
    char.level = calculate(char.exp)
    char.prof_bonus = obtain_stat_bonus('prof_bonus.csv', char.level)

    print "Let's assign the characters's ability scores"
    print "6 ability scores have been randomly generated.  They are:"
    ability_score_pool = generate_stats() #generate pool of 6 scores to assign
    ability_score_list = assign_stats(ability_score_pool) #assign those scores
    char.strength = ability_score_list[0]
    char.dexterity = ability_score_list[1]
    char.constitution = ability_score_list[2]
    char.intelligence = ability_score_list[3]
    char.wisdom = ability_score_list[4]
    char.charisma = ability_score_list[5]
    
    #get and apply racial modifiers to ability scores
    racial_ability_score_modifiers = get_racial_modifiers(char.char_race.lower())
    print racial_ability_score_modifiers
            
    #save character data via pickling
    request_save = raw_input("save character?(y/n) ")
    if request_save == 'y':
        pickle_character(char)
    
def pickle_character(char):
    #let's try pickling the user data
    file_name = char.name
    fileObject = open(file_name, 'wb')
    pickle.dump(char, fileObject)
    fileObject.close()
    
    
def obtain_stat_bonus(csvfile, stat):
    #an attempt to make a generic stat-bonus finder
    #Assumes csv stat files will all follow the same format
    filename = csvfile
    stats = read_file(filename)
    d_stats = parse_csv(stats)
    if stat in d_stats:
        print "stat bonus: ", d_stats[stat]
        return d_stats[stat]
    else:
        return 0
    
    
'''
use csv module to build character data csv (break out into own function?)
keep all on one row in CSV or use multiple rows?
currently will overwrite file if it already exists.
need to change this to overwrite only fields which have changed
char_file_name = char.name + '.csv'
with open(char_file_name, 'w') as csvfile:
    fieldnames = ['name', 'description', 'player_name', 'class']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': char.name, 'description': char.d_description,  
                     'player_name': char.player_name, 'class': char.char_class})
'''

    
def main():

    if raw_input("Are you building a new character? (y/n) ") == 'y':
        build_character()
    else:
        char_name = raw_input("Please enter name of character to adjust: ")
        file_name = char_name
        fileObject = open(file_name, 'rb')
        char = pickle.load(fileObject)
        print char.name, char.age, char.height, char.weight, char.eyes, \
        char.skin, char.hair, char.player_name, char.char_class, \
        char.background, char.alignment, char.exp, char.inspiration, \
        char.level, char.prof_bonus, char.strength, char.dexterity, \
        char.constitution, char.intelligence, char.wisdom, char.charisma
        


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