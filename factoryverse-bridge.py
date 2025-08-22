import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

path = "C:/Users/jgrim/AppData/Roaming/Factorio/script-output"
path_terraria = "C:/Users/jgrim/Documents"

FactorioEventHandler_Flip = False
TerrariaEventHandler_Flip = False

run = True
items = {}
Ore_Dict = {
    "Dirt": {
        "Terraria": "Dirt Block",
        "Factorio": "dirt"
    },
    "Daybloom_Seed": {
        "Terraria": "Daybloom Seeds",
        "Factorio": "daybloom-seeds"
    },
    "Wulfrum_Battery": {
        "Terraria": "Wulfrum Battery",
        "Factorio": "wulfrum-battery"
    },
    "Wulfrum_Scrap":{
        "Terraria": "Wulfrum Metal Scrap",
        "Factorio": "wulfrum-scrap"
    },
    "Energy_Core": {
        "Terraria": "Energy Core",
        "Factorio": "energy-core"
    },
    "Stone": {
        "Terraria": "Stone Block",
        "Factorio": "stone"
    },
    "Slime_Large": {
        "Factorio": "slimeball"
    },
    "Slime_Small": {
        "Terraria": "Gel",
        "Factorio": "small-slimeball"
    },
    "Diamond": {
        "Terraria": "Diamond",
        "Factorio": "diamond"
    },
    "Wood": {
        "Terraria": "Wood",
        "Factorio": "wood"
    },
    "Iron_Ingot": {
        "Terraria": "Iron Bar",
        "Factorio": "iron-ingot"
    },
    "Lead_Ingot": {
        "Terraria": "Lead Bar",
        "Factorio": "lead-ingot"
    },
    "Gold_Ingot": {
        "Terraria": "Gold Bar",
        "Factorio": "gold-ingot"
    },
    "Copper_Ingot": {
        "Terraria": "Copper Bar",
        "Factorio": "copper-ingot"
    },
    "Tin_Ingot": {
        "Terraria": "Tin Bar",
        "Factorio": "tin-ingot"
    },
    "Platinum_Ingot": {
        "Terraria": "Platinum Bar",
        "Factorio": "platinum-ingot"
    },
    "Iron_Ore": {
        "Terraria": "Iron Ore",
        "Factorio": "iron-ore"
    },
    "Lead_Ore": {
        "Terraria": "Lead Ore",
        "Factorio": "lead-ore"
    },
    "Gold_Ore": {
        "Terraria": "Gold Ore",
        "Factorio": "gold-ore"
    },
    "Copper_Ore": {
       "Terraria":  "Copper Ore",
        "Factorio": "copper-ore"
    },
    "Tin_Ore": {
        "Terraria": "Tin Ore",
        "Factorio": "tin-ore"
    },
    "Platinum_Ore": {
        "Terraria": "Platinum Ore",
        "Factorio": "platinum-ore"
    },
    "Wood_Chest": {
        "Terraria": "Chest",
        "Factorio": "wooden-chest"
    },
    "Oak_Tree_Seed": {
        "Terraria": "Acorn",
        "Factorio": "tree-seed"
    },
    "White_Apricorn": {
        "Terraria": "White Apricorn",
        "Factorio": "white-apricorn"
    },
    "Black_Apricorn": {
        "Terraria": "Black Apricorn",
        "Factorio": "black-apricorn"
    },
    "Red_Apricorn": {
        "Terraria": "Red Apricorn",
        "Factorio": "red-apricorn"
    },
    "Yellow_Apricorn": {
        "Terraria": "Yellow Apricorn",
        "Factorio": "yellow-apricorn"
    },
    "Green_Apricorn": {
        "Terraria": "Green Apricorn",
        "Factorio": "green-apricorn"
    },
    "Blue_Apricorn": {
        "Terraria": "Blue Apricorn",
        "Factorio": "blue-apricorn"
    },
    "Pink_Apricorn": {
        "Terraria": "Pink Apricorn",
        "Factorio": "pink-apricorn"
    },
    "Brown_Apricorn": {
        "Terraria": "Brown Apricorn",
        "Factorio": "brown-apricorn"
    },
    "Bomb_Normal": {
        "Terraria": "Bomb",
        "Factorio": "explosives"
    },
    "Radar_Tool": {
        "Terraria": "Radar"
    }
}

Ore_Dict_In = {}
Ore_Dict_Out = {}

