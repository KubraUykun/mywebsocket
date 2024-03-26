## mywebsocket
This repo contains 2 different ways of websocket server-client implementations, one using the python library "websockets" and the other using "tornado" framework.

In the folder "websockets", there are 2 different implementations of websocket communication. 
-In "websockets_websocket_1", "websockets_server_1.py" creates random data stream and sends it to the client "wesockets_client_1.py" in real-time.
-In "websockets_websocket_2", "websockets_server_2.py" sends a .xlsx file to the client "websockets_client_2.py" in a websocket connection.

In the folder "tornado", there are 2 different implementations of websocket communication. 
-In "tornado_websocket_1", "tornado_server_1.py" creates random data stream and sends it to the client "tornado_client_1.py" in real-time.
-In "tornado_websocket_2", "tornado_server_2.py" sends a .xlsx file to the client "tornado_client_2.py" in a websocket connection.

## Requirements
* Install all modules inside requirements.txt. Suggested way is to follow the following steps:
```
cd <path to mywebsocket>
conda create --name mywebsocketenv python=3.9
conda activate mywebsocketenv
pip install -r requirements.txt
```


