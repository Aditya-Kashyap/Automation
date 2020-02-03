import json
from component_add import ComponentAddition

# Making Object for the class ComponentAddition
comp_obj = ComponentAddition()

# Reading a JSON File
with open('create_project.json', 'r') as JsonFile:
    data = json.load(JsonFile)

# Entering Details for the create_json file:
print("Enter the Name of Project")
data["name"] = input()

print("Enter the Project Description")
pro_desc = input()

print("Enter Your User ID")
user_id = input()

print("Enter the Environment you want to code in")
env = input()

print("Enter the Persistent Volume Size")
per_vol = input()

# Appending these Data's into the JSON Object
data['owner']['uid'] = user_id
data['developers'] = [user_id]
data['environments'] = env
data['projectDescription'] = pro_desc
data['persistent_volume_size'] = int(per_vol)

# Taking User Choice for Adding Components:
print("Do you want to add any components")
print("Press 1 to add a component")
choice = input()

if choice == '1':
    comp = comp_obj.comp_add()
    data["components"].append(comp)

else:
    pass

while choice == '1':     # Running a loop when the user has added an component and if he wants to add more
    print("Do you want to add any other component!")
    print("Enter 1 to Add or Any other key to Exit")
    ch = input()
    if ch == '1':
        comp = comp_obj.comp_add()
        data["components"].append(comp)
    else:
        break

# Writing the Modified Data into the JSON File
with open('create_project.json', 'w') as JsonFile:
    json.dump(data, JsonFile, indent=2)

print("Your New create_project JSON Files looks:")
print(json.dumps(data, indent=1))
