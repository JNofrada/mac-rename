import subprocess

#Opens computer name text ile
comp = open("mother_devices.csv", "r")

#Creates dictionary for with current computer names and new computer names
mdict = {
    "Current Name": "New Name"
}

for line in comp:
    if not line: break
    field = line.split(",")
    mdict.update({str(field[0]):str(field[1]).rstrip()})

for x, y in mdict.items():
    print(x,y)

#Gathers current computer name
#current_name = subprocess.call(["scutil", "--get", "computerName"])
current_name = '15326-Test'

#Finds current computer name in dictionary
if str(current_name) in mdict:
    #Renames computer name, host name, and local host name
    subprocess.call(["sudo", "scutil", "--set", "LocalHostName", mdict[current_name]])
    subprocess.call(["sudo", "scutil", "--set", "HostName", mdict[current_name]])
    subprocess.call(["sudo", "scutil", "--set", "ComputerName", mdict[current_name]])
else:
    print("Computer not in dictionary or Addigy")
