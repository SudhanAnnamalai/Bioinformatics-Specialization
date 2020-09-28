# @execute python RecursiveChange.py <money> <coins(comma separated)>

import sys

money = int(sys.argv[1])
coi = sys.argv[2].split(",")
coins = [int(i) for i in coi]

def RecursiveChange(money,coins):
    if money==0:
        return 0
    MinNumCoins = float('inf')
    for i in range(0,len(coins)-1):
        if money>=coins[i]:
            NumCoins = RecursiveChange(money-coins[i],coins)
            if NumCoins+1<MinNumCoins:
                MinNumCoins = NumCoins+1
    return MinNumCoins
    
RecursiveChange(76,coins)
