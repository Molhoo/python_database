
import sqlite3 as DB
from datetime import datetime

co = DB.connect('Conet.db')
cr = co.cursor()

def init():
    #create in to table
    cr.execute('''CREATE TABLE IF NOT EXISTS everyday (
                 amuont_money REAL ,
                 daily_activity TEXT COLLATE NOCASE,
                 message TEXT COLLATE NOCASE ,
                 data TEXT              
                )''')
    co.commit()
    co.close()

def Add(amuont_money , daily_activity , message = ''):

    #Add to the databasse 

    data = str(datetime.now().strftime('%Y - %m - %d | %H:%M'))
    cr.execute('INSERT INTO everyday VALUES (:amuont_money , :daily_activity , :message , :data)' ,
     {'amuont_money':amuont_money , 'daily_activity':daily_activity , 'message':message , 'data':data})
    co.commit()
    co.close()

def Show(daily_activity = None):
    
    #Show All the databass 

    if daily_activity:
        cr.execute('SELECT * FROM everyday WHERE daily_activity = (:daily_activity)' , {'daily_activity':daily_activity})
        result = cr.fetchall()
        cr.execute('SELECT sum(amuont_money) FROM everyday WHERE daily_activity = (:daily_activity)' , {'daily_activity':daily_activity})
        Total_money = cr.fetchall()[0]
    else:
        cr.execute('SELECT * FROM everyday')
        result = cr.fetchall()
        cr.execute('SELECT sum(amuont_money) FROM everyday')
        Total_money = cr.fetchall()[0]
    
    return Total_money , result
    cr.close()

#init()
#Add(10 , 'edible' , 'lavashk va pofak khridm.')

#print(Show('game net'))
