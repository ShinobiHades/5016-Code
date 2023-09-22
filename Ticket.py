class Ticket:
    tickCount = 0
    L=[]
    openTick=0
    closedTick=0

    def __init__(self):
        self.ID=" "
        self.name=" "
        self.Email=" "
        self.Desc=" "
        self.Status=" "
        self.Response=" "
        while True:
            func_input=str(input("enter what you would like to do: "))
            if func_input.strip() == "create":
                a=self.ticket()
            elif func_input.strip() == "display":
                self.display()
            else:
                print("that is not a valid command")
    # create a ticket object
    def ticket(self):
        self.ID = str(input("Enter your staff ID: "))
        self.Name = str(input("Enter your name: "))
        self.Email = str(input("Enter your contact email: "))
        self.Desc = str(input("Enter a description of your issue: "))
        Ticket.tickCount += 1
        self.tickNumber = Ticket.tickCount + 2000
        self.Status = "Open"
        self.Response = "Not yet provided"
        self.openTick +=1
        if self.Desc.strip() == "password change":
            newPass = self.ID[0:2]+self.Name[0:3]
            self.Response = newPass
            self.Status = "Closed"
            self.openTick -= 1
            self.closedTick += 1
        self.L.append(self)
    #get the required ticket info to display later, does not work due to using the self. parts using the latest ticket data
    def displayprep(self):
        print("Ticket Number: ",self.tickNumber)
        print("Staff ID: ",self.ID)
        print("Name: ",self.Name)
        print("Email: ",self.Email)
        print("Issue description: ",self.Desc)
        print("Response: ",self.Response)
        print("Status: ",self.Status)
    #display all the ticket info one after the other following a status count
    def display(self):
        print("-------------------------------")
        print("Tickets created: ",self.tickCount)
        print("Open tickets: ",self.openTick)
        print("Closed tickets: ",self.closedTick)
        print("-------------------------------")
        for i in range(self.tickCount):
            print("-------------------------------")
            self.L[i].displayprep()
            print("-------------------------------")
                
