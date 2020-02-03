import json

# Reading the Modify_Project JSON File
with open('deploy_project.json', 'r') as JsonFile:
    json_data = json.load(JsonFile)

print("Enter the Project Name")
json_data["name"] = input()

print("Enter the Number of Components you have in the Project that you want to modify")
compo_num = input()

for i in range(int(compo_num)):
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

    # Entering the Custom Docker Image
    print("Want to add a Custom Docker Image")
    print("Enter 1 to Add, Anything Else not to")
    docker_ch = input()
    if docker_ch == '1':
        print("Enter the Custom Docker Image")
        docker = input()
    else:
        docker = ""

    # Entering the Environment Variables
    print("Do you want to add any Environment Parameters")
    print("Enter 1 to Add, Or anything else not to!")
    env_par_ch = input()
    if env_par_ch == '1':
        print("Enter the environment_parameters name and value")
        env_par_name = input("Enter the Name: ")
        env_par_value = input("Enter the Value: ")
        env = [{"name": env_par_name, "value": env_par_value}]
    else:
        env = []

    # Entering any command to run:
    print("Do you want to Enter any Command")
    print("Enter 1 to add or anything else not to")
    command_ch = input()
    if command_ch == '1':
        print("Enter the Command to be passed")
        command_pass = input()
    else:
        command_pass = ""

        # Entering the Type of Component
        print("Is this component of type= JOB")
        print("If Yes then type 1, else anything else")
        job = input()
        if job == '1':
            job = "job"
            print("Select the Type of Job")
            print("Enter 1 for Normal Job")
            print("Enter 2 for Cron Job")
            job_ch = input()
            if job_ch == '1':
                job_type = 'normal job'

            elif job_ch == '2':
                job_type = 'cron job'
                print("Do you want to add a CronJob")
                print("Enter 1 to Add else anything for not to")
                cron_ch = input()
                if cron_ch == '1':
                    print("Enter the cron schedule in the specific Cron job format")
                    cron_job = input()
                else:
                    cron_job = ""

    # # Entering any args to run:
    # print("Do you want to Enter any Arguments")
    # print("Enter 1 to add or anything else not to")
    # args_ch = input()
    # if args_ch == '1':
    #     print("Enter the number of arguments you need to pass")
    #     args_num = input()
    #     args_list = []
    #     for j in range(int(args_num)):
    #         print("Enter the Command to be passed")
    #         args = input()
    #         args_list.append(args)

    comp = {"replicas": replica_no, "build": build, "custom_docker_image": docker, "environment": env, "command": command_pass, "type": "job", "cron_schedule": cron_job}
    json_data["components"][comp_name] = comp


# Writing into the JSON File
with open('deploy_project.json', 'w') as JsonFile:
    json.dump(json_data, JsonFile, indent=2)

print("Your Deploy Project Json:")
print(json.dumps(json_data, indent=1))
