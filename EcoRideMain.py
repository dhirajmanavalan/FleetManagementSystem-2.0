from Vehicle import Vehicle

class EcoRideMain:
    @staticmethod
    def start():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicle_id = input("Enter Vehicle ID: ")
        model = input("Enter Model: ")
        battery = int(input("Enter Battery Percentage: "))
        maintenance_status = input("Enter Maintenance Status: ")
        rental_price = int(input("Enter Rental Price: "))

        vehicle = Vehicle(vehicle_id, model, battery, maintenance_status, rental_price)

        print("\nVehicle Created Successfully")
        print("Vehicle ID:", vehicle.vehicle_id)
        print("Model:", vehicle.model)
        print("Battery:", vehicle.battery_percentage)
        print("Maintenance:", vehicle.maintenance_status)
        print("Rental Price:", vehicle.rental_price)

if __name__ == "__main__":
    EcoRideMain.start()
