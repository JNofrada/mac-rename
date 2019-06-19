import subprocess

#Opens computer name text ile
comp = open("comp_names.txt", "r")

#Gathers current computer name
current_name = subprocess.call(["scutil", "--get", "computerName"])

#Finds current computer name in text file and compares to current computer name
for line in comp:
    if not line: break
    field = line.split(",")
    name1 = field[0]
    name2 = field[1]

    if (current_name == name1):
        #Renames computer name, host name, and local host name
        subprocess.call(["sudo", "scutil", "--set", "LocalHostName", name])
        subprocess.call(["sudo", "scutil", "--set", "HostName", name])
        subprocess.call(["sudo", "scutil", "--set", "ComputerName", name])