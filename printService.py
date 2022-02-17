import copy
from operator import getitem
from collections import OrderedDict


class PrintService(object):

    @staticmethod
    def print_pairings(pod):
        print('************************ PAIRINGS FOR ROUND %s ************************' % pod.roundNumber)
        for table in pod.currentPairings:
            player1 = pod.playerList[1][pod.playerList[0].index(pod.currentPairings[table][0])]
            player2 = pod.playerList[1][pod.playerList[0].index(pod.currentPairings[table][1])]
            result = pod.current_results[table - 1]
            print('* Table %s:  %s \t - %s \t | \t %s                        ' % (table, player1, player2, result))
        print('**********************************************************************')
        print("")

    @staticmethod
    def print_standings(to, pod):
        print('\nxxxxxxxxxxxxxxxxxxxxxxxx STANDINGS AFTER ROUND %s xxxxxxxxxxxxxxxxxxxxxxx' % pod.roundNumber)
        print('   Name  \tPoints     \tOMW')

        standingsDict = copy.deepcopy(to.playersDict)
        standingsDict = OrderedDict(sorted(standingsDict.items(), reverse=True, key=lambda x: getitem(x[1], 'OMW%')))
        standingsDict = OrderedDict(sorted(standingsDict.items(), reverse=True, key=lambda x: getitem(x[1], 'Points')))
        counter = 1
        for players in standingsDict:
            tempName = standingsDict[players]['Name']
            tempPoints = standingsDict[players]['Points']
            tempOMW = standingsDict[players]['OMW%'][0:6]
            print('%s. %s \t %s \t\t %s' % (counter, tempName, tempPoints, tempOMW))
            counter += 1
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    @staticmethod
    def print_welcome():
        print('**********************************************************************')
        print('*               WELCOME TO THE HAMBURG TOURNAMENT MAKER              *')
        print('**********************************************************************')

    @staticmethod
    def print_table(pod):

        local_playerList = pod.playerList[1]
        iter_forward = 0
        iter_backward = len(local_playerList) - 1

        print('*************************** SEATINGS *********************************')
        while iter_forward < iter_backward - 1:
            if iter_forward == 0:
                print('* \n*\t\t\t %i. %s ' % ((iter_forward + 1), local_playerList[iter_forward]))
                print('*\t\t\t   _____')
                print('*\t\t\t  /     \\')
                iter_forward += 1
            else:
                print('*\t %i. %s \t  |     |\t %i. %s ' % (
                    (iter_backward + 1), local_playerList[iter_backward], (iter_forward + 1),
                    local_playerList[iter_forward]))
                print("* \t\t\t  |     | ")
                iter_forward += 1
                iter_backward -= 1

        print('*\t\t\t  \\_____/')
        print('*\n*\t\t\t %i. %s ' % ((iter_backward + 1), local_playerList[iter_backward]))
        print('*')
