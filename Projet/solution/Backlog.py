from datetime import datetime, timedelta


class Backlog:
    """
    A class representing a backlog of tickets.

    Attributes:
        backlog (list): A list containing all open tickets.
        closed_backlog (list): A list containing all closed tickets.
    """

    def __init__(self):
        """
        Initializes a Backlog instance with empty lists for backlog and closed_backlog.
        """
        self.backlog = []
        self.closed_backlog = []

    def create_ticket(self, ticket):
        """
        Creates a new ticket and adds it to the backlog.

        Args:
            ticket (dict): A dictionary representing the ticket to be created.
        """
        self.backlog.append(ticket)

    def remove_ticket(self, ticket_id):
        """
        Removes a ticket with the specified ID from the backlog.

        Args:
            ticket_id (int): The ID of the ticket to be removed.
        """
        for ticket in self.backlog:
            if ticket['id'] == ticket_id:
                self.backlog.remove(ticket)

    def close_ticket(self, close_ticket):
        """
        Closes a ticket with the specified ID.

        Args:

        Returns:
            dict: The closed ticket, if found, otherwise an empty dictionary.
        """
        for ticket in self.backlog:
            if ticket['id'] == close_ticket['id']:
                self.backlog.remove(close_ticket)
                self.closed_backlog.append(close_ticket)
                return close_ticket
        return {}

    def update_ticket(self, ticket):
        """
        Updates an existing ticket in the backlog.

        Args:
            ticket (dict): A dictionary representing the updated ticket.
        """
        for i in range(len(self.backlog)):
            if self.backlog[i]['id'] == ticket['id']:
                self.backlog[i] = ticket
                return

    def get_all_tickets(self):
        """
        Retrieves all tickets from the backlog.

        Returns:
            list: A list containing all open tickets.
        """
        return self.backlog
    
    def get_open_tickets_by_state_and_date(self, days, states=["analysis", "assigned", "solved", "in_deliver"]) :
        """
        Retrieves all tickets from the backlog older than a certain number of days.

        Args:
            days (int): The number of days.
            states (list): The list of states to filter the tickets.

        Returns:
            list: A list containing all open tickets older than the specified number of days in a certain state.
        """
        old_tickets = []
        for ticket in self.backlog:
            if (datetime.now() - ticket['date']) > timedelta(days=days) and ticket['state'] in states:
                old_tickets.append(ticket)
        return old_tickets
    
    def get_closed_tickets_between_days(self, min_days, max_days=None) :
        """
        Retrieves closed tickets from the closed backlog within a range of days.

        Args:
            min_days (int): The minimum number of days since the ticket was closed.
            max_days (int, optional): The maximum number of days since the ticket was closed (default: None).
                If provided, only tickets closed within this range (inclusive of both ends) will be retrieved.
                If None, tickets closed at least min_days ago will be retrieved.

        Returns:
            list: A list containing closed tickets that meet the specified criteria.

        Note:
            If max_days is None, the function retrieves tickets closed at least min_days ago without an upper limit.
            Otherwise, it retrieves tickets closed within the range [min_days, max_days].
        """
        closed_tickets = []
        for ticket in self.closed_backlog:
            days_difference = datetime.now() - ticket['closed_date']
            if days_difference.days > min_days and (max_days is None or days_difference.days <= max_days) and ticket['state'] == "closed":
                closed_tickets.append(ticket)
        return closed_tickets