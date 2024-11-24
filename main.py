class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self, capacity, fare_per_passenger):
        super().__init__(capacity)
        self.fare_per_passenger = fare_per_passenger

    def calculate_total_fare(self, num_passengers):
        if num_passengers > self.capacity:
            return 0
        return num_passengers * self.fare_per_passenger

capacity = int(input("Enter capacity of bus: "))
fare_per_passenger = float(input("Enter fare per passenger: "))
bus = Bus(capacity, fare_per_passenger)

num_passengers = int(input("Enter number of passengers: "))
total_fare = bus.calculate_total_fare(num_passengers)

if total_fare > 0:
    print(f"Total fare for {num_passengers} passengers: ${total_fare:.2f}")
else:
    print("Number of passengers exceeds capacity")