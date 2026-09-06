from threat_intel.database_manager import DatabaseManager


class ThreatHunter:

    @staticmethod
    def hunt():

        db = DatabaseManager()

        print("\n===== Threat Hunting Results =====\n")

        results = db.get_critical_iocs()

        if not results:

            print("No Critical Threats Found")

        else:

            for row in results:

                print(f"IOC ID: {row[0]}")
                print(f"Type: {row[1]}")
                print(f"Value: {row[2]}")
                print(f"Threat: {row[3]}")
                print(f"Score: {row[4]}")
                print(f"Severity: {row[5]}")
                print("-" * 40)

        db.close()