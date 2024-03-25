import asyncio
import tornado.ioloop
import tornado.websocket

class WebSocketClient(tornado.websocket.WebSocketClientConnection):
    async def on_message(self, message):
        print("Received message:", message)

async def receive_data():
    uri = "ws://localhost:8888/websocket"  # WebSocket server URI
    try:
        future = tornado.websocket.websocket_connect(uri)
        client = await future  # Wait for the WebSocket connection to be established
        while True:
            data = await client.read_message()
            print("Received data:", data)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(receive_data)