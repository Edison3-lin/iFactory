#-*- coding: utf-8 -*-
import socket
import os
import threading

import urllib.parse
import ctypes
import datetime
import subprocess
import json
import pickle
import time
from pathlib import Path

local_port = 4321                           # 配置socket server繫結的本地埠
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)   # 配置socket server繫結的本地IP
# local_ip = '168.95.0.2'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_ip, local_port))

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("172.0.0.1",local_port))
server.listen(5)

# 只響應白名單中的計算機發來的任務
# admin_filter的key()
admin_filter = list()
admin_filter.append('127.0.0.1')
admin_filter.append('172.20.10.3')
admin_filter.append('172.20.10.4')
admin_filter.append('168.95.0.1')
admin_filter.append('168.95.0.2')


print('White list:' + str(admin_filter))
print('Server bind on %s:%s' % (local_ip, str(local_port)))
print('-----------------Server starting success-----------------')

""" Device Operate
    Device Operate
    Device Operate
"""
def Doperate(conn, command):
    ret = list()
    name = time.strftime("%Y%m%d", time.localtime()) 
    my_file = os.path.join('d:/xxx/', name+"."+command[1:4])         
    try:
        file = open(my_file, 'r')
        ret.append('data path change')
        conn.send(pickle.dumps(ret)) 
        return True
    except FileNotFoundError:
        ret.append('device stop')
        conn.send(pickle.dumps(ret)) 
        return False

""" Check Process Operate
    Check Process Operate
    Check Process Operate
"""
def Check_Process(conn):
    ### subprocess - 執行powershell檔案
    print('ediso')
    ret = list()
    POWERSHELL = "%SystemRoot%\system32\WindowsPowerShell\\v1.0\\powershell.exe"
    LINE = subprocess.run("POWERSHELL get-process -name LINE", shell=True, stdout=subprocess.PIPE) 
    if LINE.returncode == 0:
        ret.append('LINE') 
    TOTALCMD = subprocess.run("POWERSHELL get-process -name TOTALCMD", shell=True, stdout=subprocess.PIPE) 
    if TOTALCMD.returncode == 0:
        ret.append('TOTALCMD') 
    BCompare = subprocess.run("POWERSHELL get-process -name BCompare", shell=True, stdout=subprocess.PIPE) 
    if BCompare.returncode == 0:
        ret.append('BCompare') 
    print(ret)
    if ret == []:
        ret = ['No process']    
    conn.send(pickle.dumps(ret))
    
def Check_Raspberry(conn):
    ret = list()
    my_file = os.path.join('d:/smt/exe/pre.txt')
    try:
        file = open(my_file, 'r')
        file_stamp = os.path.getmtime(my_file)
        current = time.time()
        if (current - file_stamp) < 3600:
            ret.append('work')
        else:
            ret.append('stop')
        conn.send(pickle.dumps(ret)) 
        return True
    except FileNotFoundError:
        ret.append('pre.txt not found')
        conn.send(pickle.dumps(ret)) 
        return False
    
def exe_prog(command):
    # 路徑由空格，加上引號就好
    f = os.system(command)
    # os.system("C:\ProgramData\Anaconda3\envs\py2\python.exe F:\\source_files\\quant\\remote_pc_control\\exe_calc.py")
    # server.send(f)
    
def main():        
    while True:
        conn, addr = server.accept()
        command = urllib.parse.unquote(conn.recv(1024).decode('utf-8'))
        
        peer_name = conn.getpeername()
        sock_name = conn.getsockname()

        # peer_name是個tuple，peer_name[0]是ip，peer_name[1]是埠號
        now_dt = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print(u'%s, From %s:%s'%(now_dt, peer_name[0],peer_name[1])) # , sock_name
        # 白名單，管理員許可權驗證
        # print(peer_name[0])
        # if peer_name[0] in admin_filter:
        if True:
            print(command)

            if command == '"cancel"':           
                conn.send(pickle.dumps(['None'])) 
            elif command == '"Process_Operate"':
                Check_Process(conn) 
            elif command in ['"AOI_Operate"', '"SPI_Operate"', '"Print_Operate"', '"Reflow_Operate"', '"Mounter_Operate"']:
                Doperate(conn, command)
            elif command == '"Raspberry"':
                Check_Raspberry(conn)
            else:
                command == '"quit"'
                conn.send(pickle.dumps(['Quit'])) 
                conn.close()
                exit(0)
    
                
            # if command == '"start server"'
            #     t = threading.Thread(target=exe_prog,args=(command,))
            #     t.start()

        #conn.send('server: I received '+command)
    
    
if __name__ == '__main__':
    main()
    
    
    
    