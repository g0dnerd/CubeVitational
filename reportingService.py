from printService import PrintService
import re

printService = PrintService()


# input validation for results, which have to be in a "W-L-D" formatting. None of the numbers can be larger than 2.
def is_legal_result(result_):
    # use regex to find all numbers in the result
    numbers_in_result = re.findall(r'\d+', result_)
    total_numbers = 0

    for numbers in numbers_in_result:
        total_numbers += int(numbers)

    if len(result_) != 5:
        print("Invalid result!")
        return False
    elif any(number > 2 for number in numbers_in_result):
        print("Invalid result!")
        return False
    elif any(number < 0 for number in numbers_in_result):
        print("Invalid result!")
        return False
    elif total_numbers > 3 or total_numbers < 1:
        print("Invalid result!")
        return False
    else:
        print("Valid result!")
        return True


def is_legal_table(table, pod):
    table = int(table)
    if table < 1 or table >= len(pod.current_results):
        return False
    else:
        return True


def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


def report_results(pod, table):
    tableNumber = get_nth_key(pod.currentPairings, int(table) - 1)
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