for k, v in Ore_Dict.items():
    for k2, v2 in v.items():
        if not k2 in Ore_Dict_In:
            Ore_Dict_In[k2] = {}
            Ore_Dict_Out[k2] = {}
        print(k)
        Ore_Dict_In[k2][v2] = k
        Ore_Dict_Out[k2][k] = v2

class FactorioEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global FactorioEventHandler_Flip
        global items
        global Ore_Dict_In
        global path
        if event.src_path == path + '\\factorio_trash_update.txt':
            if FactorioEventHandler_Flip == False:
                with open(path + '\\factorio_trash_update.txt' ,"r") as file:
                    for line in file:
                        if line != "":
                            x = line.split(",")
                            if x[0] in Ore_Dict_In["Factorio"]:
                                x[0] = Ore_Dict_In["Factorio"][x[0]]
                            items[x[0]] = items[x[0]] + int(x[1])
                    file.close()
                    with open(path + '\\factorio_trash_update.txt' ,"w") as file:
                        file.write("")
                        file.close()
                FactorioEventHandler_Flip = True
            else:
                FactorioEventHandler_Flip = False

class TerrariaEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global TerrariaEventHandler_Flip
        global items
        global Ore_Dict_In
        global path
        if event.src_path == path_terraria + '\\terraria_trash.txt':
            if FactorioEventHandler_Flip == False:
                with open(path_terraria + '\\terraria_trash.txt' ,"r") as file:
                    for line in file:
                        if line != "":
                            if line == "SYNC\n":
                                with open(path_terraria + '\\terraria_trash_update.txt' ,"w") as file:
                                    str6 = ""
                                    for item, amount in items.items():
                                        if item in Ore_Dict_Out["Terraria"]:
                                            item = Ore_Dict_Out["Terraria"][item]
                                        str6 = str6 + item + ',' + str(amount) + "\n"
                                    print(str6)
                                    file.write(str6)
                            else:
                                x = line.split(",")
                                if x[0] in Ore_Dict_In["Terraria"]:
                                    x[0] = Ore_Dict_In["Terraria"][x[0]]
                                items[x[0]] = items[x[0]] + int(x[1])
                    file.close()
                    with open(path + '\\terraria_trash.txt' ,"w") as file:
                        file.write("")
                        file.close()
                TerrariaEventHandler_Flip = True
            else:
                TerrariaEventHandler_Flip = False

all_trash = open("C://Users//jgrim//Documents//all_trash.txt" ,"r")
for line in all_trash:
    x = line.split(",")
    for k, v in Ore_Dict_In.items():
        if x[0] in v:
            x[0] = v[x[0]]
    items[x[0]] = int(x[1])
all_trash.close()

terraria_trash = open("C://Users//jgrim//Documents//terraria_trash.txt" ,"r")
if terraria_trash.read() != "":
    for line in terraria_trash:
        x = line.split(",")
        if x[0] in Ore_Dict_In["Terraria"]:
            x[0] = Ore_Dict_In["Terraria"][x[0]]
        items[x[0]] = int(x[1])
terraria_trash.close()
terraria_trash = open("C://Users//jgrim//Documents//terraria_trash.txt" ,"w")
terraria_trash.write("")
terraria_trash.close()

factorio_trash = open(path+"//factorio_trash_update.txt" ,"r")
if factorio_trash.read() != "":
    for line in factorio_trash:
        x = line.split(",")
        if x[0] in Ore_Dict_In["Factorio"]:
            x[0] = Ore_Dict_In["Factorio"][x[0]]
        items[x[0]] = int(x[1])
factorio_trash.close()
factorio_trash = open(path+"//factorio_trash_update.txt" ,"w")
factorio_trash.write("")
factorio_trash.close()

factorio_event_handler = FactorioEventHandler()
terraria_event_handler = TerrariaEventHandler()
observer = Observer()
observer.schedule(factorio_event_handler, path)
observer.schedule(terraria_event_handler, path_terraria)
observer.start()
str5 = "/init_factorio_trash "
for item, amount in items.items():
    if item in Ore_Dict_Out["Factorio"]:
        item = Ore_Dict_Out["Factorio"][item]
    str5 = str5 + item + ',' + str(amount) + ";"
subprocess.call(['.//rcon//rcon.exe', '-a', '127.0.0.1:27015', "-p", "aitoo4aetoohe9I", 'command', str5]) 
factorio_trash.close()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    str3 = ""
    for k, v in items.items():
        str3 = str3+k+","+str(v)+"\n"
    all_trash = open("C://Users//jgrim//Documents//all_trash.txt" ,"w")
    all_trash.write(str3)
    all_trash.close()
observer.join()
