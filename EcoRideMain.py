from Vehicle import Vehicle
class EcoRideMain:
    @staticmethod
    def start():
        print("Welcome to Eco-Ride Urban Mobility System")

        vehicle_id = input("Enter Vehicle ID: ")
        model = input("Enter Model: ")
        battery = int(input("Enter Battery Percentage: "))

        vehicle = Vehicle(vehicle_id, model, battery)
        print("Your vehicle_id-->",vehicle_id,
        "\nYour model of car-->",model,
        "\nYour battery percentage-->",battery,
        "\nVehicle created successfully")

if __name__ == "__main__":
    EcoRideMain.start()
