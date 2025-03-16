class SingleServer:
    __instance = None
    last_assigned_ip = int()
    activeConnections = {}
    staticIps = {}

    def getInstance(self):
        if SingleServer.__instance is None:
            SingleServer.__instance = SingleServer()
        return SingleServer.__instance

    def __init__(self):
        if SingleServer.__instance is not None:
            raise Exception("DHCP server already created")
        else:
            SingleServer.__instance = self
            self.startIp = int()
            self.endIp = int()


    def DHCPconfig(self, startIP, endIP):
        if 0 < startIP < 254:
            self.startIp = startIP
            SingleServer.lastAssignedIP = startIP
        else:
            print("Please enter valid start IP")
            return

        if 0 < endIP < 254:
            self.endIp = endIP
        else:
            print("Please enter valid end IP")
            return
        SingleServer.activeConnections.clear()
        SingleServer.staticIps.clear()

        pass

    @staticmethod
    def DHCPrequest(self, clientName):
        if clientName in SingleServer.staticIps.items():
            return SingleServer.staticIps[clientName]
        SingleServer.lastAssignedIP = SingleServer.lastAssignedIP + 1
        while True:
            if SingleServer.lastAssignedIP in SingleServer.staticIps:
                SingleServer.lastAssignedIP = SingleServer.lastAssignedIP + 1
        return SingleServer.lastAssignedIP

    @staticmethod
    def register_connection(clientName, IPAddress):
            SingleServer.activeConnections[clientName] = IPAddress

    @staticmethod
    def show_activeConnections():
        print("Active Connections:")
        for client_name, ip_address in SingleServer.activeConnections.items():
            print(f"{client_name}: {ip_address}")
    pass

    def assignStaticIp(clientName, ip):
        SingleServer.staticIps[clientName] = ip

