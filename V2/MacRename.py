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

#Gathers current computer name
current_name = subprocess.Popen(["scutil", "--get", "LocalHostName"], stdout=subprocess.PIPE)
compName = str(current_name.stdout.read()).rstrip()
print compName


#Finds current computer name in dictionary
if str(compName) in mdict:
    #Renames computer name, host name, and local host name
    subprocess.call(["sudo", "scutil", "--set", "LocalHostName", mdict[compName]])
    subprocess.call(["sudo", "scutil", "--set", "HostName", mdict[compName]])
    subprocess.call(["sudo", "scutil", "--set", "ComputerName", mdict[compName]])
else:
    print("Computer not in dictionary or Addigy")
