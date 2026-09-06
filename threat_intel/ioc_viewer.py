from threat_intel.database_manager import DatabaseManager


class IOCViewer:

    @staticmethod
    def show():

        db = DatabaseManager()

        results = db.get_all_iocs()

        print("\n===== Stored IOCs =====\n")

        for row in results:

            print(f"ID: {row[0]}")
            print(f"Type: {row[1]}")
            print(f"Value: {row[2]}")
            print(f"Threat: {row[3]}")
            print(f"Severity: {row[4]}")
            print("-" * 40)

        db.close()