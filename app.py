print("TX-RX data of the 192.168.0.1 OpenWRT Gateway Archer C6\n")

from functions import *
from time import sleep
from env import update_interval

if update_interval == (None):
    print("You must create the .env file with the config")
    error = True
else:
    error = False

while error == False:

    new_tx=0
    new_rx=0
    actual_tx=0
    actual_rx=0

    connection = False
    while connection == False:
        values = get_tx_rx()
        
        actual_tx=values[0]
        actual_rx=values[1]

        print(values)
        if values == ('0', '0'):
            print(values)
            connection = False
        elif actual_tx == 0:
            print("TX ES 0. Reintentando...")
        elif actual_rx == 0:
            print("RX ES 0. Reintentando...")
        
        else:
            print(values)
            connection = True
        sleep(0.5)

    


    try:
        last_value = get_last_value()
        last_value=last_value[0]
    except IndexError:
        last_value=(0, '0', '0', '0', '0', (0, 0, 0, 0, 0, 0))
        print("IndexError")
    except Exception as e:
        print(f"ERROR: {e}")

    last_tx = int(last_value[1])
    last_rx = int(last_value[2])

    last_actual_tx = int(last_value[3])
    last_actual_rx = int(last_value[4])


    print(f"Last TX: {last_tx}. Last RX: {last_rx}")

    print(f"Last Actual TX: {last_actual_tx}. Last Actual RX: {last_actual_rx}")

    print(f"Actual TX: {actual_tx}. Actual RX: {actual_rx}")


    if last_actual_tx > actual_tx:
        new_tx = last_tx+actual_tx

    else:
        new_tx=actual_tx-last_actual_tx

        new_tx=new_tx+last_tx
        

    if last_actual_rx > actual_rx:
        new_rx = last_rx+actual_rx

    else:
        new_rx=actual_rx-last_actual_rx

        new_rx=new_rx+last_rx


    #print(f"New TX: {new_tx}. New RX: {new_rx}\n")


    #TEST ONLY VALUES:
    #new_tx=57483338942
    #new_rx=3675348758454
    #actual_tx=0
    #actual_rx=0

    send_to_db(new_tx,new_rx,actual_tx,actual_rx)

    #send_to_db(tx,rx,actual_tx,actual_rx)

    sleep(update_interval)
