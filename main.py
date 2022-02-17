from pypair import Tournament
from printService import PrintService
from pod import Pod

# USER-DEFINED VARIABLES
ROUND_NUMBER = 3

# Define Classes 
printService = PrintService()
pod = Pod()

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
                    pod.current_results.insert(tableNumber - 1, result)
                    resultList.append(result[0])
                    resultList.append(result[2])
                    resultList.append(result[4])
                    pod.to.report_match(tableNumber, resultList)
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

    # Start Tournament
    for round_ in range(ROUND_NUMBER):
        pod.new_pairings()
        printService.print_pairings(pod)

        report_results(pod.currentPairings, pod.playerList)

        # Print out current standings
        printService.print_standings(pod)
        pod.roundNumber += 1

        # Repeat till Finish


if __name__ == "__main__":
    main()
