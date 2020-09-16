import os
import requests
import json
def Alive(http_list):
    """ 1.傳送 AMQP require，確認回傳訊息(reply message)
        2.讀取 AMQP Queue，確認資料會正常存入Stack
        3.Step1 若失敗即代表Server本身有問題，依回傳訊息判定錯誤情況輸出對應訊息
        4.Step2 若失敗即代表Server軟體有問題，輸出訊息建議重新啟動
    Output:
        1.以Json文件輸出
        2.Output = {}
          Status:["alive","disconnect","send fail","queue fail"]
    """
    try:
        r = requests.get(http_list,timeout = 3)
        if r.status_code == requests.codes.ok:
            print('AMQP alive')
    except:
        print('AMQP stop')
    
                
    return 'Amqp_Alive\n'