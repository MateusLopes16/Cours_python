class Interface:
    """
    A class representing a text-based interface for managing tickets.
    """

    def __init__(self):
        """
        Initializes an Interface instance.
        """
        pass
        
    def choose_option(self):
        """
        Displays a menu of options and waits for user input.

        Returns:
            str: The user's selection.
        """
        print("\n1. Create a ticket")
        print("2. Assign a ticket")
        print("3. Close a ticket")
        print("4. Search keyword")
        print("5. Display issue from backlog")
        print("6. Exit")
        print("7. Old Tickets")
        print("8. Closed Stats")
        val = input("\nEnter your selection: ")
        return val
    
    def print_one_ticket(self, ticket):
        """
        Prints information about a single ticket.

        Args:
            ticket (dict): A dictionary representing the ticket.
        """
        if (ticket == {}):
            print("Invalid id: ticket not found")
            return
        print("Ticket id: ", ticket['id'])
        print("Name: ", ticket['name'])
        print("description: ", ticket['description'])
        print("Date: ", ticket['date'])
        print("State: ", ticket['state'])
        print("Responsible: ", ticket['responsible'])
        print("Closed Date: ", ticket['closed_date'])
        
    def raise_error(self, message):
        """
        Raises an exception with the given message.

        Args:
            message (str): The error message.
        """
        raise Exception(message)
    
    def display_issue_popup(self, message):
        """
        Displays a message to the user.

        Args:
            message (str): The message to display.
        """
        print(message)
    
    def action_create_ticket(self):
        """
        Prompts the user to enter ticket information.

        Returns:
            tuple: A tuple containing ticket information.
        """
        id = input("ID: ")
        name = input("Name: ")
        description = input("Description: ")
        type = input("Type: ")
        return id, name, description, type
    
    def action_assign_ticket(self):
        """
        Prompts the user to assign a ticket.

        Returns:
            tuple: A tuple containing ticket ID, assignee name, and state.
        """
        id = input("ID: ")
        assign_name = input("Assigned to: ")
        state = input("State: ")
        return id, assign_name, state
    
    def action_close_ticket(self):
        """
        Prompts the user to enter the ID of the ticket to close.

        Returns:
            str: The ID of the ticket to close.
        """
        return input("ID: ")
    
    def action_search_keyword(self):
        """
        Prompts the user to enter a keyword to search for.

        Returns:
            str: The keyword to search for.
        """
        return input("Keyword: ")

    def display_old_open_tickets(self, three_days_old_tickets, ten_days_old_tickets, twenty_days_old_tickets):
        """
        Displays tickets that are 3, 10, and 20 days old.

        Args:
            three_days_old_tickets (list): A list of tickets that are 3 days old.
            ten_days_old_tickets (list): A list of tickets that are 10 days old.
            twenty_days_old_tickets (list): A list of tickets that are 20 days old.
        """
        print("\nTickets opened for 3 days with new state:")
        for ticket in three_days_old_tickets:
            print(ticket['id'])
        print("\nTickets opened for 10 days with assigned or analysis state:")
        for ticket in ten_days_old_tickets:
            print(ticket['id'])
        print("\nTickets opened for 20 days with any state:")
        for ticket in twenty_days_old_tickets:
            print(ticket['id'])
            
    def display_closed_tickets_stats(self, three_days_closed_tickets, between_three_ten_days_closed_tickets, more_than_ten_days_closed_tickets):
        """
        Displays statistics about closed tickets in a popup.

        Args:
            three_days_closed_tickets (list): A list of tickets closed within 3 days.
            between_three_ten_days_closed_tickets (list): A list of tickets closed between 3 and 10 days.
            more_than_ten_days_closed_tickets (list): A list of tickets closed after 10 days.
        """
        print("\nTickets closed within 3 days:")
        for ticket in three_days_closed_tickets:
            print(ticket['id'])
        print("\nTickets closed between 3 and 10 days:")
        for ticket in between_three_ten_days_closed_tickets:
            print(ticket['id'])
        print("\nTickets closed after 10 days:")
        for ticket in more_than_ten_days_closed_tickets:
            print(ticket['id'])
        