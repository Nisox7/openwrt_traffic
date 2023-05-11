from tx_rx import get_tx, get_rx
from bbdd import *


def get_tx_rx():
    try:
        tx = get_tx()
        tx = tx.replace("\n","")
        tx=int(tx)
    except:
        print("Error obteniendo TX")
        tx="0"

    try:
        rx = get_rx()
        rx = rx.replace("","")
        rx=int(rx)
    except:
        print("Error obteniendo RX")
        rx="0"
    
    #last_value = get_last_value()

    #last_tx=last_value[0][1]
    #last_rx=last_value[0][2]
    
    return tx,rx



def send_to_db(tx,rx,actual_tx,actual_rx):

    #print(f"tx: {tx}, rx: {rx}\nactual_tx: {actual_tx}, actual_rx: {actual_rx}")

    write_db(tx,rx,actual_tx,actual_rx)