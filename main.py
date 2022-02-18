from printService import PrintService
import reportingService
from pod import Pod, MultiPod

# USER-DEFINED VARIABLES
ROUND_NUMBER = 3
DRAFT_AMOUNT = 2

# Define Classes 
printService = PrintService()
pods = []


###################### Start Application  ######################
def main():
    # Welcome and Init
    printService.print_welcome()
    podNumber = 0

    # ************** Menu ********************
    while True:
        printService.print_menu(podNumber, len(pods))
        option = input("* Please choose an option: ")

        # Start/Resume Round of current Pod
        if option == '1':
            try:
                while True:
                    printService.print_pairings(pods[podNumber])
                    choice = input('Please choose the result you want to input (m = menu, f = finish round): ')
                    if choice == 'm':
                        break

                    elif choice == 'f':
                        pods[podNumber].new_pairings()
                        pods[podNumber].roundNumber += 1
                        printService.print_standings(pods[podNumber])

                    elif reportingService.is_legal_table(choice, pods[podNumber]):
                        reportingService.report_results(pods[podNumber], choice)

                    else:
                        print("Error: please enter a valid table number, 'm' to go back to the menu or 'f' to "
                              "finish the round.")
            except IndexError:
                print("Error: Please create a pod first.")

        # Switch to next Pod
        elif option == '2':
            try:
                if (len(pods) - 1) == podNumber:
                    podNumber = 0
                else:
                    podNumber += 1

                printService.print_pairings(pods[podNumber])
            except IndexError:
                print("Error: Please create a pod first.")

        # Show Standings of current Pod 
        elif option == '3':
            try:
                printService.print_standings(pods[podNumber])
            except IndexError:
                print("Error: Please create a pod first.")

        # Add Pod
        elif option == '4':
            print("Add pod")
            init_new_pod()

        # Show seatings
        elif option == '5':
            try:
                printService.print_table(pods[podNumber])
            except IndexError:
                print("Error: Please create a pod first.")

        # create multi-draft pod
        elif option == '6':
            print("Add multi-draft pod")
            init_new_multi_pod()

        # Default / CatchAll
        else:
            print("* Please choose from Options                                            *")


def init_new_pod():
    pods.append(Pod())
    pods[len(pods) - 1].load_players()
    pods[len(pods) - 1].randomize_seating()
    pods[len(pods) - 1].new_pairings()


def init_new_multi_pod():
    pods.append(MultiPod(ROUND_NUMBER, DRAFT_AMOUNT))
    pods[len(pods) - 1].load_players()
    pods[len(pods) - 1].randomize_seating()
    pods[len(pods) - 1].new_pairings()


if __name__ == "__main__":
    main()
