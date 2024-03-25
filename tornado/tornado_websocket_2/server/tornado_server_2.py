import tornado.ioloop
import tornado.web
import tornado.websocket
import os

# WebSocket handler class
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")

    def on_message(self, message):
        print("Received message:", message)
        if message == "send_file":
            self.send_file("example.xlsx")  # 'example_big.xslx'
        else:
            self.write_message("Unknown command")

    def on_close(self):
        print("WebSocket connection closed")

    def send_file(self, filename):
        try:
            with open(filename, "rb") as file:
                file_content = file.read()
                self.write_message(file_content, binary=True)
                print("File sent successfully")
        except FileNotFoundError:
            print(f"File '{filename}' not found")
            self.write_message("File not found")

# Application setup
app = tornado.web.Application([
    (r"/websocket", WebSocketHandler),
])

if __name__ == "__main__":
    # Start the server
    app.listen(8888)
    print("WebSocket server started on port 8888")
    tornado.ioloop.IOLoop.current().start()