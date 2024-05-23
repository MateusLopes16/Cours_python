import unittest
import datetime
from tms_v5 import *

class TestTMS(unittest.TestCase):
    """
    Unit tests for the Ticket Management System (TMS).

    This class contains various test cases to ensure the correctness of the TMS functionalities.

    Attributes:
        db: An instance of the Backlog class.
        interface: An instance of the Interface class.
        ticket_manager: An instance of the Tms class.
        template (dict): A template dictionary representing a ticket.
    """
    def setUp(self):
        """
        Set up the test environment.

        This method is called before each test case to initialize required objects and variables.
        """
        self.db = Backlog()
        self.interface = Interface()
        self.ticket_manager = Tms(self.db, self.interface)
        self.template = {
            'id': 'Case-001',
            'name': 'IUT',
            'type': 'PR',
            'description': 'texte',
            'date_created': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'state': 'new',
            'responsible': 'L1'
        }

    def test_creation1(self):
        """
        Test ticket creation with valid inputs.

        This test case checks if a ticket is created successfully with valid input parameters.
        """
        self.ticket_manager.create_ticket('Case-001', 'IUT', 'texte', 'PR')
        self.assertEqual(self.db.get_all_tickets()[0], self.template)

    def test_creation2(self):
        """
        Test ticket creation with duplicate ID.

        This test case checks if attempting to create a ticket with a duplicate ID returns an empty dictionary.
        """
        self.ticket_manager.create_ticket('Case-001', 'IUT', 'texte', 'PR')
        self.assertEqual(self.db.get_all_tickets()[0], self.template)
        self.assertEqual(self.ticket_manager.create_ticket('Case-001', 'IUT', 'texte', 'PR'), {})

 
    def test_creation_id_error(self):
        """
        Test ticket creation with invalid ID format.

        This test case checks if an exception is raised when attempting to create a ticket with an invalid ID format.
        """
        with self.assertRaises(Exception):
            self.ticket_manager.create_ticket("002", "IUT", "texte", "PR")

    def test_creation_name_error(self):
        """
        Test ticket creation with invalid name.

        This test case checks if an exception is raised when attempting to create a ticket with an invalid name.
        """
        with self.assertRaises(Exception):
            self.ticket_manager.create_ticket("Case-002", "IUT 2", "texte", "PR")

    def test_creation_type_error(self):
        """
        Test ticket creation with invalid type.

        This test case checks if attempting to create a ticket with an invalid type returns an empty dictionary.
        """
        self.assertEqual(self.ticket_manager.create_ticket("Case-002", "IUT", "texte", "PR2"), {})

    def test_creation_empty_error(self):
        """
        Test ticket creation with empty fields.

        This test case checks if an exception is raised when attempting to create a ticket with empty fields.
        """
        with self.assertRaises(Exception):
            self.ticket_manager.create_ticket("", "IUT", "texte", "PR")
        with self.assertRaises(Exception):
            self.ticket_manager.create_ticket("Case-002", "", "texte", "PR")
        with self.assertRaises(Exception):
            self.ticket_manager.create_ticket("Case-002", "IUT", "", "PR")

    def test_assign1(self):
        """
        Test ticket assignment to a valid assignee.

        This test case checks if a ticket is successfully assigned to a valid assignee.
        """
        self.ticket_manager.create_ticket("Case-001", "IUT", "texte", "PR")
        self.ticket_manager.assign_ticket("Case-001", "L2", "analysis")
        self.assertEqual(self.db.get_all_tickets()[0]['responsible'], 'L2')

    def test_assign2(self):
        """
        Test ticket assignment with invalid ticket ID.

        This test case checks if attempting to assign a ticket with an invalid ticket ID returns False.
        """
        self.ticket_manager.create_ticket("Case-001", "IUT", "texte", "PR")
        self.assertFalse(self.ticket_manager.assign_ticket("Case-002", "L2", "analysis"))

    def test_close1(self):
        """
        Test ticket closure by a valid responsible.

        This test case checks if a ticket is successfully closed by a valid responsible.
        """
        self.ticket_manager.create_ticket("Case-001", "IUT", "texte", "PR")
        self.ticket_manager.assign_ticket("Case-001", "L2", "analysis")
        self.assertEqual(self.ticket_manager.close_ticket("Case-001"), {})

    def test_close2(self):
        """
        Test ticket closure with valid ticket ID.

        This test case checks if a ticket is successfully closed with a valid ticket ID.
        """
        self.ticket_manager.create_ticket("Case-001", "IUT", "texte", "PR")
        self.template['state'] = "closed"
        self.assertEqual(self.ticket_manager.close_ticket("Case-001"), self.template)


if __name__ == '__main__':
    unittest.main()
