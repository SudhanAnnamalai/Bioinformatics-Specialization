# @execute python DPChange.py <money> <coins(comma separated)>

import sys

money = int(sys.argv[1])
coi = sys.argv[2].split(",")
coins = [int(i) for i in coi]

def DPChange(money, Coins):
        #Takes the amount - money, Coins - list of allowed coins
    MinNumCoins=[0 for i in range(money+1)]
    #MinNumCoins - Empty placeholder at the size of amount
    for m in range(1,money):
        MinNumCoins[m]=float('inf')
        for i in range(0,len(Coins)-1):
            if m>=Coins[i]:
                if MinNumCoins[m-Coins[i]]+1<MinNumCoins[m]:
                    MinNumCoins[m]=MinNumCoins[m-Coins[i]]+1
    print(MinNumCoins)
    return MinNumCoins[money-1]
    
DPChange(money,coins)

