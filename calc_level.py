#! /usr/bin/python

"""
A Mint Jam Idea production.
author: tc
12/9/17

Let's calculate level by xp entered by user.
"""

def read_file(filename):
    fhandle = open(filename, 'r')
    for line in fhandle:
        exp = line
    fhandle.close()
    return exp

def parse_csv(exp):
    # generator that splits the string twice and builds a dictionary, all in one line!
    d_exp = dict(item.split('|') for item in exp.split(','))
    return d_exp

def check_level():
    pass

def main():
    filename = 'exp_thresholds.csv'
    exp = read_file(filename)
    d_exp = parse_csv(exp)
    answer_xp = int(raw_input('How much xp do you have? '))
    keys = []
    for key, value in d_exp.iteritems():
        keys.append(int(key))
    keys = sorted(keys)

    for cur_xp in keys:
        if answer_xp >= cur_xp:
            continue
        else:
            print "Your level is:", d_exp[str(keys[keys.index(cur_xp)-1])]
            break

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:  # try to ensure a clean exit
    pass
