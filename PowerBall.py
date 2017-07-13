# Corey Fisher
# 7/12/2017
# Submission for Greenphire assessment
# Power Ball lottery entry program
# Great exercise. Had a lot of fun with it!

from random import *
#######################################################################

######   Variable Declarations ########################################
entryArray = [] # stores name/picks of all entries.
allNums = []    # stores all favorite numbers entered of all entries.
winner = []     # stores the winning 6 PowerBall numbers.
ties = []       # stores numbers that tie for highest frequency
                # that will be pulled randomly to fill winner[].
again = True    # take another entry or display results?
maxCounts = {}  # dictionary to hold number/count of all numbers entered.
spotsToFill = 5 # number of favorites the winning number still needs.
maxFreq = 0     # highest frequency of any favorite number spanning all entries.
maxPBFreq = 0   # highest frequency of any Power Ball number across entries.
maxPBCounts = {}# dictionary for number/count of all Power Ball numbers.
PBTies = []     # stores the values of PB numbers tied for highest frequency.
pbArray = []    # stores the PB numbers that are extracted from
                # Entry objects.
#########################################################################


###### Class/Method Declarations ######################################

# set up an object for each entry with name and picks
class Entry(object):
    def __init__(self, firstName, lastName, picks):
        self.firstName = firstName
        self.lastName = lastName
        self.picks = picks
    
# get one favorite number
def get_number(picks):
    while True:
        try:
            num = int(input("Enter a number: "))
            while num < 1 or num > 69:
                num = int(input("Enter a number from 1-69 only: "))
            break
        except:
            print("Alpha characters are invalid.")
    #check for dupes
    for p in picks:
        if p == num:
            # if a dupe is found, call self recursively
            print("Number already exists. ")
            return get_number(picks)
    return num

#get the 6th powerball number
def get_pb_number():
    while True:
        try:
            pb = int(input("Enter your PowerBall number(1-26): "))
            while pb < 1 or pb > 26:
                pb = int(input("MUST BE FROM 1-26: "))
            break
        except:
            print("Alpha characters are invalid.")
    return pb

#obtain the highest frequency of any duplicate number in the list
def getMaxFreq(array):
    highestFreq = 0
    for key, value in array.items():
        if value > highestFreq:
            highestFreq = value
    return highestFreq

#create a dictionary to find the number(s) with the highest frequency
def makeDict(array):
    maxCounts = {}
    for i in array:
        if i not in maxCounts:
            maxCounts[i] = 1
        else:
            maxCounts[i] += 1
    return maxCounts

def findTies(dictionary, freq):
    ties = []
    for key, value in dictionary.items():
        if value == freq:
            ties.append(key)
    return ties
###### End Method Declarations ##########################################
        
#########################################################################

#get user input and store attributes in the Entry class
while again == True:
    picks = []      # store picks for current Entry
    first = input("first name: ")
    last = input("last name: ")
    print("Please enter 5 numbers from 1-69 with no duplicates.")

    for i in range(5):
        newRand = get_number(picks)
        picks.append(newRand)
        
    for i in range(5):
        allNums.append(picks[i])
    pb = get_pb_number()
    picks.append(pb)
    
    newEntry = Entry(first, last, picks)
    entryArray.append(newEntry)
    select = input("Another entry?(y/n) ").lower()
    while select != 'n' and select != 'y':
            select = input("Please make a valid selection(y/n) ").lower()
    if select == 'n':
        again = False
   
# extract winning numbers based on user entries
maxCounts = makeDict(allNums)
maxFreq = getMaxFreq(maxCounts)
# fill up the winning number array (1-5)
while spotsToFill > 0:
    #count unique numbers with the maximum frequency...
    maxFreqNums = 0
    for key, value in maxCounts.items():
        if value == maxFreq:
            maxFreqNums +=1
    #...and if there are enough spots, put them in the winning number list
    #and decrease number of spots left to fill
    if maxFreqNums <= spotsToFill:
        for key, value in maxCounts.items():
            if value == maxFreq:
                winner.append(key)
                spotsToFill -=1
    #otherwise, select (spotsToFill) numbers with max frequency randomly
    #and decrease (spotsToFill).
    else: 
        #fill the array with numbers that are tied for max freq
        ties = findTies(maxCounts, maxFreq)
        #randomly select one and remove it from the possible choices
        #until (spotsToFill) numbers have been picked.
        for i in range(spotsToFill):
            rng = randint(0, len(ties)-1)
            winner.append(ties[rng])
            ties.pop(rng)
            spotsToFill -= 1
    #decrease maxFreq by 1.
    maxFreq -=1


#And finally, get the winning 6th Power Ball number.
#First, populate the PB number array
for i in range(len(entryArray)):
    pbArray.append(entryArray[i].picks[5])
# determine and fill the array with numbers that are tied for max freq
maxPBCounts = makeDict(pbArray)
maxPBFreq = getMaxFreq(maxPBCounts)
PBTies = findTies(maxPBCounts, maxPBFreq)
rng = randint(0, len(PBTies)-1)
winner.append(PBTies[rng])
winner.sort()

# print all the entry names and picks
for i in range(len(entryArray)):
    print ("{} {}: ".format(entryArray[i].firstName, entryArray[i].lastName)
           , end = '')
    for j in range(5):
        print("{} ".format(entryArray[i].picks[j])
               , end = '')
    print("Power Ball: {}".format(entryArray[i].picks[5]))
print("Winning Numbers: ", end = '')
for i in range(5):
    print ("{} ".format(winner[i]), end = '')
print (" Power Ball: {}".format(winner[5]))
    



            





