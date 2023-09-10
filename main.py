import websocket
import time

message1 = "40/lookTime"
message4 = '42/lookTime,["message",{"data":{"cid":18482,"csid":72776,"upid":"6255520","type":1,"token":"9a3965dc181099313f1ca47eb94c318c","time":11,"key":"633277192270593","reqSource":0,"wid":null,"moldType":0}}]'
message3 = "2"
message4 = '42/lookTime,["message",{"data":{"cid":15214,"csid":53700,"upid":"6255520","type":4,"token":"9a3965dc181099313f1ca47eb94c318c","time":3.905758,"key":"352559868122590","reqSource":0,"wid":null,"moldType":0}}]'
def on_message(ws, message):
    print(message)
    if message.startswith("0"):
        time.sleep(3)
        ws.send(message1)
    elif message.startswith("40/lookTime"):
        time.sleep(3)
        ws.send(message4)
    elif message.startswith("42/lookTime"):
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
    wssurl = "wss://newwebnew.zgzjzj.com/socket.io/?token=9a3965dc181099313f1ca47eb94c318c&cid=18482&csid=72778&type=1&upid=6255520&key=615995779790336&wid=NaN&reqSource=0&EIO=3&transport=websocket"
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(wssurl,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()