class Ticket:
    counter = 2000  # static counter for ticket number calculation

    # used to commit entered data to a new ticket
    def __init__(self, staff_ID, name, email, description):
        self.Ticket_Number = Ticket.counter + 1
        Ticket.counter += 1
        self.StaffID = staff_ID
        self.Name = name
        self.Email = email
        self.Description = description
        self.Response = "Not yet provided"
        self.Status = "Open"
        # code to check if the ticket is for a password change
        if self.Description.lower() == "password change":
            generated_password = self.StaffID[0:2]+self.Name[0:3]
            self.Response = "New Password has been generated: " + generated_password
            self.Status = "Closed"


ticket_list = []
# ticket testing code
# ticket1 = Ticket("MARIAH", "Mariah", "Mariah@whitecliffe.ac.nz", "Monitor not working")
# ticket_list.append(ticket1)
# ticket2 = Ticket("INNA", "Inna", "inna@whitecliffe.ac.nz", "Password change")
# ticket_list.append(ticket2)
# ticket3 = Ticket("JOHNS", "John", "john@whitecliffe.ac.nz", "Request for a video-camera for conferences")
# ticket_list.append(ticket3)


# code to pull up specific tickets
def ticket_search(ticket_num):
    for t in ticket_list:
        if t.Ticket_Number == int(ticket_num):
            return t


# used to calculate the number of open and closed tickets
def show_statistics():
    tickets_open = 0
    tickets_closed = 0
    for t in ticket_list:
        if t.Status == "Open" or t.Status == "Reopened":
            tickets_open += 1
        elif t.Status == "Closed":
            tickets_closed += 1
    print(f"Tickets open: {tickets_open}")
    print(f"Tickets Closed: {tickets_closed}")
    print(f"Total Tickets: {tickets_open + tickets_closed}")


# used to display the ticket data for a single ticket
def display(ticket):
    print(f"Ticket Number: {ticket.Ticket_Number}")
    print(f"StaffID: {ticket.StaffID}")
    print(f"Name: {ticket.Name}")
    print(f"Email: {ticket.Email}")
    print(f"Description: {ticket.Description}")
    print(f"Response: {ticket.Response}")
    print(f"Status: {ticket.Status}")


# used to display the ticket data for all tickets
def display_all():
    for t in ticket_list:
        print(f"Ticket Number: {t.Ticket_Number}")
        print(f"StaffID: {t.StaffID}")
        print(f"Name: {t.Name}")
        print(f"Email: {t.Email}")
        print(f"Description: {t.Description}")
        print(f"Response: {t.Response}")
        print(f"Status: {t.Status}")
    show_statistics()


# used to have techs respond to created tickets
def respond(ticket):
    response = input("How would you like to respond to this ticket? \n > ")
    ticket.Response = response
    close = input("Would you like to close this ticket? y/n \n >")
    if close.lower() == "y":
        ticket.Status = "Closed"
    display(ticket)


# used to reopen a ticket
def reopen(ticket):
    ticket.Status = "Reopened"
    display(ticket)


# used to create a new ticket
def create():
    staff_ID = input("Enter staff ID: ")
    name = input("Enter name: ")
    email = input("Enter email: ")
    description = input("Enter description of issue: ")
    new_ticket = Ticket(staff_ID, name, email, description)
    ticket_list.append(new_ticket)
    display(new_ticket)
