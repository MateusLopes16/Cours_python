# ticket_management.py

# Import necessary modules
from db import Db  # Import the database module
from Backlog import Backlog  # Import the backlog module
from GUI import GUI  # Import the graphical user interface module
from Tms import Tms  # Import the Ticket Management System module
from Interface import Interface  # Import the interface module

if __name__ == "__main__":
    # Initialize the database
    db = Db() # si vous voulez utiliser la base de données
    # db = Backlog() # si vous voulez utiliser la liste en mémoire
    
    # Initialize the graphical user interface
    gui = GUI() # si vous voulez utiliser l'interface graphique
    # gui = Interface() # si vous voulez utiliser l'interface en ligne de commande
    
    # Initialize the Ticket Management System with the database and GUI
    ticket_manager = Tms(db, gui)
    
    # Run the Ticket Management System
    ticket_manager.run()
