from threat_intel.database_manager import DatabaseManager
from threat_intel.reputation_engine import ReputationEngine


class FeedEngine:

    @staticmethod
    def show_feed():

        db = DatabaseManager()

        results = db.get_all_iocs()

        print("\n" + "=" * 40)
        print(" Threat Intelligence Feed ")
        print("=" * 40)

        for row in results:

            reputation = ReputationEngine.get_reputation(
                row[4]
            )

            print(f"IOC ID      : {row[0]}")
            print(f"Type        : {row[1]}")
            print(f"Value       : {row[2]}")
            print(f"Threat      : {row[3]}")
            print(f"Score       : {row[4]}")
            print(f"Severity    : {row[5]}")
            print(f"Reputation  : {reputation}")

            print("-" * 40)

        db.close()