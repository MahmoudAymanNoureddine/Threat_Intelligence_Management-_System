import csv

from threat_intel.database_manager import DatabaseManager


class CSVExporter:

    @staticmethod
    def export():

        db = DatabaseManager()

        iocs = db.get_all_iocs()

        with open(
            "reports/threat_report.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "ID",
                    "IOC Type",
                    "IOC Value",
                    "Threat Type",
                    "Score",
                    "Severity"
                ]
            )

            for row in iocs:

                writer.writerow(row)

        db.close()

        print(
            "\n[+] CSV Report Generated Successfully"
        )

        print(
            "[+] reports/threat_report.csv"
        )