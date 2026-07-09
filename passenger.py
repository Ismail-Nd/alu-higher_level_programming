class Passenger:
    def __init__(self, name, current_location, destination, date):
        self.name = name
        self.current_location = current_location
        self.destination = destination
        self.date = date

    def get_passenger_info(self):
        return(f"Passenger Name : {self.name}, Loaction: {self.current_location}, Where he is heading: {self.destination}, on date: {self.date}")
    
    def get_weight_allowance(self):
        return("Allowed 30kg")

class EconomyPassenger(Passenger):
    ...


class FirstClassPassenger(Passenger):
    def __init__(self, name, current_location, destination, date, weight, lounge_access):
        super().__init__(name, current_location, destination, date)

        self.weight = weight
        self.lounge_access = lounge_access

    def set_weight(self):
        return("Weight on board 20kg")
    
    def access_lounge(self):
        return("Business Class")

class PremiumClassPassenger(Passenger):
    def __init__(self, name, current_location, destination, date, weight, priority_boarding):
        super().__init__(name, current_location, destination, date)
        self.weight = weight
        self.priority_boarding = priority_boarding

    def set_weight(self):
        return("Weight on board 30kg")

    def priority_boarding(self):
        return("High")



