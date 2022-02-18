from printService import PrintService
import reportingService
from pod import Pod

# USER-DEFINED VARIABLES
ROUND_NUMBER = 3

# Define Classes 
printService = PrintService()
pods = []


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

                choice = reportingService.report_results(pods[podNumber])
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
