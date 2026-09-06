from threat_intel.database_manager import DatabaseManager


class ExecutiveDashboard:

    @staticmethod
    def show():

        db = DatabaseManager()

        iocs = db.get_all_iocs()

        total = len(iocs)

        critical = 0
        high = 0
        medium = 0
        low = 0

        total_score = 0

        for row in iocs:

            score = row[4]

            severity = row[5]

            total_score += score

            if severity == "CRITICAL":

                critical += 1

            elif severity == "HIGH":

                high += 1

            elif severity == "MEDIUM":

                medium += 1

            elif severity == "LOW":

                low += 1

        average_score = 0

        if total > 0:

            average_score = total_score / total

        severity_map = {
            "CRITICAL": critical,
            "HIGH": high,
            "MEDIUM": medium,
            "LOW": low
        }

        top_severity = max(
            severity_map,
            key=severity_map.get
        )

        print("\n" + "=" * 40)
        print(" Executive Dashboard ")
        print("=" * 40)

        print(f"\nTotal IOCs         : {total}")

        print(f"\nCritical Threats   : {critical}")
        print(f"High Threats       : {high}")
        print(f"Medium Threats     : {medium}")
        print(f"Low Threats        : {low}")

        print(
            f"\nThreat Score Avg   : "
            f"{average_score:.2f}"
        )

        print(
            f"Top Severity       : "
            f"{top_severity}"
        )

        print("\n" + "=" * 40)

        db.close()