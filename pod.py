import copy
import csv
import random
from printService import PrintService
from pypair import Tournament

printService = PrintService()

class Pod:
    to = Tournament()
    roundNumber = 1
    playerList = []
    currentPairings = []
    current_results = []

    def randomize_seating(self):
        tempPlayerList = copy.deepcopy(self.playerList)
        [random.shuffle(sublist) for sublist in tempPlayerList]
        for i in range(len(self.playerList[0])):
            tempPlayerList[0][i] = self.playerList[0][self.playerList[1].index(tempPlayerList[1][i])]

        # print("\n Randomized seatings for this group: ", tempPlayerList[1])
        self.playerList = tempPlayerList
        printService.print_table(self)

    def load_players(self):
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

        self.playerList = listToFill
        self.addPlayers()

    def new_pairings(self):
        self.currentPairings = self.to.pair_round()
        self.current_results = ["MISSING"] * len(self.currentPairings)

    def addPlayers(self):
        for p in range(len(self.playerList[0])):
            self.to.add_player(self.playerList[0][p], self.playerList[1][p], False)
