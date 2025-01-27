from singleServer import SingleServer
class L15Access:
    def __init__(self,name):
        self.name = name
        self.level = 15
        
    def dhcpConfig(self,startIP,endIP):
        SingleServer.DHCPconfig(startIP,endIP)
    
    def dhcpRequest(self):
        SingleServer.DHCPrequest()
        
    def dnsConfig(self):
        pass
    
    def powerOn(self):
        pass
        
    def powerOff(self):
        pass
    
    def UpdateAll(self):
        pass
        
        
class L1Access:
    def __init__(self,name):
        self.name = name
        self.level = 1
        
    def dhcpRequest(self):
        SingleServer.DHCPrequest()
        
    def dnsRequest(self):
        pass
        
    def UpdateAll(self):
        pass
    
    def powerOn(self):
        pass
        
    def powerOff(self):
        pass
 

class L0Access:
    def __init__(self,name):
        self.name = name
        self.level = 0
        
    def powerOn(self):
        pass
        
    def powerOff(self):
        pass
    
    def UpdateAll(self):
        pass
        
        
        
class AdminFactory:
    @staticmethod
    def buildAdmin(priority):
        if priority == 0:
            return L0Access("default")
        if priority == 1:
            return L1Access("default")
        if priority == 15:
            return L15Access("default")
        else:
            print("invalid priority")       
    
        
    