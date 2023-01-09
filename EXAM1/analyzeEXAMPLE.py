def analyze_paragraphs(fname):
    f = open(fname,"r")
    #variables to keep track of line count of each paragraph and keeps track of the current max
    pcount = 0
    max = 0
    #for loop loops through each line in the file after opening
    for i in f:
        #Strips line of any hidden extra characters and checks to see if it is <p>
        if i.rstrip() == "<p>":
            #if it finds the <p> then it prints out the amount of lines found compares to the previous max
            #and resets the current counter
            print(str(pcount) + "-line paragraph")
            if max < pcount:
                max = pcount
            pcount = 0
        else:
            #if it does find the <p> increments the line count by 1
            pcount += 1
    #returns the max
    return max
    f.close()