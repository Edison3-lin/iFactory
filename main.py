import os
import socket
from urllib import parse
import pickle
import json
import subprocess
import time
import requests
import codecs
import iFactory.iDB as DB
import iFactory.i2_send as MQ_send
import pika, sys
import iFactory.email as email

status1 = ['alive', 'stop'] 
status2 = ['alive', 'disconnect', 'send fail', 'queue fail'] 
type3 = ['collector', 'wsgi', 'monitor'] 
status4 = ['data path change', 'device stop'] 
status5 = ['alive', 'disconnect', 'send fail', 'queue fail'] 
ret_list1 = []
ret_list2 = []
ret_list3 = []
ret_list4 = []
ret_list5 = []
email_list = {  '1122':['edison3.lin@gmail.com','edisonlin.hojac@gmail.com'],
                '1133':'b82506001@gmail.com',
                '1144':['edisonlin.hojac@gmail.com','b82506001@gmail.com'],
                '1155':['pega.edison@gmail.com','edisonlin.hojac@gmail.com']
             }


def ping_ip(dev_ip):
    is_up = subprocess.run("ping -n 1 -w 1 -c 1 %s" % dev_ip, shell=True, stdout=subprocess.PIPE) 
    return False if is_up.returncode else True


def send_cmd(dev_ip, command):
    ## return 從server收到的資料
    port = 4321
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((dev_ip, port))
        client.settimeout(5)
        client.sendall(parse.quote(command).encode('utf-8'))
        while True:
            recv_data = pickle.loads(client.recv(4096))
            if recv_data:
                client.close()
                return recv_data            
    except Exception as e:
        return ['no service']
    finally:
        client.close()
""" 1. Chcek Dev alive
    1. Chcek Dev alive
    1. Chcek Dev alive
""" 
def i1(iDB):
    ping_list = list()
    for item in iDB:
        dev_ip = item['dev_ip']
        dev_id = item['dev_id'] 
        if ping_ip(dev_ip):
            ping_list.append({'dev_id':dev_id, 'status':'alive'})
        else:
            ping_list.append({'dev_id':dev_id, 'status':'disconnect'})
    return ping_list
    
""" 2. Check AMQP alive 
    3. Check AMQP alive 
    4. Check AMQP alive 
"""
def i2():
    if MQ_send.MQ_send('PegatronMQ'):
        time.sleep(1)
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()
            r = channel.basic_get(queue='Edison', auto_ack=False)
            if r[2].decode() == 'PegatronMQ':
                channel.queue_delete(queue='Edison')
                connection.close()
                return True
            else:
                connection.close()
                return False
        except: 
            return False
    else:
        return False

""" 3. Chcek Dev process
    3. Chcek Dev process
    3. Chcek Dev process
""" 
def i3(iDB):
    process_list = list()
    for item in iDB:
        if item['line'] == 'alive':
            dev_ip = item['dev_ip']
            dev_id = item['dev_id'] 
            msg = b'"Process_Operate"'
            P_type = send_cmd(dev_ip, msg)
            process_list.append({'dev_id':dev_id, 'type':P_type})
    return process_list

""" 4. Check Dev Operate
    4. Check Dev Operate
    4. Check Dev Operate
"""    
def i4(iDB):
    log_list = list()
    for item in iDB:
        if item['line'] == 'alive':
            dev_ip = item['dev_ip']
            dev_id = item['dev_id'] 
            if item['equip_type'] == 'AOI':
                msg = b'"AOI_Operate"'
            elif item['equip_type'] == 'SPI':
                msg = b'"SPI_Operate"'
            elif item['equip_type'] == 'Print':
                msg = b'"Print_Operate"'
            elif item['equip_type'] == 'Reflow':
                msg = b'"Reflow_Operate"'
            elif item['equip_type'] == 'Mounter':
                msg = b'"Mounter_Operate"'
            else:
                msg = b'"cancel"'
            # msg = b'"quit"'
            log = send_cmd(dev_ip, msg)
            log_list.append({'dev_id':dev_id, 'status':log[0]})
    return log_list

