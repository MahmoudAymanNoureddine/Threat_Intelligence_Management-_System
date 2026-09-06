from threat_intel.database_manager import DatabaseManager


class ReputationManager:

    @staticmethod
    def add():

        db = DatabaseManager()

        print("\n===== Assign Reputation =====\n")

        ioc_id = input(
            "IOC ID: "
        )

        reputation = input(
            "Reputation (MALICIOUS / SUSPICIOUS / MONITOR / WHITELISTED / INTERNAL_ASSET): "
        ).upper()

        db.add_reputation(
            ioc_id,
            reputation
        )

        db.close()

        print(
            "\n[+] Reputation Assigned Successfully"
        )

    @staticmethod
    def update():

        db = DatabaseManager()

        print("\n===== Update Reputation =====\n")

        ioc_id = input(
            "IOC ID: "
        )

        reputation = input(
            "New Reputation: "
        ).upper()

        db.update_reputation(
            ioc_id,
            reputation
        )

        db.close()

        print(
            "\n[+] Reputation Updated Successfully"
        )

    @staticmethod
    def view():

        db = DatabaseManager()

        reputations = db.get_reputations()

        print("\n===== IOC Reputations =====\n")

        if not reputations:

            print(
                "No Reputation Records Found"
            )

        else:

            for row in reputations:

                print(
                    f"IOC ID      : {row[0]}"
                )

                print(
                    f"IOC Value   : {row[1]}"
                )

                print(
                    f"Reputation  : {row[2]}"
                )

                print("-" * 40)

        db.close()