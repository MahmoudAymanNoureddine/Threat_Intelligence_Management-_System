from threat_intel.database_manager import DatabaseManager


class StatisticsEngine:

    @staticmethod
    def show():

        db = DatabaseManager()

        iocs = db.get_all_iocs()

        total = len(iocs)

        critical = 0
        high = 0
        medium = 0
        low = 0

        for row in iocs:

            severity = row[5]

            if severity == "CRITICAL":
                critical += 1

            elif severity == "HIGH":
                high += 1

            elif severity == "MEDIUM":
                medium += 1

            elif severity == "LOW":
                low += 1

        print("\n" + "=" * 40)
        print(" Threat Intelligence Statistics ")
        print("=" * 40)

        print(f"\nTotal IOCs : {total}")

        print(f"Critical   : {critical}")
        print(f"High       : {high}")
        print(f"Medium     : {medium}")
        print(f"Low        : {low}")

        print("\n" + "=" * 40)

        db.close()