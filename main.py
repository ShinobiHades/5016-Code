from Ticket import * # used to import all the functions from the ticket file


# the main class to get user inputs and load the correct funtions in the ticket file
def main():
    user_choice = ""
    while user_choice != "exit":
        user_choice = input("What would you like to do? \n"
                            "<Create> new ticket,\n"
                            "Display <all> tickets,\n"
                            "<Display> one ticket,\n"
                            "<Respond> to a ticket,\n"
                            "<Reopen> a ticket, \n"
                            "Show <Statistics>.\n"
                            "> ")
        if user_choice.lower() == "create":
            create() # used to load up the ticket creation functions
        elif user_choice.lower() == "display":
            user_choice = input("Which ticket would you like to view? (Enter ticket number) \n> ")
            ticket = ticket_search(user_choice)
            display(ticket) # used to display a single ticket's data
        elif user_choice.lower() == "all":
            display_all() # used to display the ticket data for all created tickets
        elif user_choice.lower() == "respond":
            user_choice = input("Which ticket would you like to respond? (Enter ticket number) \n> ")
            ticket = ticket_search(user_choice)
            respond(ticket) # used to load up the respond function to respond to a created ticket
        elif user_choice.lower() == "reopen":
            user_choice = input("Which ticket would you like to reopen? (Enter ticket number) \n> ")
            ticket = ticket_search(user_choice)
            reopen(ticket) # used to reopen a ticket
        elif user_choice.lower() == "statistics":
            show_statistics() # used to show the overall statistics for tickets, total number and how many tickets are open or closed
        else:
            print("Please enter a valid option. :< \n") # a check to make sure that a valid input is made


# loads the function above making the entire program work
main()
print("Thank you for using this ticket system!")
