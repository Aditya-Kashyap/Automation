import json

# Reading the Modify_Project JSON File
with open('deploy_project.json', 'r') as JsonFile:
    data = json.load(JsonFile)

print("Enter the Project Name")
data["name"] = input()

print("Enter the Number of Components you have in the Project that you want to modify")
compo_num = input()

for i in range(2):
    print("Enter the Component Name")
    comp_name = input()

    # Entering Replica
    print("Enter the number of Replica you want to make")
    replica_no = input()

    # Entering the Build Version
    print("Do you want you specify the Build Version. It's mandatory if NOT specifying a Custom Docker Image")
    print("Enter 1 to specify or anything else not to")
    build_choice = input()
    if build_choice == '1':
        print("Enter the build version")
        build = input()
    else:
        build = ""

    comp = {"replicas": replica_no, "build": build}
    data["components"][comp_name] = comp

# Writing into the JSON File
with open('deploy_project.json', 'w') as JsonFile:
    json.dump(data, JsonFile, indent=2)

print("Your Deploy Project Json:")
print(json.dumps(data, indent=1))
