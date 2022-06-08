import asyncio
import websockets
import pyautogui


async def hello():
    async with websockets.connect("ws://localhost:8080") as websocket:
        await websocket.send("Hello world!")
        while True:
            message = await websocket.recv()
            match message:
                case 'up':
                    pyautogui.moveRel(0, -10)
                case 'down':
                    pyautogui.moveRel(0, 10)
                case 'left':
                    pyautogui.moveRel(-10, 0)
                case 'right':
                    pyautogui.moveRel(10, 0)
                case 'disconnect':
                    break

asyncio.run(hello())
