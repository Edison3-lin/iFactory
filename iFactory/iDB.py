import cx_Oracle

def Get_DB():
  # user = "smtuser"
  # passwd = "pega#1234"
  # listener = '10.255.70.36:1521'
  """ SQLPLUS """
  # d:>sqlplus system/2goixdxi@//localhost:1521/XEPDB1 as sysdba
  # SQL>grand dba to admin;
  
  db = cx_Oracle.connect("system/2goixdxi@//localhost:1521/XEPDB1")
  cur = db.cursor()

  cur.execute("SELECT * FROM SYS.EQUIP_INFO$")
  res = cur.fetchall()
  equip_info = list()
  for r in res:
    equip_info.append({'vendor':r[0],'equip_type':r[1],'dev_id':r[2],'dev_ip':r[3], \
    'dev_mac':r[4],'factory':r[5],'line':r[6]})

  # # 关闭数据库连接
  db.close()
  return equip_info

