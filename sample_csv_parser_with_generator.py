#import re

def main():
    #re_get_stat = '[+|-]?\d+\|[+|-]?\d+' # super fancy...but sadly unused.  Instead I wrote a generator!
    fhandle = open('stats.csv', 'r')
    d_stats = {}
    # add each item in the file into a list
    for line in fhandle:
        statline = line
    fhandle.close()

    # generator that splits the string twice and builds a dictionary, all in one line!
    d_stats = dict(item.split('|') for item in statline.split(','))


    stat = raw_input("What is your stat? ")
    # strip the effing leading space from the effing question.
    stat = stat.lstrip()

    # remove the \n character stored with the 20 from the file.
    print d_stats[stat].rstrip()
    
try:
    if __name__ == "__main__":
        main()
    else:
        pass
except KeyboardInterrupt:
    pass
