from threat_intel.database_manager import DatabaseManager


class CorrelationEngine:

    @staticmethod
    def correlate():

        db = DatabaseManager()

        iocs = db.get_all_iocs()

        threat_groups = {}

        for row in iocs:

            threat_type = row[3]

            if threat_type not in threat_groups:

                threat_groups[threat_type] = []

            threat_groups[threat_type].append(row)

        print("\n" + "=" * 50)
        print(" IOC Correlation Engine ")
        print("=" * 50)

        if not threat_groups:

            print("\nNo Correlations Found")

        else:

            for threat, records in threat_groups.items():

                print(f"\nThreat Type: {threat}")

                print(
                    f"Related IOCs: {len(records)}"
                )

                print("-" * 40)

                for record in records:

                    print(
                        f"{record[1]} : "
                        f"{record[2]}"
                    )

                print("-" * 40)

        db.close()