# from nis import match
import csv
from printService import PrintService
from pod import Pod

# USER-DEFINED VARIABLES
ROUND_NUMBER = 3

# Define Classes 
printService = PrintService()
pods = []


###################### Reporting ######################
def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


def report_results(pod):
    choice = ''

    while (choice != 'm') and (choice != 'f'):
        choice = input('Please choose the result you want to input (m = menu, f = finish round): ')

        # Report results
        if (choice != 'm') and (choice != 'f'):
            try:
                tableNumber = get_nth_key(pod.currentPairings, int(choice) - 1)
                player1 = pod.playerList[1][pod.playerList[0].index(pod.currentPairings[tableNumber][0])]
                player2 = pod.playerList[1][pod.playerList[0].index(pod.currentPairings[tableNumber][1])]
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
        # Finish Round
        elif choice == 'f':
            pod.new_pairings()
            pod.roundNumber += 1
            printService.print_standings(pod)

        return choice


###################### Start Application  ######################
def main():
    # Welcome and Init
    printService.print_welcome()
    podNumber = 0
    init_new_pod()

    # ************** Menu ********************
    while True:
        printService.print_menu(podNumber, len(pods))
        option = input("* Please choose Option:")

        # Start/Resume Round of current Pod
        if option == '1':
            for round_ in range(ROUND_NUMBER):
                printService.print_pairings(pods[podNumber])

                choice = report_results(pods[podNumber])
                if choice == 'm':
                    break


        # Switch to next Pod
        elif option == '2':
            if (len(pods) - 1) == podNumber:
                podNumber = 0
            else:
                podNumber += 1

            printService.print_pairings(pods[podNumber])

        # Show Standings of current Pod 
        elif option == '3':
            printService.print_standings(pods[podNumber])

        # Add Pod
        elif option == '4':
            print("Add Pod")
            init_new_pod()

        # Show seatings
        elif option == '5':
            printService.print_table(pods[podNumber])

        elif option == '6':
            pods[podNumber].new_pairings()
        # Default / CatchAll
        else:
            print("* Please choose from Options                                            *")


def init_new_pod():

    pods.append(Pod())
    pods[len(pods) - 1].load_players()
    pods[len(pods) - 1].randomize_seating()
    pods[len(pods) - 1].new_pairings()


if __name__ == "__main__":
    main()
