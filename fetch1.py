from indodax import indodax
from datetime import datetime
import pickle
import sys
  
# Open the file in binary mode
with open('cred.pkl', 'rb') as file:      
    # Call load method to deserialze
    mycred = pickle.load(file)
  
dax = indodax(mycred['key'],mycred['secret'])

if len(sys.argv)<2:
    print("Market not defined")
    exit()
else:
    market = sys.argv[1]

data = indodax.get_price(market)

# 'server_time', 'high', 'low', 'vol_btc', 'vol_idr', 'last', 'buy', 'sell'
print(datetime.fromtimestamp(data['ticker']['server_time']), "\t", 
    data['ticker']['last'],"\t",
    data['ticker']['high'],"\t",
    data['ticker']['low'],"\t",
    data['ticker']['vol_btc'],"\t",
    data['ticker']['vol_idr'],"\t",
    data['ticker']['last'],"\t",
    data['ticker']['buy'],"\t",
    data['ticker']['sell'])
