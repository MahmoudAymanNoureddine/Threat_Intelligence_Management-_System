from threat_intel.database_manager import DatabaseManager


class CampaignManager:

    @staticmethod
    def create_campaign():

        db = DatabaseManager()

        print("\n===== Create Campaign =====\n")

        campaign_name = input(
            "Campaign Name: "
        )

        threat_type = input(
            "Threat Type: "
        )

        severity = input(
            "Severity: "
        )

        db.add_campaign(
            campaign_name,
            threat_type,
            severity
        )

        db.close()

        print(
            "\n[+] Campaign Created Successfully"
        )

    @staticmethod
    def view_campaigns():

        db = DatabaseManager()

        campaigns = db.get_all_campaigns()

        print(
            "\n===== Threat Campaigns =====\n"
        )

        for campaign in campaigns:

            print(
                f"ID: {campaign[0]}"
            )

            print(
                f"Campaign: {campaign[1]}"
            )

            print(
                f"Threat Type: {campaign[2]}"
            )

            print(
                f"Severity: {campaign[3]}"
            )

            print("-" * 40)

        db.close()