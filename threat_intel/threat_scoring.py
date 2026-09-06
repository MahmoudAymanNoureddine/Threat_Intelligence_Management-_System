class ThreatScoring:

    THREAT_SCORES = {

        "BOTNET": 95,

        "RANSOMWARE": 100,

        "MALWARE": 90,

        "PHISHING": 85,

        "MALICIOUS IP": 80,

        "TOR EXIT NODE": 75,

        "BRUTE FORCE": 70,

        "SNIFFING": 60,

        "SPAM": 40
    }

    @staticmethod
    def calculate(threat_type):

        score = ThreatScoring.THREAT_SCORES.get(
            threat_type.upper(),
            20
        )

        if score >= 90:

            severity = "CRITICAL"

        elif score >= 70:

            severity = "HIGH"

        elif score >= 40:

            severity = "MEDIUM"

        else:

            severity = "LOW"

        return score, severity