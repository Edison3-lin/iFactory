import time
from pathlib import Path
import os
# 檔案或目錄路徑
# my_file = Path("/etc/os-release")
def Operate(equip_type):
    
    # 格式化成2016-03-20 11:45:39形式
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 

    
    # 格式化成Sat Mar 28 22:24:24 2016形式
    # print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) 
    
    # 将格式字符串转换为时间戳
    # a = "Sat Mar 28 22:24:24 2016"
    # print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))    
    
    
    # print(equip_type)
    # if equip_type == 'SPI':
    if equip_type == 'Mounter':
        name = time.strftime("%Y%m%d", time.localtime()) 
        file = os.path.join('e:/cae_app/jobs/', name+".dat")         
        my_file = Path(file)        
        
    if equip_type == 'Reflow':
        name = time.strftime("%Y%m%d", time.localtime()) 
        file = os.path.join('e:/cae_app/jobs/', name+".dat")         
        my_file = Path(file)        
        
    if equip_type == 'Print':
        name = time.strftime("%Y%m%d", time.localtime()) 
        file = os.path.join('e:/cae_app/jobs/', name+".log")         
        my_file = Path(file)        
    
    # if equip_type == 'AOI':
    
    return my_file.exists()