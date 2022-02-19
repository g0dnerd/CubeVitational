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
            result = pod.currentResults[table - 1]
            print('* Table %s:  %s \t - %s \t | \t %s                        ' % (table, player1, player2, result))
        print('**********************************************************************')
        print("")

    @staticmethod
    def print_standings(pod):
        from pod import MultiPod
        if not issubclass(type(pod), MultiPod):
            print('\nxxxxxxxxxxxxxxxxxxxxxxxx STANDINGS AFTER ROUND %s xxxxxxxxxxxxxxxxxxxxx' % pod.roundNumber)
        else:
            if pod.draftNumber > 1:
                print('\nxxxxxxxxxxxxxxxxxxxxxxxx STANDINGS AFTER ROUND %s xxxxxxxxxxxxxxxxxxxxx'
                      % pod.roundNumber + pod.roundNumber * pod.draftNumber)
            else:
                print('\nxxxxxxxxxxxxxxxxxxxxxxxx STANDINGS AFTER ROUND %s xxxxxxxxxxxxxxxxxxxxx' % pod.roundNumber)
        print('   Name  \tPoints     \tOMW')

        standingsDict = copy.deepcopy(pod.to.playersDict)
        standingsDict = OrderedDict(sorted(standingsDict.items(), reverse=True, key=lambda x: getitem(x[1], 'OMW%')))
        standingsDict = OrderedDict(sorted(standingsDict.items(), reverse=True, key=lambda x: getitem(x[1], 'Points')))
        counter = 1
        for players in standingsDict:
            tempName = standingsDict[players]['Name']
            tempPoints = standingsDict[players]['Points']
            tempOMW = standingsDict[players]['OMW%']
            print('%s. %s \t %s \t\t %s' % (counter, tempName, tempPoints, tempOMW))
            counter += 1
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    @staticmethod
    def print_welcome():
        print('**********************************************************************')
        print('*               WELCOME TO THE HAMBURG TOURNAMENT MAKER              *')
        print('**********************************************************************')

    @staticmethod
    def print_menu(podNumber, amountPods):
        print('******************************* MENU *********************************')
        print('*                                                                    *')
        print('* 1. Start/Resume Round of current Pod   2. Switch to next Pod       *')
        print('*                                                                    *')
        print('* 3. Show Standings of current Pod       4. Add Pod                  *')
        print('*                                                                    *')
        print('* 5. Show Seatings                       6. Add multi-draft pod      *')
        print('*                                                                    *')
        print('* 7. Cut multi-pods for Top8             8. Exit                     *')
        print('*                    (Current Pod: %i from %i Pods)                    *' % (podNumber + 1, amountPods))
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

    @staticmethod
    def print_merged_standings(pods_):
        pod1 = pods_[0]
        pod2 = pods_[1]
        all_players_dict = {**pod1.to.playersDict, **pod2.to.playersDict}
        print('\nxxxxxxxxxxxxxxxxxxxxxxxx FINAL STANDINGS xxxxxxxxxxxxxxxxxxxxx')
        print('   Name  \tPoints     \tOMW')

        all_players_dict = OrderedDict(sorted(all_players_dict.items(),
                                              reverse=True, key=lambda x: getitem(x[1], 'OMW%')))
        all_players_dict = OrderedDict(sorted(all_players_dict.items(),
                                              reverse=True, key=lambda x: getitem(x[1], 'Points')))
        counter = 1
        for players in all_players_dict:
            tempName = all_players_dict[players]['Name']
            tempPoints = all_players_dict[players]['Points']
            tempOMW = all_players_dict[players]['OMW%']
            print('%s. %s \t %s \t\t %s' % (counter, tempName, tempPoints, tempOMW))
            counter += 1
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
