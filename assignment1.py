"""
FIT2004 2022 semester 2 assignment 1
Diabro Immoral Gacha (DIG)
"""

__author__ = "Pin Hen Song"

from typing import List
from math import pow

def analyse(results: List[List], roster: int, score: int) ->List[List]:
    """
    :input:
        arg1: results, list of matches 
        arg2: roster, length of character set
        arg2: score, target score
    :return: [top10matches, searchedmatches]
    :time complexity: O(NM), dominant by sort_all_team(), radix_sort_ABC(), search_matches() and find_top10()
    :aux space complexity: O(NM)

    >>> results = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36],
    ...             ['BAB', 'BAB', 36], ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49], ['BBA', 'ABB', 55],
    ...             ['AAB', 'AAA', 58], ['ABA', 'AAA', 46], ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
    ...             ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30], ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]
    >>> analyse(results, 2, 64)
    [[['ABB', 'AAB', 70], ['ABB', 'BBB', 68], ['AAB', 'BBB', 67], ['AAB', 'AAB', 65], ['AAB', 'AAA', 64], ['ABB', 'ABB', 64], ['AAA', 'AAA', 62], ['AAB', 'AAA', 58], ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]], [['AAB', 'AAA', 64], ['ABB', 'ABB', 64]]]

    >>> results = [['AAB', 'AAB', 35],['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36],
    ...             ['BAB', 'BAB', 36], ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49], ['BBA', 'ABB', 55],
    ...             ['AAB', 'AAA', 58], ['ABA', 'AAA', 46], ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
    ...             ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30], ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]
    >>> analyse(results, 2, 63)
    [[['ABB', 'AAB', 70], ['ABB', 'BBB', 68], ['AAB', 'BBB', 67], ['AAB', 'AAB', 65], ['AAB', 'AAA', 64], ['ABB', 'ABB', 64], ['AAA', 'AAA', 62], ['AAB', 'AAA', 58], ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]], [['AAB', 'AAA', 64], ['ABB', 'ABB', 64]]]

    >>> results = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36],
    ...             ['BAB', 'BAB', 36], ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49], ['BBA', 'ABB', 55],
    ...             ['AAB', 'AAA', 58], ['ABA', 'AAA', 46], ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
    ...             ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30], ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]
    >>> analyse(results, 2, 71)
    [[['ABB', 'AAB', 70], ['ABB', 'BBB', 68], ['AAB', 'BBB', 67], ['AAB', 'AAB', 65], ['AAB', 'AAA', 64], ['ABB', 'ABB', 64], ['AAA', 'AAA', 62], ['AAB', 'AAA', 58], ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]], []]

    >>> results = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36],
    ...             ['BAB', 'BAB', 36], ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49], ['BBA', 'ABB', 55],
    ...             ['AAB', 'AAA', 58], ['ABA', 'AAA', 46], ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
    ...             ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30], ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]
    >>> analyse(results, 2, 0)
    [[['ABB', 'AAB', 70], ['ABB', 'BBB', 68], ['AAB', 'BBB', 67], ['AAB', 'AAB', 65], ['AAB', 'AAA', 64], ['ABB', 'ABB', 64], ['AAA', 'AAA', 62], ['AAB', 'AAA', 58], ['ABB', 'ABB', 58], ['AAB', 'ABB', 57]], [['AAB', 'ABB', 30]]]
    """

    #sort team name in lexicographical order
    sort_all_team(results, roster) #O(NM)

    #sort according to team 
    results = radix_sort_ABC(results, roster, 0) #O(NM)
    results = radix_sort_ABC(results, roster, 1) #O(NM)

    #find matches that that has score that bigger or equal and closest to target score 
    searchedmatches = search_matches(results, score) #O(NM)

    #find top 10 team
    top10matches = find_top10(results) #O(NM)

    return [top10matches, searchedmatches]

def sort_all_team(results: List[List], roster: int):
    """
    sort team name of all matches in lexicographical order

    :input:
        arg1: results, results of matches 
        arg2: roster, number of possible letters
    :time complexity: 
        O(NM), loop through matches cost N, and count sort each team name cost M
        where N is number of matches, i.e. len(results), M is number of character of team
    :aux space complexity: O(M), dominant by count_sort_team_char()

    """
    for match in range(len(results)): #O(N)
        for team in range(2): #team1 & team2 O(1)
            results[match][team] = count_sort_team_char(results[match][team], roster) #sort team name, O(M)

def count_sort_team_char(team: str, roster: int) -> str:
    """
    sort matches by team name in lexicographical order

    :input:
        arg1: team, team name
        arg2: roster, number of possible letters
    :return: sorted team name
    :time complexity: O(M), where M is number of character of team, i.e. len(team)
    :aux space complexity: O(M), which is dominant by the size of "output"
    """

    count = [0]*roster #O(r) = O(1)
    position = [0]*roster #O(r) = O(1)
    output = [0]*len(team) #O(M)

    #count
    for char in team: #O(M)
        count[ord(char)-65] += 1 #store letter value in number
            
    #position
    for i in range(1,roster): #O(r) = O(1)
        position[i] = count[i-1] + position[i-1]

    #output
    for i in range(len(team)): #O(M)
        key = ord(team[i])-65 #transform key back to letter
        output[position[key]] = chr(key+65) 
        position[key] += 1 #increase position 
    
    return ''.join(output) #O(M)

