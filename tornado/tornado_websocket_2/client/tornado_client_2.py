import asyncio
import tornado.ioloop
import tornado.websocket
import time

async def receive_file():
    uri = "ws://localhost:8888/websocket"  # WebSocket server URI
    try:
        start_time = time.time()  # Record the start time

        # Set max_message_size to desired value (in bytes)
        max_message_size = 50 * 1024 * 1024  # For example, 10 MB
        
        websocket = await tornado.websocket.websocket_connect(uri, max_message_size=max_message_size)
        
        # Send command to request the file
        await websocket.write_message("send_file")
        
        # Receive the file content from the server
        file_content = await websocket.read_message()
        
        # Save the received file content to a file
        with open('received_file.xlsx', 'wb') as file:
            file.write(file_content)
            print("File received and saved successfully")
        
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
            
    except tornado.websocket.WebSocketClosedError:
        print("WebSocket connection closed unexpectedly")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(receive_file())