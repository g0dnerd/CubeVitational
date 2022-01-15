import copy
import csv
import random
from operator import getitem
from pypair import Tournament
from collections import OrderedDict

# USER-DEFINED VARIABLES
ROUND_NUMBER = 3

# initialize the tournament
to = Tournament()


def load_players(pathToLoad, listToFill):
    with open(pathToLoad) as csvfile:
        playerReader = csv.reader(csvfile, delimiter=',')
        for player in playerReader:
            # skip the row with headers
            if player[0] != 'ID:':
                listToFill[0].append(int(player[0]))
                listToFill[1].append(player[1])


def randomize_seating(playerList_):
    tempPlayerList = copy.deepcopy(playerList_)
    [random.shuffle(sublist) for sublist in tempPlayerList]
    for i in range(len(playerList_[0])):
        tempPlayerList[0][i] = playerList_[0][playerList_[1].index(tempPlayerList[1][i])]
    return tempPlayerList


def print_pairings(pairings_, playerList_, roundNumber_):
    print('\nPAIRINGS FOR ROUND %s:' % roundNumber_)
    for table in pairings_:
        player1 = playerList_[1][playerList_[0].index(pairings_[table][0])]
        player2 = playerList_[1][playerList_[0].index(pairings_[table][1])]
        print('Table %s: %s - %s' % (table, player1, player2))


def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


def report_results(pairings_, playerList_):
    choice = ''

    while choice != 'q':
        choice = input('Please choose the result you want to enter or input q to finish inputting results: ')

        if choice != 'q':
            try:
                tableNumber = get_nth_key(pairings_, int(choice) - 1)
                player1 = playerList_[1][playerList_[0].index(pairings_[tableNumber][0])]
                player2 = playerList_[1][playerList_[0].index(pairings_[tableNumber][1])]
                result = input('Enter result %s vs %s in W-L-D format: ' % (player1, player2))
                print("")
                resultList = list()
                try:
                    resultList.append(result[0])
                    resultList.append(result[2])
                    resultList.append(result[4])
                    to.report_match(tableNumber, resultList)
                except IndexError:
                    print("Error: Result must be entered in W-L-D formatting (e.g. 2-1-0)")
            except ValueError:
                print("Error: Invalid input. Input must either be a table number from above or q to finish inputting "
                      "results.")


def print_standings():
    standingsDict = copy.deepcopy(to.playersDict)
    standingsDict = OrderedDict(sorted(standingsDict.items(), reverse = True, key = lambda x: getitem(x[1], 'OMW%')))
    standingsDict = OrderedDict(sorted(standingsDict.items(), reverse = True, key = lambda x: getitem(x[1], 'Points')))
    counter = 1
    for players in standingsDict:
        tempName = standingsDict[players]['Name']
        tempPoints = standingsDict[players]['Points']
        tempOMW = (standingsDict[players]['OMW%'])[0:6]
        print('%s. %s - %s - %s' % (counter, tempName, tempPoints, tempOMW))
        counter += 1


def main():
    playerList = [[] for _ in range(2)]
    csvPath = input("Please enter the full name of the relevant CSV file: ")
    load_players(csvPath, playerList)
    # print("Unrandomized group: ", playerList)
    playerList = randomize_seating(playerList)
    print("\n Randomized seatings for this group: ", playerList[1])

    for p in range(len(playerList[0])):
        to.add_player(playerList[0][p], playerList[1][p], False)

    roundNumber = 1
    for round_ in range(ROUND_NUMBER):
        pairings = to.pair_round()
        print_pairings(pairings, playerList, roundNumber)
        print("")
        report_results(pairings, playerList)

        # print out current standings
        print('\n STANDINGS AFTER ROUND %s' % roundNumber)
        print('   Name - Points - OMW')
        print_standings()
        roundNumber += 1


if __name__ == "__main__":
    main()
