from service import service

class controller:
    service1 = service()
    
    def startApp(self):
        print("App Starting!")
        choice = input("What do you want to do..: ")
        print(choice)
        print(self.service1.addToDB())
        # print(self.service2)

controller1 = controller()

controller1.startApp()

