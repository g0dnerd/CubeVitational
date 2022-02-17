from printService import PrintService
from pod import Pod

# USER-DEFINED VARIABLES
ROUND_NUMBER = 3

# Define Classes 
printService = PrintService()
podOne = Pod()
podTwo = Pod()
podLarge = Pod()


###################### Reporting ######################
def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


def report_results(pairings_, playerList_, pod_):
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
                    pod_.currentResults.insert(tableNumber - 1, result)
                    podLarge.currentResults.insert(tableNumber - 1, result)
                    resultList.append(result[0])
                    resultList.append(result[2])
                    resultList.append(result[4])
                    pod_.to.report_match(tableNumber, resultList)
                    podLarge.to.report_match(tableNumber, resultList)
                except IndexError:
                    print("Error: Result must be entered in W-L-D formatting (e.g. 2-1-0)")
            except ValueError:
                print("Error: Invalid input. Input must either be a table number from above or q to finish inputting "
                      "results.")

            printService.print_pairings(pod_)


###################### Start Application  ######################
def main():
    # Welcome 
    printService.print_welcome()

    # Init pods
    podOne.load_players()
    podTwo.load_players()
    podLarge.load_players()

    # Randomize seatings - import them for the overview pod
    podOne.randomize_seating()
    podLarge.import_seating(podOne)

    # Start the first of two pods
    for round_ in range(ROUND_NUMBER):
        podOne.new_pairings()
        podLarge.import_pairings(podOne)
        printService.print_pairings(podOne)

        report_results(podOne.currentPairings, podOne.playerList, podOne)

        # Print out current standings
        printService.print_standings(podLarge)
        podOne.roundNumber += 1
        podLarge.roundNumber += 1

        # Repeat till Finish

    # Start the second of two pods
    podTwo.randomize_seating()

    for round_ in range(ROUND_NUMBER):
        podTwo.new_pairings()
        podLarge.import_pairings(podTwo.currentPairings)
        printService.print_pairings(podTwo)

        report_results(podTwo.currentPairings, podTwo.playerList, podTwo)

        # Print out current standings
        print(podLarge.playerList)
        printService.print_standings(podLarge)
        podTwo.roundNumber += 1
        podLarge.roundNumber += 1


if __name__ == "__main__":
    main()
