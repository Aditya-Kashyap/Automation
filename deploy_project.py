import json
from component_add import ComponentAddition

# Making Object for the class ComponentAddition
comp_obj = ComponentAddition()

# Reading the Build_Project JSON File
with open('deploy_project.json', 'r') as JsonFile:
    json_data = json.load(JsonFile)


print("Enter the Project Name you want to deploy!")
json_data["name"] = input()

print("Enter the target environment you want to deploy in:")
json_data["target_environment"] = input()

print("Enter the Number of Components you want to deploy")
comp_num = input()

for i in range(int(comp_num)):
    print("Enter the Component Name")
    comp_name = input()
    json_data["components"] = comp_name
    comp = comp_obj.comp_add_deploy()
    json_data["components"][comp_name] = comp

# Writing into the JSON File
with open('deploy_project.json', 'w') as JsonFile:
    json.dump(json_data, JsonFile, indent=2)

print("Your Deploy Project Json:")
print(json.dumps(json_data, indent=1))
