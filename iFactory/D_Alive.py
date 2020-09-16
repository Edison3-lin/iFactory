import os
import json
def Alive(ip):
    """ JSON字串轉Python dict
        python json字串轉成python物件
        需要使用json模塊的loads()

        dict轉JSON字串
        python物件轉json字串
        需要使用json模塊的dumps()
    """
    
    D_Alive_ret = list()
    json_temp = {}
    for i in ip:
        j = eval(i)
        for dev_id, dev_ip in j.items():
            # print(dev_id)
            # 實現pingIP地址的功能，-c1指傳送報文一次，-w1指等待1秒 
            backinfo = os.system('ping -c 1 -w 1 -n 1 %s' % dev_ip)
            json_temp['dev_id'] = dev_id
            if backinfo:
                json_temp['status'] = 'stop'
            else:
                json_temp['status'] = 'alive'
            D_Alive_ret.append(json.dumps(json_temp))
        

    for i in D_Alive_ret:
        a = json.loads(i)
        print(a['status'])    
    return D_Alive_ret



