import PySimpleGUI as sg
from Interface import Interface

class GUI(Interface):
    """
    A class representing a Graphical User Interface (GUI) for managing tickets.

    Inherits from Interface class.

    Attributes:
        layout (list): A list containing the layout of the GUI.
        window (PySimpleGUI.Window): A window object for the GUI.
    """

    def __init__(self):
        """
        Initializes a GUI instance with the layout and window.
        """
        super().__init__()
        self.layout = [
            [sg.Text('Ticket Management System')],
            [sg.Button('Create Ticket'), sg.Button('Assign Ticket'), sg.Button('Close Ticket')],
            [sg.Button('Search Keyword'), sg.Button('Display Issue'), sg.Button('Exit')],
            [sg.Button('Old Tickets'), sg.Button('Closed Ticket Stats')]
        ]
        self.window = sg.Window('TMS GUI', self.layout)

    def choose_option(self):
        """
        Displays the GUI and waits for user input to choose an option.

        Returns:
            str: A string representing the chosen option.
        """
        while True:
            event, _ = self.window.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                return '6'
            elif event == 'Create Ticket':
                return '1'
            elif event == 'Assign Ticket':
                return '2'
            elif event == 'Close Ticket':
                return '3'
            elif event == 'Search Keyword':
                return '4'
            elif event == 'Display Issue':
                return '5'
            elif event == 'Old Tickets':
                return '7'
            elif event == 'Closed Ticket Stats':
                return '8'

    def print_one_ticket(self, ticket):
        """
        Displays information about a single ticket in a popup.

        Args:
            ticket (dict): A dictionary representing the ticket.
        """
        sg.popup(f"Ticket id: {ticket['id']}\nName: {ticket['name']}\nDescription: {ticket['description']}\nDate: {ticket['date_created']}\nState: {ticket['state']}\nResponsible: {ticket['responsible']}\nClosed Date: {ticket['closed_date']}")

    def raise_error(self, message):
        """
        Displays an error message in a popup.

        Args:
            message (str): The error message to display.
        """
        sg.popup_error(message)

    def display_issue_popup(self, message):
        """
        Displays a message in a popup.

        Args:
            message (str): The message to display.
        """
        sg.popup(message)

    def action_create_ticket(self):
        """
        Displays a window for creating a ticket and waits for user input.

        Returns:
            tuple: A tuple containing ticket information.
        """
        layout = [
            [sg.Text('Create Ticket')],
            [sg.Text('ID:'), sg.InputText(key='id')],
            [sg.Text('Name:'), sg.InputText(key='name')],
            [sg.Text('Description:'), sg.InputText(key='description')],
            [sg.Text('Type:'), sg.InputText(key='type')],
            [sg.Button('Create'), sg.Button('Cancel')],
        ]
        window = sg.Window('Create Ticket', layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancel'):
                window.close()
                return '', '', '', ''
            elif event == 'Create':
                window.close()
                return values['id'], values['name'], values['description'], values['type']

    def action_assign_ticket(self):
        """
        Displays a window for assigning a ticket and waits for user input.

        Returns:
            tuple: A tuple containing ticket ID, assignee name, and state.
        """
        layout = [
            [sg.Text('Assign Ticket')],
            [sg.Text('ID:'), sg.InputText(key='id')],
            [sg.Text('Assigned to:'), sg.InputText(key='assign_name')],
            [sg.Text('State:'), sg.InputText(key='state')],
            [sg.Button('Assign'), sg.Button('Cancel')],
        ]
        window = sg.Window('Assign Ticket', layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancel'):
                window.close()
                return '', '', ''
            elif event == 'Assign':
                window.close()
                return values['id'], values['assign_name'], values['state']

    def action_close_ticket(self):
        """
        Displays a window for closing a ticket and waits for user input.

        Returns:
            str: The ID of the ticket to be closed.
        """
        layout = [
            [sg.Text('Close Ticket')],
            [sg.Text('ID:'), sg.InputText(key='id')],
            [sg.Button('Close'), sg.Button('Cancel')],
        ]
        window = sg.Window('Close Ticket', layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancel'):
                window.close()
                return ''
            elif event == 'Close':
                window.close()
                return values['id']

    def action_search_keyword(self):
        """
        Displays a window for searching tickets by keyword and waits for user input.

        Returns:
            str: The keyword to search for.
        """
        layout = [
            [sg.Text('Search Tickets')],
            [sg.Text('Keyword:'), sg.InputText(key='keyword')],
            [sg.Button('Search'), sg.Button('Cancel')],
        ]
        window = sg.Window('Search Keyword', layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancel'):
                window.close()
                return ''
            elif event == 'Search':
                window.close()
                return values['keyword']
            
    def display_old_open_tickets(self, three_days_old_tickets, ten_days_old_tickets, twenty_days_old_tickets):
        """
        Displays tickets that are opened for 3-10-20 days in a popup.

        Args:
            three_days_old_tickets (list): A list of tickets opened for 3 days.
            ten_days_old_tickets (list): A list of tickets opened for 10 days.
            twenty_days_old_tickets (list): A list of tickets opened for 20 days.
        """
        layout = [
        [sg.Text('Tickets opened for 3 days with new state:')],
        [sg.Listbox(values=[f"ID: {ticket['id']}" for ticket in three_days_old_tickets], size=(30, min(len(three_days_old_tickets), 5)), key='three_days_tickets')],
        [sg.Text('Tickets opened for 10 days with assigned or analysis state:')],
        [sg.Listbox(values=[f"ID: {ticket['id']}" for ticket in ten_days_old_tickets], size=(30, min(len(ten_days_old_tickets), 5)), key='ten_days_tickets')],
        [sg.Text('Tickets opened for 20 days with any state:')],
        [sg.Listbox(values=[f"ID: {ticket['id']}" for ticket in twenty_days_old_tickets], size=(30, min(len(twenty_days_old_tickets), 5)), key='twenty_days_tickets')],
        [sg.Button('OK')]
    ]

        window = sg.Window('Old Open Tickets', layout)

        while True:
            event, _ = window.read()

            if event == sg.WIN_CLOSED or event == 'OK':
                window.close()
                break
            
    def display_closed_tickets_stats(self, three_days_closed_tickets, between_three_ten_days_closed_tickets, more_than_ten_days_closed_tickets):
        """
        Displays statistics about closed tickets in a popup.

        Args:
            three_days_closed_tickets (list): A list of tickets closed within 3 days.
            between_three_ten_days_closed_tickets (list): A list of tickets closed between 3 and 10 days.
            more_than_ten_days_closed_tickets (list): A list of tickets closed after 10 days.
        """
        layout = [
        [sg.Text('Tickets closed within 3 days:')],
        [sg.Listbox(values=[f"ID: {ticket['id']}" for ticket in three_days_closed_tickets], size=(30, min(len(three_days_closed_tickets), 5)), key='three_days_closed_tickets')],
        [sg.Text('Tickets closed between 3 and 10 days:')],
        [sg.Listbox(values=[f"ID: {ticket['id']}" for ticket in between_three_ten_days_closed_tickets], size=(30, min(len(between_three_ten_days_closed_tickets), 5)), key='between_three_ten_days_closed_tickets')],
        [sg.Text('Tickets closed after 10 days:')],
        [sg.Listbox(values=[f"ID: {ticket['id']}" for ticket in more_than_ten_days_closed_tickets], size=(30, min(len(more_than_ten_days_closed_tickets), 5)), key='more_than_ten_days_closed_tickets')],
        [sg.Button('OK')]
    ]

        window = sg.Window('Closed Ticket Stats', layout)

        while True:
            event, _ = window.read()

            if event == sg.WIN_CLOSED or event == 'OK':
                window.close()
                break
