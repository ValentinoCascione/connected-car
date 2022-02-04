import RPi.GPIO as gpio
import time

import asyncio
import websockets
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def forward():
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)

def turnLeft():
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

def turnRight():
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)

def reverse():
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)

def stop():
    init()
    gpio.cleanup()
    
async def server(websocket, path):
    async for message in websocket:
        print(message)
        if (message == "forward"):
            forward()
        elif (message == "stop"):
            stop()
        elif (message == "reverse"):
            reverse()
        elif (message == "turnLeft"):
            turnLeft()
        elif(message == "turnRight"):
            turnRight()

        await websocket.send(message)

start_server = websockets.serve(server, "", 4040)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
