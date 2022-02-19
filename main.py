from printService import PrintService
import reportingService
from pod import Pod, MultiPod, TrackingPod

# USER-DEFINED VARIABLES
ROUND_NUMBER = 3
DRAFT_AMOUNT = 2

# Define Classes 
printService = PrintService()
pods = []
tracking_pods = []


###################### Start Application  ######################
def main():
    # Welcome and Init
    printService.print_welcome()
    podNumber = 0
    trackingPodNumber = 0

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
                        if not issubclass(type(pods[podNumber]), MultiPod):
                            pods[podNumber].new_pairings()
                            pods[podNumber].roundNumber += 1
                            printService.print_standings(pods[podNumber])
                        else:
                            # if the current pod is a multi-pod draft, but not in its final round yet, proceed as usual
                            if pods[podNumber].roundNumber < pods[podNumber].roundsAmount:
                                tracking_pods[trackingPodNumber].shadow_results(pods[podNumber])
                                pods[podNumber].new_pairings()
                                pods[podNumber].roundNumber += 1
                                tracking_pods[trackingPodNumber].shadow_pairings(pods[podNumber])
                                printService.print_standings(tracking_pods[trackingPodNumber])

                            # if a draft in the pod is finished, reset the multi-pod
                            elif pods[podNumber].draftNumber < DRAFT_AMOUNT:
                                tracking_pods[trackingPodNumber].shadow_results(pods[podNumber])
                                printService.print_standings(tracking_pods[trackingPodNumber])
                                pods[podNumber].reset_pod()
                                pods[podNumber].new_pairings()
                                tracking_pods[trackingPodNumber].shadow_pairings(pods[podNumber])

                            else:
                                tracking_pods[trackingPodNumber].shadow_results(pods[podNumber])
                                printService.print_standings(tracking_pods[trackingPodNumber])
                                break

                    # if a legal table number was entered, report the result
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
                    trackingPodNumber = 0
                else:
                    podNumber += 1
                    trackingPodNumber += 1

                printService.print_pairings(pods[podNumber])

            except IndexError:
                print("Error: Please create a pod first.")

        # Show Standings of current Pod 
        elif option == '3':
            try:
                if not issubclass(type(pods[podNumber]), MultiPod):
                    printService.print_standings(pods[podNumber])
                else:
                    printService.print_standings(tracking_pods[trackingPodNumber])
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
            tracking_pods[len(tracking_pods) - 1].shadow_playerlist(pods[len(pods) - 1])
            tracking_pods[len(tracking_pods) - 1].shadow_pairings(pods[len(pods) - 1])

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
    tracking_pods.append(TrackingPod())
    pods[len(pods) - 1].load_players()
    pods[len(pods) - 1].randomize_seating()
    pods[len(pods) - 1].new_pairings()


if __name__ == "__main__":
    main()
