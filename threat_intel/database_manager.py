import sqlite3
from datetime import datetime


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "data/threat_intelligence.db"
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS iocs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            ioc_type TEXT,

            ioc_value TEXT,

            threat_type TEXT,

            score INTEGER,

            severity TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS campaigns (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            campaign_name TEXT,

            threat_type TEXT,

            severity TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS timeline (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            action TEXT,

            target TEXT,

            timestamp TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tags (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            ioc_id INTEGER,

            tag TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reputations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            ioc_id INTEGER,

            reputation TEXT
        )
        """)

        self.connection.commit()

    def add_timeline_event(self, action, target):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.cursor.execute("""
        INSERT INTO timeline
        (
            action,
            target,
            timestamp
        )
        VALUES (?, ?, ?)
        """,
        (
            action,
            target,
            timestamp
        ))

        self.connection.commit()

    def get_all_events(self):

        self.cursor.execute("""
        SELECT *
        FROM timeline
        ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def add_ioc(
        self,
        ioc_type,
        ioc_value,
        threat_type,
        score,
        severity
    ):

        self.cursor.execute("""
        INSERT INTO iocs
        (
            ioc_type,
            ioc_value,
            threat_type,
            score,
            severity
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            ioc_type,
            ioc_value,
            threat_type,
            score,
            severity
        ))

        self.connection.commit()

        self.add_timeline_event(
            "IOC Added",
            ioc_value
        )

    def get_all_iocs(self):

        self.cursor.execute(
            "SELECT * FROM iocs"
        )

        return self.cursor.fetchall()

    def search_ioc(self, value):

        self.cursor.execute("""
        SELECT *
        FROM iocs
        WHERE ioc_value = ?
        """,
        (value,)
        )

        return self.cursor.fetchall()

    def update_ioc(
        self,
        ioc_id,
        threat_type,
        severity
    ):

        self.cursor.execute("""
        UPDATE iocs
        SET
            threat_type = ?,
            severity = ?
        WHERE id = ?
        """,
        (
            threat_type,
            severity,
            ioc_id
        ))

        self.connection.commit()

        self.add_timeline_event(
            "IOC Updated",
            str(ioc_id)
        )

    def delete_ioc(self, ioc_id):

        self.cursor.execute("""
        DELETE FROM iocs
        WHERE id = ?
        """,
        (ioc_id,)
        )

        self.connection.commit()

        self.add_timeline_event(
            "IOC Deleted",
            str(ioc_id)
        )

    def get_critical_iocs(self):

        self.cursor.execute("""
        SELECT *
        FROM iocs
        WHERE severity = 'CRITICAL'
        """)

        return self.cursor.fetchall()

    def add_campaign(
        self,campaign_name,
        threat_type,
        severity
    ):

        self.cursor.execute("""
        INSERT INTO campaigns
        (
            campaign_name,
            threat_type,
            severity
        )
        VALUES (?, ?, ?)
        """,
        (
            campaign_name,
            threat_type,
            severity
        ))

        self.connection.commit()

        self.add_timeline_event(
            "Campaign Created",
            campaign_name
        )

    def get_all_campaigns(self):

        self.cursor.execute(
            "SELECT * FROM campaigns"
        )

        return self.cursor.fetchall()

    def add_tag(
        self,
        ioc_id,
        tag
    ):

        self.cursor.execute("""
        INSERT INTO tags
        (
            ioc_id,
            tag
        )
        VALUES (?, ?)
        """,
        (
            ioc_id,
            tag
        ))

        self.connection.commit()

        self.add_timeline_event(
            "Tag Added",
            tag
        )

    def search_tag(
        self,
        tag
    ):

        self.cursor.execute("""
        SELECT iocs.*
        FROM iocs
        JOIN tags
        ON iocs.id = tags.ioc_id
        WHERE tags.tag = ?
        """,
        (tag,)
        )

        return self.cursor.fetchall()

    def add_reputation(
        self,
        ioc_id,
        reputation
    ):

        self.cursor.execute("""
        INSERT INTO reputations
        (
            ioc_id,
            reputation
        )
        VALUES (?, ?)
        """,
        (
            ioc_id,
            reputation
        ))

        self.connection.commit()

        self.add_timeline_event(
            "Reputation Assigned",
            reputation
        )

    def update_reputation(
        self,
        ioc_id,
        reputation
    ):

        self.cursor.execute("""
        UPDATE reputations
        SET reputation = ?
        WHERE ioc_id = ?
        """,
        (
            reputation,
            ioc_id
        ))

        self.connection.commit()

        self.add_timeline_event(
            "Reputation Updated",
            reputation
        )

    def get_reputations(self):

        self.cursor.execute("""
        SELECT
            reputations.ioc_id,
            iocs.ioc_value,
            reputations.reputation
        FROM reputations
        JOIN iocs
        ON reputations.ioc_id = iocs.id
        """)

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()