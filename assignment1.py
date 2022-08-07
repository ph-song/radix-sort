"""
FIT2004 2022 semester 2 assignment 1
Diabro Immoral Gacha (DIG)
"""

__author__ = "Pin Hen Song"

from curses.ascii import isalpha
from operator import index
import re
from typing import List
from string import ascii_uppercase
from unittest import result
from math import pow

from sklearn.utils import resample

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
    :precondition: score <= 100
    """

    #sort team name in lexicographical order
    results = count_sort_team(results, roster)
    results = swap_team_score(results, roster)

    #sort according to score & team 
    results = radix_sort_ABC(results, roster, 0)
    results = radix_sort_ABC(results, roster, 1)

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
            results[match][team] = count_sort_team_char(results[match][team], roster) #sort name, O(M)
            #print(results[match][team])
    """
    #reverse order
    for match in range(len(results)):
        if results[match][2]<50:
            results[match][0], results[match][1] = results[match][1], results[match][0]
            results[match][2] = 100 - results[match][2]
    """

def swap_team_score(results):
    for match in range(len(results)):
        if results[match][2]<50:
            results[match][0], results[match][1] = results[match][1], results[match][0]
            results[match][2] = 100 - results[match][2]

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

def radix_sort_ABC(results: List[List], roster: int, col: int):
    """
    sort col-th team in lexicographical order

    :input:
        arg1: results
        arg2: roster
        arg3: column to sort
    :output, return or postcondition:
    :time complexity: 
    :aux space complexity:
    """
    output = [0]*len(results)

    for kth_dgt in range(len(results[0])-1,-1,-1): #O(M)
        count = [0]*roster
        position = [0]*roster

        #count
        for row in range(len(results)): #O(N)
            char = results[row][col][kth_dgt]
            count[ord(char)-65]+=1

        #position
        for i in range(1,roster): #O(r)
            position[i] = position[i-1] + count[i-1]
        
        #output
        for row in range(len(results)): #O(N)
            key = ord(results[row][col][kth_dgt])-65
            output[position[key]] = results[row]
            position[key] += 1
    
        results = output.copy() #O(N)*****
    
    return output


def radix_sort_123(results: List[List], col: int =2):
    """
    sort score in lexicographical order

    :input:
        arg1: results
        arg2: roster
        arg3: column to sort
    :output, return or postcondition:
    :time complexity: 
    :aux space complexity:
    """
    roster = 10
    output = [0]*len(results)

    for kth_dgt in range(2): #O(M) ***assume max score 50 - 00
        count = [0]*roster
        position = [0]*roster

        #count
        for row in range(len(results)): #O(N)
            num = int(results[row][col]//pow(10,kth_dgt)%10) #******int() complexity
            count[num]+=1


        #position
        for i in range(roster-1-1, -1, -1): #O(r)
            position[i] = position[i+1] + count[i+1]
        
        #output
        for row in range(len(results)): #O(N)
            key = int(results[row][col]//pow(10,kth_dgt)%10)
            output[position[key]] = results[row]
            position[key] += 1 #-=***
    
        results = output.copy() #O(N)*****
    
    return output

if __name__ == "__main__":
    roster = 2
    a = 'BAA'


    results = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
                ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
                ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
                ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
                ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
                ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
                ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]

    #results = [['AAB', 'BBA', 50], ['ABB', 'BBB', 53], ['BAB', 'BBB', 52]]

    count_sort_team(results,roster)
    swap_team_score(results)
    #print(results)
    results = radix_sort_ABC(results, 2, 1)
    results = radix_sort_ABC(results, 2, 0)
    results = radix_sort_123(results, 2)
    print(results)

