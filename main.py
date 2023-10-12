from Ticket import *


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
            create()
        elif user_choice.lower() == "display":
            user_choice = input("Which ticket would you like to view? (Enter ticket number) \n> ")
            ticket = ticket_search(user_choice)
            display(ticket)
        elif user_choice.lower() == "all":
            display_all()
        elif user_choice.lower() == "respond":
            user_choice = input("Which ticket would you like to respond? (Enter ticket number) \n> ")
            ticket = ticket_search(user_choice)
            respond(ticket)
        elif user_choice.lower() == "reopen":
            user_choice = input("Which ticket would you like to reopen? (Enter ticket number) \n> ")
            ticket = ticket_search(user_choice)
            reopen(ticket)
        elif user_choice.lower() == "statistics":
            show_statistics()
        else:
            print("Please enter a valid option. :< \n")


main()
print("Thank you for using this ticket system!")
