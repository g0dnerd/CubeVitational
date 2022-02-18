import copy
import csv
import random
from pypair import Tournament


class Pod:
    def __init__(self):
        self.to = Tournament()
        self.roundNumber = 1
        self.playerList = []
        self.currentPairings = []
        self.current_results = []

    def randomize_seating(self):
        tempPlayerList = copy.deepcopy(self.playerList)
        [random.shuffle(sublist) for sublist in tempPlayerList]
        for i in range(len(self.playerList[0])):
            tempPlayerList[0][i] = self.playerList[0][self.playerList[1].index(tempPlayerList[1][i])]

        # print("\n Randomized seatings for this group: ", tempPlayerList[1])
        self.playerList = tempPlayerList

    def load_players(self):
        listToFill = [[] for _ in range(2)]
        csvPath = input("CSV file: ")
        # print("Please enter the full name of the relevant CSV file: ")
        # csvPath = 'playerlist1.csv'
        with open(csvPath) as csvfile:
            playerReader = csv.reader(csvfile, delimiter=',')
            for player in playerReader:
                # skip the row with headers
                if player[0] != 'ID:':
                    listToFill[0].append(int(player[0]))
                    listToFill[1].append(player[1])

        self.playerList = listToFill

        for p in range(len(self.playerList[0])):
            self.to.add_player(self.playerList[0][p], self.playerList[1][p], False)

    def new_pairings(self):
        self.currentPairings = self.to.pair_round()
        self.current_results = ["MISSING"] * len(self.currentPairings)


class MultiPod(Pod):
    def __init__(self, roundNumber, draftsAmount):
        super().__init__()
        self.roundNumber = roundNumber
        self.draftsAmount = draftsAmount
