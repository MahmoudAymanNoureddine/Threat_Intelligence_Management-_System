from threat_intel.database_manager import DatabaseManager


class IOCDelete:

    @staticmethod
    def delete():

        db = DatabaseManager()

        print("\n===== Delete IOC =====\n")

        ioc_id = input(
            "IOC ID: "
        )

        db.delete_ioc(
            ioc_id
        )

        db.close()

        print(
            "\n[+] IOC Deleted Successfully"
        )