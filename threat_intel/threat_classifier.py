class ThreatClassifier:

    THREAT_SCORES = {

        "ransomware": 100,

        "malicious ip": 90,

        "botnet": 85,

        "c2 server": 95,

        "phishing": 80,

        "trojan": 75,

        "spyware": 70,

        "suspicious": 50
    }

    @staticmethod
    def classify(threat_type):

        score = ThreatClassifier.THREAT_SCORES.get(
            threat_type.lower(),
            25
        )

        if score >= 90:

            severity = "CRITICAL"

        elif score >= 70:

            severity = "HIGH"

        elif score >= 50:

            severity = "MEDIUM"

        else:

            severity = "LOW"

        return score, severity