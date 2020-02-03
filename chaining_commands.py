from subprocess import *


print("Hello Welcome to Xpresso")
print("Your First Command: xprctl -h/xprctl --help:\n")
print("This will give the all the help you need with the xprctl commands in Xpresso\n")
xpresso = Popen('xprctl -h ', shell=True)

xpresso.wait()

status = xpresso.poll()

if status == 0:
    print("\n____________END OF 1st INPUT__________________\n")
    print("Your Second Input Command: xprctl list :\n ")
    print("It will give the List details of the commands present in Xpresso\n")
    xpresso = Popen('xprctl list', shell=True)
    xpresso.wait()
    status1 = xpresso.poll()

    if status1 == 0:
        print("\n____________END OF 2st INPUT__________________\n")
        print("Your Last Command: xprctl info: \n")
        print("Gives the Info of all the services present in Xpresso with their IP's\n")
        xpresso = Popen('xprctl info ', shell=True)
        xpresso.wait()
        print("\n____________END OF 3rd INPUT__________________\n")
        print("Have a Good Day! Bye from Xpresso")

    else:
        print("Wrong 2rd Input")

else:
    print("Wrong 1st Input")