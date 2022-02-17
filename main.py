# pypair tournament maker branch for the CubeVitational Hamburg,
# a cube tournament with the following tournament structure:
# 16 people in two groups of 8 play two drafts each.
# these drafts are 3 rounds each and seatings are re-done after the fist pod.
# # After both drafts, a cut to top 8 over both groups is made.

from pypair import Tournament
from printService import PrintService
from pod import Pod

# USER-DEFINED VARIABLES
ROUND_NUMBER = 6

# Define Classes 
printService = PrintService()
pod = Pod()
to = Tournament()


###################### Reporting ######################
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
                resultList = list()
                try:
                    pod.currentResults.insert(tableNumber - 1, result)
                    print(type(result[0]))
                    resultList.append(result[0])
                    resultList.append(result[2])
                    resultList.append(result[4])
                    to.report_match(tableNumber, resultList)
                except IndexError:
                    print("Error: Result must be entered in W-L-D formatting (e.g. 2-1-0)")
            except ValueError:
                print("Error: Invalid input. Input must either be a table number from above or q to finish inputting "
                      "results.")

            printService.print_pairings(pod)


###################### Start Application  ######################
def main():
    # Welcome 
    printService.print_welcome()

    # Init Tournament
    pod.load_players()

    # Randomize seatings
    pod.randomize_seating()

    # Add Players to Tournament
    for p in range(len(pod.playerList[0])):
        to.add_player(pod.playerList[0][p], pod.playerList[1][p], False)

    # Start Tournament
    for round_ in range(3):
        pod.new_pairings(to.pair_round())
        printService.print_pairings(pod)

        report_results(pod.currentPairings, pod.playerList)

        # Print out current standings
        printService.print_standings(to, pod)
        pod.roundNumber += 1

    # Initialize the second pod for the group with new random seatings
    toTwo = Tournament()
    podTwo = Pod()
    podTwo.load_players()
    podTwo.randomize_seating()

    # Add Players to Tournament
    for p in range(len(podTwo.playerList[0])):
        toTwo.add_player(podTwo.playerList[0][p], podTwo.playerList[1][p], False)

    print(podTwo.playerList)

    for round_ in range(3):
        podTwo.new_pairings(toTwo.pair_round())
        printService.print_pairings(podTwo)

        report_results(podTwo.currentPairings, podTwo.playerList)

        # Print out current standings
        printService.print_standings(toTwo, podTwo)
        podTwo.roundNumber += 1

    printService.print_merged_standings(toTwo, podTwo, to)


if __name__ == "__main__":
    main()
