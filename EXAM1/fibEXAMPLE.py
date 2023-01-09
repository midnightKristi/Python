
def is_fib_like(intlist):

    #gets the length of the list
    listLen = len(intlist)

    #checks to see if the list is less than 2 and if so will automatically return true
    if listLen > 2:
        #if the list length is greater than 2 it calculates the formula for the fib sequence and compares each number
        #fib1 grabs the first integer in the list also acts as the "seed" or first number
        fib1 = intlist[0]
        #fib2 grabs the second integer in the list
        fib2 = intlist[1]
        #temp is next calculated number in the sequence starts as 0
        temp = 0
        #beginning interation number to skip first two integers
        i = 2
        #loops through the list starting at the 3rd given integer
        while i < listLen:
            #temp is calculated by adding the previous number to the current number
            temp = intlist[i - 1] + intlist[i - 2]

            #compares the calculated sequnce number (temp) to the given list number to see if it matches
            if temp != intlist[i]:
                #if it does not match return false it does not follow the sequence
                return False
            #iterate the loop up one
            i += 1
    #if list length is less than 2 or temp always matches the compared number returns true follows the sequnce
    return True