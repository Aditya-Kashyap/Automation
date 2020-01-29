from subprocess import *

print("Enter the Project name to be cloned")
pro_name = input()

command = 'git clone https://bitbucket.org/xpresso_teams_stage/' + pro_name + '.git'

git_clone = Popen(command, shell=True)
git_clone.wait()

print("Your Git files are cloned under the Path")
path = Popen('pwd')
path.wait()

