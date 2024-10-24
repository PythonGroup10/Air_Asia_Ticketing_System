import DBBase as airDB #Used to import the Database class

class AirAsiaDatabase(airDB.DBBase):
    def __init__(self):
        super().__init__("airasiadb.sqlite") #Creates the database in SQLite

    def reset_database(self): #This section will create the actual tables in our database
        try:
            drop_sql = """ 
                DROP TABLE IF EXISTS Customer; 
                DROP TABLE IF EXISTS Flight; 
                DROP TABLE IF EXISTS Ticket;
                DROP TABLE IF EXISTS Employee; 
                DROP TABLE IF EXISTS Airport; 
            """
            super().execute_script(drop_sql)
            create_sql = """
                CREATE TABLE Customer (
                    customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    first_name TEXT NOT NULL, 
                    last_name TEXT NOT NULL, 
                    dob DATE NOT NULL, 
                    citizenship TEXT NOT NULL, 
                    email TEXT,
                    username VARCHAR(128) NOT NULL UNIQUE,
                    password BINARY NOT NULL
                );
            
                CREATE TABLE Airport(
                    airport_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    airport_code TEXT NOT NULL UNIQUE,
                    airport_name TEXT NOT NULL, 
                    city TEXT NOT NULL, 
                    country TEXT NOT NULL 
                );
            
                CREATE TABLE Flight ( 
                    flight_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    airportFrom VARCHAR(128) NOT NULL,
                    airportTo VARCHAR(128) NOT NULL, 
                    aircraftType TEXT NOT NULL,
                    departure_date DATE NOT NULL, 
                    time TEXT NOT NULL, 
                    departure_gate TEXT NOT NULL,
                    arrival_gate TEXT NOT NULL, 
                    duration_in_hrs REAL NOT NULL
                );
            
                CREATE TABLE Ticket (
                    ticket_num INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    customer_id INTEGER NOT NULL, 
                    flight_id INTEGER NOT NULL,
                    cost REAL NOT NULL, 
                    purchase_date DATE NOT NULL, 
                    FOREIGN KEY (customer_id) REFERENCES Customer (customer_id), 
                    FOREIGN KEY (flight_id) REFERENCES Flight (flight_id)
                ); 
            
                CREATE TABLE Employee (
                    employee_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL, 
                    last_name TEXT NOT NULL, 
                    job_title TEXT NOT NULL,
                    flight_id INTEGER NOT NULL, 
                    username VARCHAR(128) NOT NULL UNIQUE,
                    password BINARY NOT NULL,
                    FOREIGN KEY (flight_id) REFERENCES Flight (flight_id)  
                );
            """
            super().execute_script(create_sql)
            print("The Air Asia Database has been successfully created!") #This statement will print if the database was made without issues
        except Exception as e:
            print("Something went wrong, the specific error is:", e) #This statement here indicates that there was an error creating the database
        finally:
            super().close_db() #This statement right here will make it so we follow best practices and close our database











