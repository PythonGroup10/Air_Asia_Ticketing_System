# add customer menu and employee menu here
from datetime import datetime
import random

class TicketMenu:
    def __init__(self):
        self.ticket = Ticket()
        self.flight = Flight()
        self.customer = Customer()

    def search_flights(self):
        # Retrieve all available flights in the database
        available_flights = self.flight.getAllFlights()

        #This will print all the available flights for the customer to view
        print("List of available flights to choose from:")
        for flight in available_flights:
            print(f"Flight ID: {flight[0]}, Takeoff Airport: {flight[1]} Destination: {flight[2]}, Date: {flight[4]} Time: {flight[5]}")

    def purchase_ticket(self):
        cust_user = input("Please enter your username: ")

        customer_info = self.customer.retrieve_customer_information(cust_user)
        if customer_info is None:
            print("Customer not found. Please check your username.")
            return
        customer_id = customer_info[0]

        self.search_flights()
        try:
            flight_chosen = input(int("Please enter the flight ID you wish to fly on: "))
            username = input("Please enter your username: ")
            purchase_date = datetime.now().strftime('%Y-%m-%d')  # Format: YYYY-MM-DD
            cost = random.uniform(100.0, 1500.0)

            customer_info = self.customer.retrieve_customer_information(username)
            if customer_info:
                customer_id = customer_info[0]  # Assuming the first element is customer_id
                self.ticket.addTicket(customer_id, flight_chosen, cost, purchase_date)
                print("Ticket for flight purchased successfully! Please have a safe trip!")
            else:
                print("Customer account not found. Please sign up for an account before proceeding")
        except Exception as e:
            print("There was an error purchasing your flight:", e)

    def customer_menu(self):
        ticket_interface = TicketMenu()

        while True:
            print("*** Welcome to the customer menu ***")
            print("1. Search for flight")
            print("2. Purchase a flight ticket")
            print("3. Exit")

            customer_choice = input(int("Please input the number for the option you would like: "))

            if customer_choice == 1:
                print("***SEARCH FOR FLIGHTS***")
                ticket_interface.search_flights()
            elif customer_choice == 2:
                print("***PURCHASE FLIGHT TICKETS***")
                ticket_interface.purchase_ticket()
            elif customer_choice == 3:
                print("Thank you for using Air Asia! Have a good day")
                break
            else:
                print("Unable to retrieve your account information, please try again or sign up")
