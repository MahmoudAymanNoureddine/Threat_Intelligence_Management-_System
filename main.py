from threat_intel.menu import Menu
from threat_intel.ioc_manager import IOCManager
from threat_intel.ioc_viewer import IOCViewer
from threat_intel.ioc_search import IOCSearch
from threat_intel.ioc_update import IOCUpdate
from threat_intel.ioc_delete import IOCDelete


def main():

    while True:

        choice = Menu.show()

        if choice == "1":

            IOCManager.add()

        elif choice == "2":

            IOCViewer.show()

        elif choice == "3":

            IOCSearch.search()

        elif choice == "4":

            IOCUpdate.update()

        elif choice == "5":

            IOCDelete.delete()

        elif choice == "6":

            print("\nGoodbye!")
            break

        else:

            print("\nInvalid Choice")


if __name__ == "__main__":
    main()