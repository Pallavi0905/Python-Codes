class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seat available in the train is {self.seats}")

    def fareInfo(self):
        print(f"The price of the train ticket is {self.fare}")
    
    def bookTicket(self):
        if (self.seats>0):
            print(f"Your ticket has been booked. Your seat no. is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("This train is full. Kindly go with Tatkal")
      
Intercity = Train("Intersity Express: 14015", 90, 2)
Intercity.fareInfo()
Intercity.getstatus()
Intercity.bookTicket()