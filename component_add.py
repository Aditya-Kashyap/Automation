class ComponentAddition:

    def __init__(self):
        self.arr = {"name": "sample-name", "type": "sample-type", "flavor": "sample-flavor", "description": "sample"}

    @staticmethod
    def comp_add():
        print("Enter the Name of Component to be added")
        comp_name = input()
        print("Enter the Type of Components")
        comp_type = input()
        print("Enter the Flavor of the component")
        comp_flavor = input()
        print("Enter a Description for the Component")
        comp_desc = input()

        # Adding those new components in the shape of array:
        data = {"name": comp_name, "type": comp_type, "flavor": comp_flavor, "description": comp_desc}
        return data

    @staticmethod
    def comp_add_deploy():

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

        # # Entering the Custom Docker Image
        # print("Want to add a Custom Docker Image")
        # print("Enter 1 to Add, Anything Else not to")
        # docker_ch = input()
        # if docker_ch == '1':
        #     print("Enter the Custom Docker Image")
        #     docker = input()
        #     data["components"][comp_name] = {"custom_docker_image", docker}
        #
        # # Entering the Environment Variables
        # print("Do you want to add any Environment Parameters")
        # print("Enter 1 to Add, Or anything else not to!")
        # env_par_ch = input()
        # if env_par_ch == '1':
        #     print("Enter the environment_parameters name and value")
        #     env_par_name = input("Enter the Name: ")
        #     env_par_value = input("Enter the Value")
        #     data["components"][comp_name]["environment_parameters"] = [{"name": env_par_name, "value": env_par_value}]
        # else:
        #     data["components"][comp_name]["environment_parameters"] = []
        #
        # # Entering the Port
        # print("Do you want to add PORT:")
        # print("Enter 1 to Add to Add Port, Anything else not to")
        # port_ch = input()
        # if port_ch == '1':
        #     print("Enter the Port name and the corresponding value")
        #     port_name = input("Enter the Port Name")
        #     port_value = input("Enter the Port Value")
        #     data["components"][comp_name]["ports"] = [{"name": port_name, "value": port_value}]
        #
        # # Entering the Persistent Volume
        # print("Do you want to add a Persistent Volume")
        # print("Enter 1 to add or anything else not to")
        # per_space = input()
        # if per_space == '1':
        #     print("Enter the Mount Path")
        #     mount_path = input()
        #     data["components"][comp_name]["persistence"] = [{"mount_path": mount_path}]
        #
        # # Entering the Type of Component
        # print("Is this component of type= JOB")
        # print("If Yes then type 1, else anything else")
        # job = input()
        # if job == '1':
        #     data["components"][comp_name] = {"type": "job"}
        #     print("Select the Type of Job")
        #     print("Enter 1 for Normal Job")
        #     print("Enter 2 for Cron Job")
        #     job_ch = input()
        #     if job_ch == '1':
        #         job_type = 'normal job'
        #
        #     elif job_ch == '2':
        #         job_type = 'cron job'
        #         print("Do you want to add a CronJob")
        #         print("Enter 1 to Add else anything for not to")
        #         cron_ch = input()
        #         if cron_ch == '1':
        #             print("Enter the cron schedule in the specific Cron job format")
        #             cron_job = input()
        #             data["components"][comp_name] = {"cron_schedule": cron_job}
        #         else:
        #             data["components"][comp_name] = {"cron_schedule": ""}
        #
        # # Entering any command to run:
        # print("Do you want to Enter any Command")
        # print("Enter 1 to add or anything else not to")
        # command_ch = input()
        # if command_ch == '1':
        #     print("Enter the Command to be passed")
        #     command = input()
        #     data["components"][comp_name] = {"command": command}
        #
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
        #     data["components"][comp_name] = {"args": args_list}

        comp = {"replicas": replica_no, "build": build}
        return comp
