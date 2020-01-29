import json

# Reading the Build_Project JSON File
with open('build_project.json', 'r') as JsonFile:
    data = json.load(JsonFile)

print("Enter the Project Name")
data["name"] = input()

print("Enter the Number of Components you have in the Project that you want to build")
compo_num = input()

for i in range(int(compo_num)):
    print("Enter the Component Name")
    comp_name = input()

    print("Enter the Branch You want to push it in")
    comp_branch = input()

    print("Enter the description i.e: trail version")
    comp_desc = input()

    comp = {"branch": comp_branch, "description": comp_desc}
    data["components"][comp_name] = comp

# Writing into the JSON File
with open('build_project.json', 'w') as JsonFile:
    json.dump(data, JsonFile, indent=2)

print("Your Build Project :")
print(json.dumps(data, indent=1))
