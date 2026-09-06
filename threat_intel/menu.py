class Menu:

    @staticmethod
    def show():

        print("\n" + "=" * 40)
        print(" Threat Intelligence Platform ")
        print("=" * 40)

        print("1. Add IOC")
        print("2. View All IOCs")
        print("3. Search IOC")
        print("4. Exit")

        return input("\nChoice: ")