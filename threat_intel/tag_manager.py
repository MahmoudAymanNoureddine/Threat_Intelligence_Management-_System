from threat_intel.database_manager import DatabaseManager


class TagManager:

    @staticmethod
    def add_tag():

        db = DatabaseManager()

        print("\n===== Add IOC Tag =====\n")

        ioc_id = input(
            "IOC ID: "
        )

        tag = input(
            "Tag: "
        )

        db.add_tag(
            ioc_id,
            tag
        )

        db.close()

        print(
            "\n[+] Tag Added Successfully"
        )

    @staticmethod
    def search_by_tag():

        db = DatabaseManager()

        print(
            "\n===== Search By Tag =====\n"
        )

        tag = input(
            "Tag: "
        )

        results = db.search_tag(
            tag
        )

        if not results:

            print(
                "\n[-] No Results Found"
            )

        else:

            for row in results:

                print(
                    f"\nIOC ID      : {row[0]}"
                )

                print(
                    f"Type        : {row[1]}"
                )

                print(
                    f"Value       : {row[2]}"
                )

                print(
                    f"Threat Type : {row[3]}"
                )

                print(
                    f"Severity    : {row[5]}"
                )

                print("-" * 40)

        db.close()