#pip3 install paramiko

import paramiko
from env import openwrt_ip, openwrt_user, openwrt_password, openwrt_interface

#client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


error = False

#------------------GET OUTPUT COMMANDS FUNCTION------------------
def get_output(command):
    # initialize the SSH client
    error = False
    
    connection = False

    while connection == False:

        try:
            client.connect(hostname=openwrt_ip, username=openwrt_user, password=openwrt_password, look_for_keys=False)
            error = False
            print("CONNECTION TRUE")
        except:
            print("[!] Cannot connect to the SSH Server")
            error = True

        if error == False:
            try:
                stdin, stdout, stderr = client.exec_command(command)
                output = (stdout.read().decode())
                connection = True
                return output
                #err = stderr.read().decode()
                #if err:
                #   print(err)
            except:
                return "Error"
        else:
            connection=False
            print("Connection FALSE")
            return "[!] Cannot connect to the SSH Server"

def get_rx():
    command = r"""ifconfig {0} | awk '/RX bytes/ {{split($2, a, ":"); print a[2]}}'""".format(openwrt_interface)
    output = get_output(command)
    return output

def get_tx():
    command = r"""ifconfig {0} | awk '/TX bytes/ {{split($6, a, ":"); print a[2]}}'""".format(openwrt_interface)
    output = get_output(command)
    return output

#def get_tx_rx():
#    output = get_output("ash /root/scripts/wan_tx_rx.sh")
#    return output
