from threat_intel.database_manager import DatabaseManager
from threat_intel.threat_scoring import ThreatScoring


class IOCManager:

    @staticmethod
    def add():

        db = DatabaseManager()

        print("\n===== Add New IOC =====\n")

        ioc_type = input(
            "IOC Type (IP / Domain / Hash): "
        )

        ioc_value = input(
            "IOC Value: "
        )

        threat_type = input(
            "Threat Type: "
        )

        score, severity = (
            ThreatScoring.calculate(
                threat_type
            )
        )

        db.add_ioc(
            ioc_type,
            ioc_value,
            threat_type,
            score,
            severity
        )

        db.close()

        print("\n[+] IOC Added Successfully")

        print(
            f"Threat Score: {score}"
        )

        print(
            f"Severity: {severity}"
        )