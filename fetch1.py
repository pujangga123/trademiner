from indodax import indodax
import time
from datetime import datetime
import pickle
  
# Open the file in binary mode
with open('cred.pkl', 'rb') as file:      
    # Call load method to deserialze
    mycred = pickle.load(file)
  
dax = indodax(mycred['key'],mycred['secret'])

while True:
    data = indodax.get_price('btc')
    print(datetime.fromtimestamp(data['ticker']['server_time']), "\t", data['ticker']['last'])
    time.sleep(900)