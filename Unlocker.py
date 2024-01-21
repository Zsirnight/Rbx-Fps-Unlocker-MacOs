from time import sleep
import json

FpsSelection = input("Type out the exact number of frames per second you want your roblox client to uncap to (for example, 30 or 120): \n")
with open("/Applications/Roblox.app/Contents/MacOS/ClientSettings/ClientAppSettings.json", "w") as json_file:
    data_dict = {"DFIntTaskSchedulerTargetFps": FpsSelection}
    json.dump(data_dict, json_file)
print(f"Your FPS has been uncapped to : {FpsSelection} Fps | if roblox is open , fully close it and rerun it for the fps change to take affect")
sleep(1)
input("Press Enter/Return to exit...")
