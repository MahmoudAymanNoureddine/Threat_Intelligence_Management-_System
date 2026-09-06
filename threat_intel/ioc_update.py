from threat_intel.database_manager import DatabaseManager


class IOCUpdate:

    @staticmethod
    def update():

        db = DatabaseManager()

        print("\n===== Update IOC =====\n")

        ioc_id = input("IOC ID: ")

        threat_type = input(
            "New Threat Type: "
        )

        severity = input(
            "New Severity: "
        )

        db.update_ioc(
            ioc_id,
            threat_type,
            severity
        )

        db.close()

        print(
            "\n[+] IOC Updated Successfully"
        )