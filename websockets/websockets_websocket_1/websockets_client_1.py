# client.py
import asyncio
import websockets
import time

async def receive_data():
    uri = "ws://localhost:8888"  # WebSocket server URI
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                start_time = time.perf_counter()  # Record the start time
                data = await websocket.recv()  # Receive data from the server
                print("Received data:", data)
                end_time = time.perf_counter()  # Record the end time
                elapsed_time = end_time - start_time  # Calculate the elapsed time
                print(f"Elapsed time: {elapsed_time:.6f} seconds")
        except websockets.exceptions.ConnectionClosedError:
            print("WebSocket connection closed")
                              
 
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(receive_data())