class ReputationEngine:

    @staticmethod
    def get_reputation(score):

        if score >= 90:

            return "MALICIOUS"

        elif score >= 70:

            return "SUSPICIOUS"

        elif score >= 50:

            return "MONITOR"

        else:

            return "BENIGN"