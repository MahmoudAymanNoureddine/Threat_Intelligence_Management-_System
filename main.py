from threat_intel.menu import Menu
from threat_intel.ioc_manager import IOCManager
from threat_intel.ioc_viewer import IOCViewer
from threat_intel.ioc_search import IOCSearch
from threat_intel.ioc_update import IOCUpdate
from threat_intel.ioc_delete import IOCDelete
from threat_intel.report_generator import ReportGenerator
from threat_intel.threat_hunter import ThreatHunter
from threat_intel.statistics_engine import StatisticsEngine
from threat_intel.feed_engine import FeedEngine
from threat_intel.executive_dashboard import ExecutiveDashboard
from threat_intel.correlation_engine import CorrelationEngine


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

            ReportGenerator.generate()

        elif choice == "7":

            ThreatHunter.hunt()

        elif choice == "8":

            StatisticsEngine.show()

        elif choice == "9":

            FeedEngine.show_feed()

        elif choice == "10":

            ExecutiveDashboard.show()

        elif choice == "11":

            CorrelationEngine.correlate()

        elif choice == "12":

            print("\nGoodbye!")
            break

        else:

            print("\nInvalid Choice")


if __name__ == "__main__":
    main()