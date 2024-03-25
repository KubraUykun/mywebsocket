import asyncio
import websockets
import time

async def receive_file():
    uri = "ws://localhost:8765"  # WebSocket server URI
    async with websockets.connect(uri, max_size=None) as websocket:
        start_time = time.time()  # Record the start time
        # Receive the file content from the server
        file_content = await websocket.recv()
        # Save the received file content to a file
        with open('received_file.xlsx', 'wb') as file:
            file.write(file_content)
            print("File received and saved successfully")
        
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(receive_file())