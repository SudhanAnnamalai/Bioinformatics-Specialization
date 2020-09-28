# @ exec python GreedyChange.py <Money>
'''
The heuristic used by cashiers all over the world to make change, which we call GreedyChange, iteratively selects the largest coin denomination possible'''
import sys
Money = sys.argv[1]

def GreedyChange(money):
    change = []
    coins = [1,2,5,10,50,100,500,2000]
    while money>0:
        coin = max([i for i in coins if i<=money])
        change.append(coin)
        money = money-coin
    return change

GreedyChange(Money)
