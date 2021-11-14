from websocket import create_connection
import json
import time

# accesses and stores the information of the api


# opens plot file
file = open('plotted.txt', 'a')
warnFile = open('warningLog.txt', 'a')

index = 0

while True:
    # websocket api
    ws = create_connection("wss://2021-utd-hackathon.azurewebsites.net")
    recieve = ws.recv()

    time.sleep(4.97)    # delay time for the next update

    # load the
    recieve = json.loads(recieve)
    flowRate = recieve["flowRateIn"]
    file.write(str(index))
    file.write(',')
    json.dump(flowRate, file)
    file.write('\n')
    file.flush()
    index += 1

    print(round(flowRate))
    # check flow rate, based on that decide how much to open water flow, and write to warn log if needed
    if (round(flowRate) >= 400000 and round(flowRate) <= 600000): # make common case first
        print("Water levels good: medium flow rate (50%)")
    elif(round(flowRate) > 600000 and round(flowRate) < 1000000):
        warnFile.write("On day ")
        warnFile.write(str(index))
        warnFile.write(": warning, water level high, temporarily decreased intake \n")
        print("Flow level approaching critical high: decrease flow rate (15%)")
        warnFile.flush()
    elif (round(flowRate) >= 1000000):
        warnFile.write("On day ")
        warnFile.write(str(index))
        warnFile.write(": warning, water level high, temporarily decreased intake \n")
        print("Flow level at critical high: SHUTDOWN (0%)")
        warnFile.flush()
    else: #<30000
        warnFile.write("On day ")
        warnFile.write(str(index))
        warnFile.write(": warning, water level low, temporarily increased intake \n")
        print("Flow level at critical low: increase flow rate (85%)")
        warnFile.flush()
