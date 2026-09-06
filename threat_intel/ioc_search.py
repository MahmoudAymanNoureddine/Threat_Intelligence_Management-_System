from threat_intel.database_manager import DatabaseManager


class IOCSearch:

    @staticmethod
    def search():

        db = DatabaseManager()

        value = input(
            "\nIOC Value: "
        )

        results = db.search_ioc(
            value
        )

        if not results:

            print(
                "\n[-] IOC Not Found"
            )

        else:

            print(
                "\n===== Search Results =====\n"
            )

            for row in results:

                print(f"ID: {row[0]}")
                print(f"Type: {row[1]}")
                print(f"Value: {row[2]}")
                print(f"Threat: {row[3]}")
                print(f"Severity: {row[4]}")
                print("-" * 40)

        db.close()