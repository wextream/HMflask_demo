import time
import json
import mysql.connector
import paho.mqtt.client as mqtt

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="test1"
)

def insert_data(val):
    mycursor = mydb.cursor()
    sql = "insert into predictioninfo (Date, Time, lat, lon, pmval) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()

def on_message(client2, userdata, message):
    data = (message.payload.decode('utf-8'))
    data = json.loads(data)
    listdata = [data['Date'],data['Time'],data['lat'],data['lon'],data['pmval']]
    if __name__ == '__main__':
        insert_data(listdata)

def on_connect(client, userdata, flags, rc): 
    print("Connected with result code {0}".format(str(rc))) 
    client2.subscribe("pm2.5")
    

broker = '34.124.157.195'
client2 = mqtt.Client('SuperDuperSub')
client2.on_connect = on_connect
client2.on_message = on_message
client2.connect(broker)
client2.loop_forever()