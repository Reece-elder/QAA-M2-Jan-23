from service import Service

class Controller:
    service1 = Service()
    
    def startApp(self):
        # print("App Starting!")
        choice = input("What do you want to do..: ")
        print(choice)
        return self.service1.addToDB()
        # print(self.service2)

controller1 = Controller()

print(controller1.startApp())

