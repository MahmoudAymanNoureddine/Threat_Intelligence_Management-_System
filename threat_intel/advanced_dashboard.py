from collections import Counter

from threat_intel.database_manager import DatabaseManager


class AdvancedDashboard:

    @staticmethod
    def show():

        db = DatabaseManager()

        iocs = db.get_all_iocs()

        campaigns = db.get_all_campaigns()

        total_iocs = len(iocs)

        total_campaigns = len(campaigns)

        critical = 0
        high = 0
        medium = 0
        low = 0

        total_score = 0

        threat_types = []

        for row in iocs:

            score = row[4]

            severity = row[5]

            threat_types.append(
                row[3]
            )

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

        if total_iocs > 0:

            average_score = (
                total_score /
                total_iocs
            )

        top_threat = "N/A"

        if threat_types:

            top_threat = Counter(
                threat_types
            ).most_common(1)[0][0]

        print("\n" + "=" * 50)
        print(" Advanced Threat Intelligence Dashboard ")
        print("=" * 50)

        print(
            f"\nTotal IOCs       : {total_iocs}"
        )

        print(
            f"Total Campaigns  : {total_campaigns}"
        )

        print(
            f"\nCritical Threats : {critical}"
        )

        print(
            f"High Threats     : {high}"
        )

        print(
            f"Medium Threats   : {medium}"
        )

        print(
            f"Low Threats      : {low}"
        )

        print(
            f"\nAverage Score    : "
            f"{average_score:.2f}"
        )

        print(
            f"Top Threat Type  : "
            f"{top_threat}"
        )

        print("\n" + "=" * 50)

        db.close()