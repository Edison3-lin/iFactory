from mongoengine import *
class User(Document):
    uid = SequenceField(primary_key=True)
    vendor = StringField(max_length=20)
    equip_type = StringField(max_length=20)
    dev_id = StringField(max_length=50)
    dev_ip = StringField(max_length=45)
    dev_mac = StringField(max_length=17)
    factory = StringField(max_length=20)
    line = StringField(max_length=20)

def Get_DB():
    # my = connect('Edison') 
    # connect('DB1', host='168.95.0.2', port=27017)
    connect('DB1', host='mongodb://localhost')
    return User.objects()

""" Update DB
    Update DB
    Update DB
"""    
def UpdateDB(equip_info):
    if(equip_info):
        for user_data in equip_info:
            User(**user_data).save()

