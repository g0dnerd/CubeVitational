import copy
import csv
import random
from printService import PrintService

printService = PrintService()


class Pod:
    roundNumber = 1
    playerList = []
    currentPairings = []
    current_results = []

    def randomize_seating(self):
        # print("Unrandomized group: ", Pod.playerList)
        # printService.print_table(self)
        tempPlayerList = copy.deepcopy(Pod.playerList)
        [random.shuffle(sublist) for sublist in tempPlayerList]
        for i in range(len(Pod.playerList[0])):
            tempPlayerList[0][i] = Pod.playerList[0][Pod.playerList[1].index(tempPlayerList[1][i])]

        # print("\n Randomized seatings for this group: ", tempPlayerList[1])
        Pod.playerList = tempPlayerList
        printService.print_table(self)

    @staticmethod
    def load_players():
        listToFill = [[] for _ in range(2)]
        # csvPath = input("Please enter the full name of the relevant CSV file: ")
        # print("Please enter the full name of the relevant CSV file: ")
        csvPath = 'playerlist1.csv'
        with open(csvPath) as csvfile:
            playerReader = csv.reader(csvfile, delimiter=',')
            for player in playerReader:
                # skip the row with headers
                if player[0] != 'ID:':
                    listToFill[0].append(int(player[0]))
                    listToFill[1].append(player[1])

        Pod.playerList = listToFill

    @staticmethod
    def new_pairings(new_pairings):
        Pod.currentPairings = new_pairings
        Pod.current_results = ["MISSING"] * len(Pod.currentPairings)
