from threat_intel.database_manager import DatabaseManager


class IOCManager:

    @staticmethod
    def add_ioc():

        db = DatabaseManager()

        print("\n=== Add New IOC ===\n")

        ioc_type = input(
            "IOC Type (IP / Domain / Hash): "
        )

        ioc_value = input(
            "IOC Value: "
        )

        threat_type = input(
            "Threat Type: "
        )

        severity = input(
            "Severity (Low / Medium / High): "
        )

        db.add_ioc(
            ioc_type,
            ioc_value,
            threat_type,
            severity
        )

        db.close()

        print(
            "\n[+] IOC Added Successfully"
        )