import psycopg2
from Backlog import Backlog
from datetime import datetime, timedelta

class Db(Backlog):
    """
    A class representing a database interface for managing tickets.

    Inherits from Backlog class.

    Attributes:
        conn (psycopg2.connection): A connection to the PostgreSQL database.
        cur (psycopg2.cursor): A cursor for executing database operations.
    """

    def __init__(self):
        """
        Initializes a Db instance and creates a connection to the database.
        """
        super().__init__()
        self.conn = psycopg2.connect(host="localhost", dbname="nomDeLaBase", user="postgres_user", password="mysecretpassword")
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates necessary tables in the database if they don't already exist.
        """
        create_table_sql = """
        
            CREATE TABLE IF NOT EXISTS Tickets (
            id VARCHAR(8) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            type VARCHAR(2) NOT NULL CHECK (type IN ('PR', 'IR')),
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            state VARCHAR(20) NOT NULL DEFAULT 'new' CHECK (state IN ('new', 'analysis', 'assigned', 'solved', 'in_deliver', 'closed')),
            responsible VARCHAR(2) NOT NULL CHECK (responsible IN ('L1', 'L2', 'L3')),
            closed_date TIMESTAMP
            );
        """
        self.cur.execute(create_table_sql)
        self.conn.commit()

    def create_ticket(self, ticket):
        """
        Creates a new ticket in the database.

        Args:
            ticket (dict): A dictionary representing the ticket to be created.

        Returns:
            int: The ID of the created ticket.
        """
        insert_ticket_sql = """
            INSERT INTO Tickets (id, name, description, type, state, responsible)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id;
        """
        self.cur.execute(insert_ticket_sql, (
             ticket['id'],
            ticket['name'],
            ticket['description'],
            ticket['type'],
            ticket['state'],
            ticket['responsible']
        ))
        self.conn.commit()
        return ticket['id']

    def update_ticket(self, ticket):
        """
        Updates an existing ticket in the database.

        Args:
            ticket (dict): A dictionary representing the updated ticket.
        """
        update_ticket_sql = """
            UPDATE Tickets
            SET name = %s, description = %s, type = %s, state = %s, responsible = %s
            WHERE id = %s;
        """
        self.cur.execute(update_ticket_sql, (
            ticket['name'],
            ticket['description'],
            ticket['type'],
            ticket['state'],
            ticket['responsible'],
            ticket['id']
        ))
        self.conn.commit()

    def close_ticket(self, ticket):
        """
        Closes a ticket in the database.

        Args:
            ticket_id (int): The ID of the ticket to be closed.

        Returns:
            dict: The closed ticket.
        """
        close_ticket_sql = """
            UPDATE Tickets
            SET state = 'closed', closed_date = CURRENT_TIMESTAMP
            WHERE id = %s;
        """
        self.cur.execute(close_ticket_sql, (ticket['id'],))
        self.conn.commit()
        return ticket

    def get_all_tickets(self):
        """
        Retrieves all tickets from the database.

        Returns:
            list: A list containing dictionaries representing all tickets.
        """
        get_all_tickets_sql = """
            SELECT * FROM Tickets;
        """
        self.cur.execute(get_all_tickets_sql)
        rows = self.cur.fetchall()

        tickets = []
        columns = [desc[0] for desc in self.cur.description]
        for row in rows:
            ticket = dict(zip(columns, row))
            tickets.append(ticket)
        return tickets
    
    def get_open_tickets_by_state_and_date(self, days, states=["analysis", "assigned", "solved", "in_deliver"]):
        """
        Retrieves all tickets from the backlog older than a certain number of days.

        Args:
            days (int): The number of days.
            states (list): The list of states to filter the tickets.

        Returns:
            list: A list containing all open tickets older than the specified number of days in a certain state.
        """
        open_tickets = []
        query = """
            SELECT * FROM Tickets WHERE date_created < %s AND state IN %s;
        """
        date_threshold = datetime.now() - timedelta(days=days)
        self.cur.execute(query, (date_threshold, tuple(states)))
        rows = self.cur.fetchall()

        columns = [desc[0] for desc in self.cur.description]
        for row in rows:
            ticket = dict(zip(columns, row))
            open_tickets.append(ticket)
        return open_tickets

    def get_closed_tickets_between_days(self, min_days, max_days=None):
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
        query = """
            SELECT * FROM Tickets WHERE state = 'closed' AND closed_date <= CURRENT_DATE - INTERVAL '%s days';
        """
        if max_days is not None:
            query = """
                SELECT * FROM Tickets WHERE state = 'closed' AND closed_date >= CURRENT_DATE - INTERVAL '%s days' AND closed_date <= CURRENT_DATE - INTERVAL '%s days' + INTERVAL '1 days';
            """
            self.cur.execute(query, (max_days, min_days))
        else:
            self.cur.execute(query, (min_days,))

        rows = self.cur.fetchall()

        columns = [desc[0] for desc in self.cur.description]
        for row in rows:
            ticket = dict(zip(columns, row))
            closed_tickets.append(ticket)
        return closed_tickets
