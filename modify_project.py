import json
from component_add import ComponentAddition

# Reading the Build_Project JSON File
with open('modify_project.json', 'r') as JsonFile:
    data = json.load(JsonFile)

# Making Object for the class ComponentAddition
comp_obj = ComponentAddition()

print("Enter the Name of Previously Created Project you want to Modify")
project_name = input()
data["name"] = project_name

print("Do you want to add any components")
print("Enter 1 to Add or Any other key to Exit")
ch = input()
if ch == '1':
    comp = comp_obj.comp_add()
    data["components"].append(comp)
else:
    pass

# Writing into the JSON File
with open('modify_project.json', 'w') as JsonFile:
    json.dump(data, JsonFile, indent=1)

print("Your Modified Project :")
print(json.dumps(data, indent=1))
