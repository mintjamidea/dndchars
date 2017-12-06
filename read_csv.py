

def main():
    fhandle = open('stats.csv', 'r')
    stats = []
    split_stats = []
    d_stats = {}
    for item in fhandle:
        stats.append(item)
    
    for item in stats: 
        split_stats = item.split(',')
    
    for item in split_stats:
        val = item.split('|')
        d_stats[val[0]] = val[1]
    for key, value in d_stats.items():
        print key, "===>", value
        print type(key), type(value)
    stat = raw_input("What is your stat? ")
    stat = stat.lstrip()
    print d_stats[stat]

try:
    if __name__ == "__main__":
        main()
    else:
        pass
except KeyboardInterrupt:
    pass

