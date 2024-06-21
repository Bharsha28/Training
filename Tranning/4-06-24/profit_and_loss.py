prices=list(map(int,input().split()))
if len(prices)<2:
           print( 0)
min1=prices[0]
profit=0
for j in range(1,len(prices)):
    curr_profit=prices[j]-min1
    profit=max(curr_profit,profit)
    min1=min(min1,prices[j])
print(profit)
