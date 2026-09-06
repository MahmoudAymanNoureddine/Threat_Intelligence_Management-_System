from threat_intel.database_manager import DatabaseManager
from threat_intel.report_generator import ReportGenerator


class ReportMenu:

    @staticmethod
    def generate():

        db = DatabaseManager()

        data = db.get_all_iocs()

        ReportGenerator.generate_json(
            data
        )

        ReportGenerator.generate_html(
            data
        )

        db.close()

        print(
            "\n[+] Reports Generated Successfully"
        )

        print(
            "[+] reports/threat_report.json"
        )

        print(
            "[+] reports/threat_report.html"
        )