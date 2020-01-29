import json

# Reading the Build_Project JSON File
with open('modify_project.json', 'r') as JsonFile:
    data = json.load(JsonFile)

print("Enter the Project Name you want to build")
data["name"] = input()
