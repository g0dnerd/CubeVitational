import copy
import csv
import random
from reportingService import get_nth_key
from pypair import Tournament


class Pod:
    def __init__(self):
        self.to = Tournament()
        self.roundNumber = 1
        self.playerList = []
        self.currentPairings = []
        self.currentResults = []

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
        self.currentResults = ["MISSING"] * len(self.currentPairings)


class MultiPod(Pod):
    def __init__(self, roundNumber_, draftsAmount):
        super().__init__()
        self.roundsAmount = roundNumber_
        self.draftsAmount = draftsAmount
        self.draftNumber = 1

    def reset_pod(self):
        self.to = Tournament()
        self.roundNumber = 1
        self.currentPairings = []
        self.currentResults = []
        self.draftNumber += 1

        for p in range(len(self.playerList[0])):
            self.to.add_player(self.playerList[0][p], self.playerList[1][p], False)


class TrackingPod(Pod):
    def __init__(self):
        super().__init__()

    def shadow_playerlist(self, pod_):
        self.playerList = copy.deepcopy(pod_.playerList)
        for p in range(len(self.playerList[0])):
            self.to.add_player(self.playerList[0][p], self.playerList[1][p], False)

    def shadow_pairings(self, pod_):
        self.to.reset_round()
        self.currentPairings = copy.deepcopy(pod_.currentPairings)
        for table in self.currentPairings:
            self.to.pair_players(self.currentPairings[table][0], self.currentPairings[table][1])

    def shadow_results(self, pod_):
        self.currentResults = copy.deepcopy(pod_.currentResults)
        result = list()
        for matches in range(len(self.currentPairings)):
            tableNumber = get_nth_key(self.currentPairings, matches)
            result.clear()
            result.append(self.currentResults[matches][0])
            result.append(self.currentResults[matches][2])
            result.append(self.currentResults[matches][4])
            p1_name = self.to.playersDict[self.currentPairings[tableNumber][0]]["Name"]
            p2_name = self.to.playersDict[self.currentPairings[tableNumber][1]]["Name"]
            print("Reporting result %s vs %s: %s - %s - %s" % (p1_name, p2_name, result[0], result[1], result[2]))
            self.to.report_match(tableNumber, result)
