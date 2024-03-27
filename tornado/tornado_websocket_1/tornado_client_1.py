import asyncio
import tornado.ioloop
import tornado.websocket
import time

class WebSocketClient(tornado.websocket.WebSocketClientConnection):
    async def on_message(self, message):
        print("Received message:", message)

async def receive_data():
    uri = "ws://localhost:8888/websocket"  # WebSocket server URI
    try:
        future = tornado.websocket.websocket_connect(uri)
        client = await future  # Wait for the WebSocket connection to be established
        while True:
            start_time = time.perf_counter()  # Record the start time
            data = await client.read_message()
            print("Received data:", data)
            end_time = time.perf_counter()  # Record the end time
            elapsed_time = end_time - start_time  # Calculate the elapsed time
            print(f"Elapsed time: {elapsed_time:.6f} seconds")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(receive_data)