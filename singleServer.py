class SingleServer:
    __instance = None

    def getInstance(self):
        if SingleServer.__instance is None:
            SingleServer.__instance = SingleServer()
        return SingleServer.__instance

    def __init__(self):
        if SingleServer.__instance is not None:
            raise Exception("DHCP server already created")
        else:
            SingleServer.__instance = self

    def DHCPconfig(self, startIP, endIP):
        pass

    def DHCPrequest(self):
        pass