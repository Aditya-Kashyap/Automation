from subprocess import *
import json
from component_add import ComponentAddition

# Making Object for the class ComponentAddition
comp_obj = ComponentAddition()


# Logging In:
print('Please Enter the User ID \n')
u_id = input()
print('\nPlease enter the Work Space which you want to work in:\n ')
work_env = input()
login_command_string = 'xprctl login -u ' + u_id + ' ' + '-w ' + work_env

print('\nYour Login Command\n')
print(login_command_string)

login = Popen(login_command_string, shell=True)
login.wait()

login_status = login.poll()

if login_status == 0:
    # Create Project ______________________________________________________________________
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

    while choice == '1':  # Running a loop when the user has added an component and if he wants to add more
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

    create_project_string = "xprctl create_project -f create_project.json"
    create_project = Popen(create_project_string, shell=True)
    create_project.wait()
    create_status = create_project.poll()

    if create_status == 0:
        # Building Project _____________________________________________________________

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

        build_project_string = "xprctl build_project -f build_project.json"
        build_command = Popen(build_project_string, shell=True)
        build_command.wait()
        build_status = build_command.poll()
        print(build_status)