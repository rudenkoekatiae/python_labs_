class Park:
    def __init__(self, name="", address="", length_of_bicycle_lanes=0, ticket_price=0.0, visitors=0):
        self.name = name  
        self.__address = address  
        self.__length_of_bicycle_lanes = length_of_bicycle_lanes  
        self.__ticket_price = ticket_price 
        self.visitors = visitors 

    def __str__(self):
        return (f"Park info:\n"
                f" (Address: {self.address})\n"
                f" (Length of bicycle lanes: {self.length_of_bicycle_lanes})\n"
                f" (Ticket price: {self.ticket_price})\n")

    def __repr__(self):
        return (f"address='{self.address}', "
                f"length_of_bicycle_lanes={self.length_of_bicycle_lanes}, "
                f"ticket_price={self.ticket_price}, ")
    
    @property
    def address(self):
        return self.__address
    
    @property
    def length_of_bicycle_lanes(self):
        return self.__length_of_bicycle_lanes
    
    @property
    def ticket_price(self):
        return self.__ticket_price

    @address.setter
    def address(self, address):
        self.__address = address
    
    @length_of_bicycle_lanes.setter
    def length_of_bicycle_lanes(self, length_of_bicycle_lanes):
        self.__length_of_bicycle_lanes = length_of_bicycle_lanes
    
    @ticket_price.setter
    def ticket_price(self, ticket_price):
        self.__ticket_price = ticket_price

    def __del__(self):
        print(f"Park {self.name} is being deleted.")

def main():
    park_1 = Park("Stryi Park", "Lviv, Ulasa Samchuka 14", 3600, 3.5, 500000)
    park_2 = Park("Hyde Park", "London", 6400, 0.0, 13000000)
    park_3 = Park("Central Park", "New York", 4900, 150.15, 42000000)

    parks = [park_1, park_2, park_3]

    max_name_length = max(len(park.name) for park in parks) + 9
    max_bicycle_lane_length = max(len(str(park.length_of_bicycle_lanes)) for park in parks) + 27
    max_address_length = max(len(park.address) for park in parks) + 8
    max_ticket_price_length = max(len(str(park.ticket_price)) for park in parks) + 17
    max_visitors_length = max(len(str(park.visitors)) for park in parks) + 17

    
    print(f"{'Park Name':<{max_name_length}} "
          f"{'Address':<{max_address_length}} "
          f"{'Length of Bicycle Lanes (m)':<{max_bicycle_lane_length}} "
          f"{'Ticket Price ($)':<{max_ticket_price_length}} "
          f"{'Visitors per year':<{max_visitors_length}}")
    
    total_width = (max_name_length + max_bicycle_lane_length + max_address_length +
                 max_ticket_price_length + max_visitors_length)

    print("=" * total_width)

    for park in parks:
        print(f"{park.name:<{max_name_length}} " 
              f"{park.address:<{max_address_length}} " 
              f"{park.length_of_bicycle_lanes:<{max_bicycle_lane_length}} "
              f"{park.ticket_price:<{max_ticket_price_length}} "
              f"{park.visitors:<{max_visitors_length}}") 

if __name__ == '__main__':
    main()