def search_matches(results: List[List], score) -> List:
    """
    find matches in results which score bigger or equal to target score

    :input:
        arg1: results, results of matches 
        arg2: roster, number of possible letters
    :return: list of matches which score bigger or equal than target score
    :time complexity: 
        O(NM), loop through matches cost N and copy team cost M
        where N is number of matches i.e. len(results), M is number of character of team, i.e. len(team)
    :aux space complexity: 
        dominant by the size of "searchedmatches", 
        worse case scenario: all matches matches the score, hence O(NM)
    """
    searchedmatches = [] #return list
    min_diff = 100 #difference between match score and target score
    results = radix_sort_123(results)

    #find minimum score difference 
    for match in results: #O(N)
        diff = match[2] - score #calculate score difference 
        if diff>=0 and diff < min_diff:
            min_diff = diff
        diff = 100 - match[2] - score
        if diff>=0 and diff < min_diff:
            min_diff = diff

    for match in results: #O(N) 
        #case where flipping score and team is not needed
        if match[2] - score == min_diff:
            #add to return list if resturn list is empty or it's not duplicated match
            if not searchedmatches or match != searchedmatches[len(searchedmatches)-1]: #O(2M) = O(M), compare 2 team
                searchedmatches.append(match.copy()) #O(M), copy() cost M
                
        #case where flipping score and team is needed
        if 100 - match[2] - score == min_diff:
            match[0], match[1] = match[1], match[0]
            match[2] = 100 - match[2]
            if not searchedmatches or match != searchedmatches[len(searchedmatches)-1]: #O(2M) = O(M), compare 2 team
                searchedmatches.append(match.copy())  #O(M), copy() cost M

    return searchedmatches


def find_top10(results: List[List]) -> List:
    """
    find top 10 highest score matches

    :input:
        arg1: results, results of matches 
    :return: list of top 10 highest score matches
    :time complexity: 
        O(NM), loop through "results" cost N, copy team cost M
        where N is number of matches i.e. len(results) and M is number of character of team, i.e. len(team)
    :aux space complexity: O(10*M) = O(M), dominant by the size of "top10matches"
    """

    flip_all_team_score(results, False) #O(N)
    results = radix_sort_123(results) #O(N)

    #flip all team's score to > 50 and find top 10 team
    top10matches = []
    for i in range(len(results)): #O(N)
        if len(top10matches) >= 10:
            break
        elif not top10matches or results[i] != top10matches[len(top10matches)-1]: #O(2M), compare 2 team
            top10matches.append(results[i].copy()) #O(M), copy cost M
    
    #if len(top10matches) < 10, flip all team score to <50,
    #and append top score matches to top10matches until top 10 mathches is found
    if len(top10matches)<10:
        flip_all_team_score(results, True)
        for i in range(len(results)-1,-1,-1): #O(N)
            if len(top10matches) >= 10:
                break
            elif not top10matches or results[i] != top10matches[len(top10matches)-1]: #O(2M), compare 2 team
                top10matches.append(results[i].copy()) #O(M), copy() cost M
    

    return top10matches

def flip_all_team_score(results, below_50: bool = False)->List:
    """
    flip score of all team to below 50 or above 50

    :input:
        arg1: results, results of matches 
        arg2: below_50, if true, flip all team score to below 50, else above 50
    :return: list of top 10 highest score matches
    :time complexity: O(N), loop through "results" cost N, where N is number of matches i.e. len(results)
    :aux space complexity: O(M) for swapping team
    """

    for match in range(len(results)): #O(N)
        score = results[match][2]
        #(if score is >=50 and target score is <50) or (score is <= 50 and target score is not < 50)
        if (score>=50 and below_50) or (score<50 and not below_50):
            results[match][0], results[match][1] = results[match][1], results[match][0] #swap team position
            results[match][2] = 100 - score #flip score 

def radix_sort_ABC(results: List[List], roster: int, col: int):
    """
    sort matches by col-th team in lexicographical order

    :input:
        arg1: results, results of matches 
        arg2: roster, number of possible letters
        arg3: col, index of column to sort
    :return: "results" with sorted col-th column in lexicographical order
    :time complexity: 
        O(MN), count sort cost N and repeat count sort M times
        where M is the number of character of team, i.e. len(team), N is number of matches i.e. len(results)
    :aux space complexity: O(NM), which is dominant by the size of "output"
    """
    output = [0]*len(results)

    #access every letter
    for letter in range(len(results[0])-1,-1,-1): #O(M)
        count = [0]*roster #O(1)
        position = [0]*roster #O(1)

        #count
        for row in range(len(results)): #O(N)
            char = results[row][col][letter]
            count[ord(char)-65]+=1

        #position
        for i in range(1,roster): #O(1)
            position[i] = position[i-1] + count[i-1]
        
        #output
        for row in range(len(results)): #O(N)
            key = ord(results[row][col][letter])-65
            output[position[key]] = results[row]
            position[key] += 1
    
        results = output.copy() #update results, O(N)
    
    return output


def radix_sort_123(results: List[List], col: int =2) -> List:
    """
    sort matches by score in descending order

    :input:
        arg1: results, results of matches 
        arg2: roster, number of possible letters
        arg3: col, index of column to sort
    :return: list of matches which sorted according to score
    :time complexity: 
        O(N), count sort cost N where N is number of matches i.e. len(results)
    :aux space complexity: O(NM) dominant by the size of "output", where M is number of character of team, i.e. len(team)
    """
    roster = 10
    output = [0]*len(results)

    
    for kth_dgt in range(3): #assume largest possible number of digit is 3, i.e. 100
        count = [0]*roster
        position = [0]*roster

        #count
        for row in range(len(results)): #O(N)
            num = int(results[row][col]//pow(10,kth_dgt)%10) #access kth digit and count
            count[num]+=1

        #position
        for i in range(roster-1-1, -1, -1):
            position[i] = position[i+1] + count[i+1]
        
        #output
        for row in range(len(results)): #O(N)
            key = int(results[row][col]//pow(10,kth_dgt)%10)
            output[position[key]] = results[row]
            position[key] += 1
    
        results = output.copy() #update results, O(N)
    
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
