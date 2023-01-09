def process_scores(fname):
    f = open(fname, "r")
    #loops through each line of the file
    for i in f:
        #stores the name and removes any hidden extra characters
        name = i.rstrip()
        #reads the next line with the socres
        scorel = f.readline()
        #gets the total score count
        scoretot = scorel.count("+") + scorel.count("-")
        #calculates the percentage of + occuring compared to the total as float
        percent = float(scorel.count("+")) / float(scoretot)
        #formats to include a rounded 0.1% decimal percentage
        percent = "{:.1%}".format(percent)
        #prints the name and percentage format
        print(name + ": " + percent + " plus")
    f.close()