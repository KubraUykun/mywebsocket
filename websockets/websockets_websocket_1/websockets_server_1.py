# server.py
import asyncio
import websockets
import random
import string

async def stream_data(websocket, path):
    print("WebSocket connection established")
    try:
        while True:
            data = ''.join(random.choices(string.ascii_letters, k=10))  # Generate random data      
            await websocket.send(data) # Send data to the client
            await asyncio.sleep(1)  # Adjust the interval as needed
    except websockets.exceptions.ConnectionClosedError:
        print("WebSocket connection closed")


if __name__ == "__main__":
    start_server = websockets.serve(stream_data, "localhost", 8888)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("WebSocket server started on port 8888")
    asyncio.get_event_loop().run_forever()