from pypair import Tournament
import os
import csv

home = os.path.expanduser("~")

# create two separate tournaments for the two groups and load in player list CSVs.
to = Tournament()
playerList = [[] for _ in range(2)]

csvPath = input("Please enter the full name of the relevant CSV file: ")


def load_players(pathToLoad, listToFill):
    with open(pathToLoad) as csvfile:
        playerReader = csv.reader(csvfile, delimiter=',')
        for p in playerReader:
            # skip the row with headers
            if p[0] != 'ID:':
                listToFill[0].append(int(p[0]))
                listToFill[1].append(p[1])


to.load_player_csv(csvPath)
load_players(csvPath, playerList)


def print_pairings(pairings_, playerList_):
    for table in pairings_:
        player1 = playerList_[1][playerList_[0].index(pairings_[table][0])]
        player2 = playerList_[1][playerList_[0].index(pairings_[table][1])]
        print('Table %s: %s - %s' % (table, player1, player2))


def main():
    pairings = to.pair_round()
    print_pairings(pairings, playerList)
    print("")


if __name__ == "__main__":
    main()
