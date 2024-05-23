import re
import datetime

class Tms:
     """
    The Ticket Management System class.

    This class handles various operations related to ticket management.

    Attributes:
        backlog_manager: The object managing the backlog.
        interface: The interface object for user interaction.
    """
     def __init__(self, backlog_manager, interface):
          """
        Initializes the Ticket Management System.

        Args:
            backlog_manager: The object managing the backlog.
            interface: The interface object for user interaction.
        """
          self.backlog_manager = backlog_manager
          self.interface = interface

     def create_ticket(self, id, name, description, type):
          """
        Creates a new ticket.

        Args:
            id (str): The ID of the ticket.
            name (str): The name of the ticket.
            description (str): The description of the ticket.
            type (str): The type of the ticket.

        Returns:
            dict: A dictionary representing the created ticket.
        """
          validTypes = ["PR", "IR"]
          if (type not in validTypes):
               self.interface.display_issue_popup("Type is not valid. Please enter PR or IR")
               return {}
          if (not re.match("^Case-\d\d\d$", id)):
               self.interface.raise_error("ID is not in format Case-XXX where X represents a digit.")
               return {}
          if (len(id) == 0 or len(name) == 0 or len(description) == 0):
               self.interface.raise_error("One or more fields are empty, please fill all the details.")
               return {}
          if (not re.match("^\w+$", name)):
               self.interface.raise_error("Name is not alphanumeric.")
               return {}
          for ticket in self.backlog_manager.get_all_tickets():
               if ticket and ticket['id'] == id:
                    self.interface.display_issue_popup("Ticket already exists")
                    return {}
          ticket = {
              'id': id,
              'name': name,
              'type': type,
              'description': description,
              'date_created': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
              'state': 'new',
              'responsible': 'L1',
              'closed_date': ''
          }
          self.backlog_manager.create_ticket(ticket)
          self.interface.display_issue_popup("Create ticket {}".format(id))
          return ticket

     def close_ticket(self, case_id):
          """
        Closes the specified ticket.

        Args:
            case_id (str): The ID of the ticket to close.

        Returns:
            dict: A dictionary representing the closed ticket.
        """
          for ticket in self.backlog_manager.get_all_tickets():
               if ticket['id'] == case_id and ticket['responsible'] == "L1":
                    ticket['state'] = "closed"
                    ticket['closed_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    return self.backlog_manager.close_ticket(ticket)
               elif ticket['id'] == case_id and ticket['responsible'] != "L1":
                    self.interface.display_issue_popup("Only L1 can close the ticket")
                    return {}
          self.interface.display_issue_popup("Invalid id: ticket not found")
          return {}

     def assign_ticket(self, case_id, case_assign, state):
          """
        Assigns the specified ticket to an assignee.

        Args:
            case_id (str): The ID of the ticket.
            case_assign (str): The assignee of the ticket.
            state (str): The state of the ticket.

        Returns:
            bool: True if the ticket was successfully assigned, False otherwise.
        """
          validStates = ["analysis", "assigned", "solved", "in_deliver", "closed"]
          validOwners = ["L1", "L2", "L3"]

          if (state not in validStates):
               self.interface.display_issue_popup("State is not valid. Please enter analysis, assigned, solved, in_deliver, or closed")
               return False
          if (case_assign not in validOwners):
               self.interface.display_issue_popup("Assignee is not valid. Please enter L1, L2, or L3")
               return False
          self.interface.display_issue_popup("Assign ticket {} to {}".format(case_id,case_assign))
          for ticket in self.backlog_manager.get_all_tickets():
               if ticket['id']==case_id:
                    ticket['state'] = state
                    ticket['responsible'] = case_assign
                    self.backlog_manager.update_ticket(ticket)
                    return True
          self.interface.display_issue_popup("Invalid id {} : ticket does not exists".format(case_id))
          return False

     def print_one_ticket(self, case_id):
          """
        Prints information about the specified ticket.

        Args:
            case_id (str): The ID of the ticket to print.

        Returns:
            bool: True if the ticket was found and printed, False otherwise.
        """
          for ticket in self.backlog_manager.get_all_tickets():
               if ticket['id'] == case_id:
                    self.interface.print_one_ticket(ticket)
                    return True
          self.interface.display_issue_popup("Invalid id: ticket not found")
          return False

     def search_tickets(self, keyword):
          """
        Searches for tickets based on the provided keyword.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            bool: True if at least one ticket matching the keyword was found, False otherwise.
        """
          found = False
          for ticket in self.backlog_manager.get_all_tickets():
               if (keyword in str(ticket['id']) or keyword in ticket['type'] or keyword in ticket['name'] or keyword in ticket['description'] or
                    keyword in str(ticket['date_created']) or keyword in ticket['state'] or keyword in ticket['responsible']):
                    self.print_one_ticket(ticket['id'])
                    found = True
          if not found:
               self.interface.display_issue_popup("Keyword {} not found".format(keyword))
          return found
     
     def get_old_open_tickets(self):
          """
          Retrieves tickets that are opened for 3-10-20 days.
          """
          three_days_old_tickets = self.backlog_manager.get_open_tickets_by_state_and_date(3, ['new'])
          ten_days_old_tickets = self.backlog_manager.get_open_tickets_by_state_and_date(10, ['assigned', 'analysis'])
          twenty_days_old_tickets = self.backlog_manager.get_open_tickets_by_state_and_date(20)
          
          self.interface.display_old_open_tickets(three_days_old_tickets, ten_days_old_tickets, twenty_days_old_tickets)
          
     def get_closed_tickets_between_days(self):
          """
          Retrieves statistics about closed tickets.
          """
          three_days_closed_tickets = self.backlog_manager.get_closed_tickets_between_days(0, 3)
          between_three_ten_days_closed_tickets = self.backlog_manager.get_closed_tickets_between_days(3, 10)
          more_than_ten_days_closed_tickets = self.backlog_manager.get_closed_tickets_between_days(10)

          self.interface.display_closed_tickets_stats(three_days_closed_tickets, between_three_ten_days_closed_tickets, more_than_ten_days_closed_tickets)
     
     def run(self):
          """
        Runs the Ticket Management System.

        This method continuously prompts the user for input and performs actions based on the chosen option.
        """
          while True:
               val = self.interface.choose_option()
               if val == '1':
                    id, name, description, type = self.interface.action_create_ticket()
                    self.create_ticket(id, name, description, type)
               elif val == '2':
                    id, assign_name, state = self.interface.action_assign_ticket()
                    self.assign_ticket(id, assign_name, state)
               elif val == '3':
                    id = self.interface.action_close_ticket()
                    issue = self.close_ticket(id)
                    if issue != {}:
                         self.interface.display_issue_popup("Ticket closed successfully!")
               elif val == '4':
                    keyword = self.interface.action_search_keyword()
                    self.search_tickets(keyword)
               elif val == '5':
                    id = self.interface.action_close_ticket()
                    self.print_one_ticket(id)
               elif val == '6':
                    break
               elif val == '7':
                    self.get_old_open_tickets()
               elif val == '8':
                    self.get_closed_tickets_between_days()
               else:
                    self.interface.display_issue_popup("Invalid option")