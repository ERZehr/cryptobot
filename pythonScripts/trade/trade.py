import sys # for arguments
import buy as buy
import sell as sell

Asset = sys.argv[1]
Quantity = sys.argv[2]
Action = sys.argv[3]
Type = sys.argv[4]
if(sys.argv[4] != "market_order"):
    Line = sys.argv[5]
User = sys.argv[6]

if(Action == "buy"):
    if(Type == "market_order"):
        buy.marketOrder(Asset, Quantity, User)
    elif(Type == "market_order_cash"):
        buy.marketOrderCash(Asset, Quantity, User)
    elif(Type == "limit_order"):
        buy.limitOrder(Asset, Quantity, Line, User)
    elif(Type == "stop_order"):
        buy.stopOrder(Asset, Quantity, Line, User)
    else:
        exit

elif(Action == "sell"):
    if(Type == "market_order"):
        sell.marketOrder(Asset, Quantity, User)
    elif(Type == "market_order_cash"):
        sell.marketOrderCash(Asset, Quantity, User)
    elif(Type == "sell_all"):
        sell.sellAll(Asset, User)
    elif(Type == "limit_order"):
        sell.limitOrder(Asset, Quantity, Line, User)
    elif(Type == "stop_order"):
        sell.stopOrder(Asset, Quantity, Line, User)
    else:
        exit

else:
    exit
