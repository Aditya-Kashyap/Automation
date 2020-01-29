from subprocess import *


class LoginClass:
    # def __init__(self):
    #     self.u_id = u_id

    @staticmethod
    def get_user_credentials(self):
        print('Please Enter the User ID \n')
        u_id = input()

        print('\nPlease enter the Work Space which you want to work in:\n ')
        self.work_env = input()

    @staticmethod
    def run_login_command(self):
        login_command_string = 'xprctl login -u ' + self.u_id + ' ' + '-w ' + self.work_env

        print('\nYour Login Command\n')
        print(login_command_string)

        login = Popen(login_command_string, shell=True)
        login.wait()


user_login = LoginClass()
user_login.get_user_credentials()
