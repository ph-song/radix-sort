"""
FIT2004 2022 semester 2 assignment 1
Diabro Immoral Gacha (DIG)
"""

__author__ = "Pin Hen Song"

from operator import index
from typing import List
from string import ascii_uppercase
from unittest import result


#N is the number of matches within results.
#M is the number of characters within a team for each match.


def analyze(results: List[List], roster: int, score: int):
    """
    :input:
        arg1:
        arg2:
    :output, return or postcondition:
    :time complexity:
    :aux space complexity:
    """

    #sort team name in lexicographical order
    results = count_sort_team(results, roster)


    #sort according to score, then team 

    #find top 10 team

    #find matches that score >= score


    pass

def count_sort_team(results: List[List], roster: int) -> None:
    """
    sort all team name in lexicographical order

    :input:
        arg1: results
        arg2: roster
    :return:
    :time complexity:
    :aux space complexity:

    e.g.
    count_sort_team([['BBAC','CCCA',43], ['BACB','CACB',83], ['CBAC','BCCA',21]], 3)
    >>>[['ABBC', 'ACCC', 43], ['ABBC', 'ABCC', 83], ['ABCC', 'ABCC', 21]]
    """
    for match in range(len(results)): #O(N)
        for team in range(2):
            #print(results[match][team], end = ' ')
            results[match][team] = count_sort_team_char(results[match][team], roster) #sort name
            #print(results[match][team])

    for match in range(len(results)):
        if results[match][2]<50:
            results[match][0], results[match][1] = results[match][1], results[match][0]
            results[match][2] = 100 - results[match][2]

    return results

def count_sort_team_char(team: str, roster: int) -> str:
    """
    sort team name in lexicographical order

    :input:
        arg1: team
        arg2: roster
    :output, return or postcondition:
    :time complexity:
    :aux space complexity:

    e.g.
    sort_team('BDA')
    >>>'ABD'
    """
    #r = roster, M = len(team)

    count = [0]*roster #O(r)
    position = [0]*roster #O(r)
    output = [0]*len(team) #O(M)

    #count
    for char in team: #O(M)
        count[ord(char)-65] += 1 #complexity of ord()?

    #position
    for i in range(1,roster): #O(r)
        position[i] = count[i-1] + position[i-1]

    #output
    for i in range(len(team)): #O(M)
        key = ord(team[i])-65
        output[position[key]] = chr(key+65)
        position[key] += 1
    
    return ''.join(output)

def radix_sort(results: List[List], roster: int, index_to_sort: int):
    """
    
    """
    pass

    

if __name__ == "__main__":
    roster = 2
    a = 'BAA'
    print(count_sort_team_char(a,roster))


    results = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
                ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
                ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
                ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
                ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
                ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
                ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]
    
    count_sort_team(results,roster)
    print(results)

