import asyncio
import websockets

async def send_file(websocket, path):
    # Open the CSV file to be sent
    with open('example.xlsx', 'rb') as file: #'example_big.xlsx'
        # Read the file content
        file_content = file.read()
        # Send the file content over the WebSocket connection
        await websocket.send(file_content)
        print("File sent successfully")

start_server = websockets.serve(send_file, "localhost", 8765, max_size=None)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()