class Menu:

    @staticmethod
    def show():

        print("\n" + "=" * 40)
        print(" Threat Intelligence Platform ")
        print("=" * 40)

        print("1. Add IOC")
        print("2. View All IOCs")
        print("3. Search IOC")
        print("4. Update IOC")
        print("5. Delete IOC")
        print("6. Generate Reports")
        print("7. Threat Hunting")
        print("8. Statistics Dashboard")
        print("9. Threat Feed")
        print("10. Exit")

        return input("\nChoice: ")