import os

with os.scandir('//TEATREE/USER04') as entries:
    for entry in entries:
        print(entry.name)