""" 5. Check Raspberry Operate
    5. Check Raspberry Operate
    5. Check Raspberry Operate
"""   
def i5(iDB):
    Ras_list = list()
    for item in iDB:
        if ((item['line'] == 'alive') and ((item['equip_type'] == 'SPI') or (item['equip_type'] == 'Mounter'))):
            dev_ip = item['dev_ip']
            dev_id = item['dev_id'] 
            msg = b'"Raspberry"'
            Ras = send_cmd(dev_ip, msg)
            Ras_list.append({dev_id:Ras[0]})
    return Ras_list            

""" 6. Check DB Update
    6. Check DB Update
    6. Check DB Update
"""   
def i6():
    with open('os.txt', 'r') as f:
        a = f.readlines()
        for d in a:
            if 'start time' in d:
                b = d.strip('\n')        
                e = b.split(' ')
                i = 0
                for f in e:
                    if f == 'time':
                        t_str = e[i+1]+' '+e[i+2]    
                    i += 1    
                print(t_str)

    
    
""" X. Run remote xServer.py
    X. Run remote xServer.py
    X. Run remote xServer.py
"""   
 
import msvcrt as m
def wait():
    m.getch()
   
def main():
    fun = 0
    while True:
        iDB = DB.Get_DB()   #DB objects
        # print(iDB)
        ret_list1 = []
        # ret_list1 = i1(iDB)
        ret_list2 = []
        ret_list3 = []
        ret_list4 = []
        ret_list5 = []
        while fun not in [1,2,3,4,5,6,9]:
            os.system('cls')
            print('(1) Check Device alive\n')
            print('(2) Check Amqp alive\n')
            print('(3) Check Process operate\n')
            print('(4) Check Device operate\n')
            print('(5) Check Raspberry operate\n')
            print('(6) Check API interface\n')
            print('(9) Exit!\n')
            try:
                fun = int(input('Please input function: (1-6, 9=Exit) '))
            except ValueError:
                os.system('cls')
                print('Input number: (1-6, 9=Exit) ') 
                wait()
        for i in iDB:                    
            if fun == 1:
                ## function 1
                ret_list1 = i1(iDB)
                with codecs.open("fun1.json", "w", "utf-8") as fout:
                    json.dump(ret_list1, fout, indent=4, sort_keys=True)
                # break    
            if fun == 2:
                ## function 2
                if i2():
                    ret_list2.append({'dev_id':'AMQP', 'status':'alive'})
                else:
                    ret_list2.append({'dev_id':'AMQP', 'status':'stop'})
                    
                with codecs.open("fun2.json", "w", "utf-8") as fout:
                    json.dump(ret_list2, fout, indent=4, sort_keys=True)
                
            elif fun == 3:            
                ## function 3
                ret_list3 = i3(iDB)
                # print(ret_list3)
                with codecs.open("fun3.json", "w", "utf-8") as fout:
                    json.dump(ret_list3, fout, indent=4, sort_keys=True)
                # break    
                
            elif fun == 4:            
                ## function 4
                ret_list4 = i4(iDB)
                # print(ret_list4)
                with codecs.open("fun4.json", "w", "utf-8") as fout:
                    json.dump(ret_list4, fout, indent=4, sort_keys=True)
                # break    

            elif fun == 5:            
                ## function 5
                ret_list5 = i5(iDB)
                # print(ret_list5)
                with codecs.open("fun5.json", "w", "utf-8") as fout:
                    json.dump(ret_list5, fout, indent=4, sort_keys=True)
                # break  
            elif fun == 6:            
                ## function 6
                i6()
                wait()
            elif fun == 9:            
                sys.exit(0)
                # break
            else:
                pass
                # break  
            fun = 0
    
    
if __name__ == '__main__':
    main()
        
