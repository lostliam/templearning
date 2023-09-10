import websocket
import time
import re,random
classids = [
    '42/lookTime,["message",{"data":{"cid":18538,"csid":73008,"upid":"6255520","type":4,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":157.981332,"key":"634792018203748","reqSource":0,"wid":null,"moldType":0}}]',
    '42/lookTime,["message",{"data":{"cid":15214,"csid":53700,"upid":"6255520","type":4,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":3.905758,"key":"352559868122590","reqSource":0,"wid":null,"moldType":0}}]',
    '42/lookTime,["message",{"data":{"cid":18482,"csid":72776,"upid":6255520,"type":4,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":14.952045,"key":"420577864522462","reqSource":0,"wid":null,"moldType":0}}]',
    '42/lookTime,["message",{"data":{"cid":6449,"csid":18459,"upid":6255520,"type":4,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":3.904323,"key":"344012491077215","reqSource":0,"wid":null,"moldType":0}}]',
    '42/lookTime,["message",{"data":{"cid":17938,"csid":69285,"upid":6255520,"type":4,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":3.92059,"key":"355744184163808","reqSource":0,"wid":null,"moldType":0}}]',
    '42/lookTime,["message",{"data":{"cid":17949,"csid":69357,"upid":6255520,"type":4,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":3.854015,"key":"296716742604587","reqSource":0,"wid":null,"moldType":0}}]',
    '42/lookTime,["message",{"data":{"cid":5878,"csid":16523,"upid":6255520,"type":4,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":3.893309,"key":"952537441592507","reqSource":0,"wid":null,"moldType":0}}]',
    '42/lookTime,["message",{"data":{"cid":5879,"csid":16526,"upid":6255520,"type":4,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":3.920325,"key":"191903525324193","reqSource":0,"wid":null,"moldType":0}}]'
]

message1 = "40/lookTime"
message4 = '42/lookTime,["message",{"data":{"cid":18482,"csid":72776,"upid":"6255520","type":1,"token":"2f9c8ac1af3e4e17364a2a8dc6161b41","time":11,"key":"633277192270593","reqSource":0,"wid":null,"moldType":0}}]'
message3 = "2"
message4 = random.choice(classids)
def on_message(ws, message):
    global message4
    if message.startswith("0"):
        time.sleep(3)
        ws.send(message1)
    elif message.startswith("40/lookTime"):
        time.sleep(3)
        ws.send(message4)
    elif message.startswith("42/lookTime"):
        print(message)
        match = re.search(r'"lookTime":(\d+)', message)
        if match:
            look_time = match.group(1)
            if int(look_time)> 2.5*60*60:
                message4=random.choice(classids)
        time.sleep(3)
        ws.send(message3)
    elif message.startswith("3"):
        time.sleep(3)
        ws.send(message4)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection established")

if __name__ == "__main__":
    wssurl = "wss://newwebnew.zgzjzj.com/socket.io/?token=2f9c8ac1af3e4e17364a2a8dc6161b41&cid=18482&csid=72778&type=1&upid=6255520&key=615995779790336&wid=NaN&reqSource=0&EIO=3&transport=websocket"
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(wssurl,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()