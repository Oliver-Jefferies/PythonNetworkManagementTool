#from AdminFactory import UserFactory
from levelAdminFactory import AdminFactory
#from singleServer import SingleServer

# Create lists for users
admins=["Roger"]
normalUsers=["John", "Joe"]
beginners=["Aaron"]

#Create User Introduction and give Options
while True:
    print ("Welcome to the network admin application")
    print ("What tasks do you need performed?")
    print("")
    print("Press 1 for DHCP Configuration")
    print("Press 2 for Static IP Configuration")
    print("Press 3 for End User System Updates")
    print("Press 4 for DNS Configurations")
    print("Press 5 for End User System Updates")
    print("Press 0 to exit")
    print("")
    
    #Prompt the user for choice of task
    choice = int(input("What task do you want to perform?: "))
        # If the user chooses DHCP, prompt user for their priority
    if choice == 1:
        #Prompt user for name, depending on what list they are in, create a respective admin class
        name = input("Enter your name: ")
        if name in admins:
            admin = AdminFactory.buildAdmin(15)
            print("You have the correct priority level for all DHCP Configurations ")
            
            while True:
                task = input("Press d for Request DHCP address \nPress b for DHCP Pool Configuration \nPress 0 for exit  ")
                  
                if task == "d":
                    admin.dhcpRequest()

                    
                elif task == "b":
                    startIP = (int(input("Enter start IP for DHCP Pool: ")))
                    endIP = (int(input("Enter end IP for DHCP Pool:")))
                    admin.dhcpConfig(startIP,endIP)
                
                else:
                    break
                
                
        if name in normalUsers:
            admin = AdminFactory.buildAdmin(1)
            print("You have the priority level to perform the following actions ")
            task = input(" Press d for Request DHCP address \nPress 0 for exit  ")
            if task == "d":
                admin.dhcpRequest()    
            else:
                break
            
        else:
            print("You dont have access to these configurations")
            print("")
                
                

            

