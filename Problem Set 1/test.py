# -*- coding: utf-8 -*-
"""
Created on Tue May 08 11:23:58 2018

@author: Dell XPS
"""
def greedy_cow_transport(cows,limit=10):
    trips = []
    cowsCopy = cows.copy()
    sortedCows = sorted(cowsCopy.items(), key=lambda x: x[1], reverse = True)
    while sum(cowsCopy.values()) > 0:
        ship = []
        total = 0
        for cow, value in sortedCows:
            if cowsCopy[cow] != 0 and value + total <= limit:
                ship.append(cow)
                total += value
                cowsCopy[cow] = 0       # use 0 as a flag setter
        trips.append(ship)
    return trips


print greedy_cow_transport({'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}, 10)