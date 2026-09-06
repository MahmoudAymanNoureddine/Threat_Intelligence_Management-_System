from threat_intel.database_manager import DatabaseManager


class TimelineManager:

    @staticmethod
    def show():

        db = DatabaseManager()

        events = db.get_all_events()

        print("\n" + "=" * 50)
        print(" IOC Activity Timeline ")
        print("=" * 50)

        if not events:

            print("\nNo Timeline Events Found")

        else:

            for event in events:

                print(f"\nID         : {event[0]}")
                print(f"Action     : {event[1]}")
                print(f"Target     : {event[2]}")
                print(f"Timestamp  : {event[3]}")

                print("-" * 40)

        db.close()