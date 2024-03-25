import asyncio
import tornado.ioloop
import tornado.web
import tornado.websocket
import random
import string

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    async def open(self):
        print("WebSocket connection opened")
        await self.stream_data()

    def on_close(self):
        print("WebSocket connection closed")

    async def stream_data(self):
        while True:
            data = ''.join(random.choices(string.ascii_letters, k=10))  # Generate random data
            self.write_message(data)  # Send data to the client
            await asyncio.sleep(1)  # Adjust the interval as needed

# Application setup
app = tornado.web.Application([
    (r"/websocket", WebSocketHandler),
])

if __name__ == "__main__":
    # Start the server
    app.listen(8888)
    print("WebSocket server started on port 8888")
    tornado.ioloop.IOLoop.current().start()