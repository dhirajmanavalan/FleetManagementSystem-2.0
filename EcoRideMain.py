from Vehicle import Vehicle
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter

class EcoRideMain:
    @staticmethod
    def start():
        print("Welcome to Eco-Ride Urban Mobility System")

        print("Choose Vehicle Type:")
        print("1. Electric Car")
        print("2. Electric Scooter")

        try:
            choice = int(input("Enter choice (1 or 2): "))

            vehicle_id = input("Enter Vehicle ID: ")
            model = input("Enter Model: ")
            battery = int(input("Enter Battery Percentage: "))
            maintenance_status = input("Enter Maintenance Status: ")
            rental_price = int(input("Enter Rental Price: "))

            vehicles = []

            if choice == 1:
                seating_capacity = int(input("Enter Seating Capacity: "))
                car = ElectricCar(
                    vehicle_id,
                    model,
                    battery,
                    maintenance_status,
                    rental_price,
                    seating_capacity
                )
                vehicles.append(car)

            elif choice == 2:
                max_speed = int(input("Enter Maximum Speed: "))
                scooter = ElectricScooter(
                    vehicle_id,
                    model,
                    battery,
                    maintenance_status,
                    rental_price,
                    max_speed
                )
                vehicles.append(scooter)

            else:
                print("Invalid choice")
                return

            print("\n--- Vehicle Summary & Trip Cost ---")
            for vehicle in vehicles:
                print("\nModel:", vehicle.model)
                print("Battery:", vehicle.battery_percentage)
                print("Maintenance:", vehicle.maintenance_status)
                print("Rental Price:", vehicle.rental_price)

                if isinstance(vehicle, ElectricCar):
                    print("Seating Capacity:", vehicle.seating_capacity)
                    distance = float(input("Enter Distance: "))
                    cost = vehicle.calculate_trip_cost(distance)
                else:
                    print("Max Speed:", vehicle.max_speed_limit)
                    minutes = float(input("Enter Minutes: "))
                    cost = vehicle.calculate_trip_cost(minutes)

                print("Trip Cost:", cost)

        except ValueError as e:
            print("Input Error:", e)

if __name__ == "__main__":
    EcoRideMain.start()
