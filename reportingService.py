from printService import PrintService

printService = PrintService()


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
                print(
                    "Error: Invalid input. Input must either be a table number from above or q to finish inputting "
                    "results.")
        # Finish Round
        elif choice == 'f':
            pod.new_pairings()
            pod.roundNumber += 1
            printService.print_standings(pod)

        return choice