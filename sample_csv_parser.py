def main():
    fhandle = open('stats.csv', 'r')
    stats = []
    split_stats = []
    d_stats = {}
    # add each item in the file into a list
    for item in fhandle:
        stats.append(item)
    
    # parse the item string on a comma and store in a variable
    for item in stats: 
        split_stats = item.split(',')
    
    # parse on pipe and store in dictionary
    for item in split_stats:
        val = item.split('|')
        d_stats[val[0]] = val[1]
    stat = raw_input("What is your stat? ")
    # strip the effing leading space from the effing question.
    stat = stat.lstrip()
    print d_stats[stat]

try:
    if __name__ == "__main__":
        main()
    else:
        pass
except KeyboardInterrupt:
pass
