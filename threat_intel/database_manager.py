import sqlite3


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "data/threat_intelligence.db"
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS iocs (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                ioc_type TEXT,

                ioc_value TEXT,

                threat_type TEXT,

                severity TEXT
            )
            """
        )

        self.connection.commit()

    def add_ioc(
        self,
        ioc_type,
        ioc_value,
        threat_type,
        severity
    ):

        self.cursor.execute(
            """
            INSERT INTO iocs
            (
                ioc_type,
                ioc_value,
                threat_type,
                severity
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                ioc_type,
                ioc_value,
                threat_type,
                severity
            )
        )

        self.connection.commit()

    def get_all_iocs(self):

        self.cursor.execute(
            "SELECT * FROM iocs"
        )

        return self.cursor.fetchall()

    def search_ioc(self, value):

        self.cursor.execute(
            """
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

        self.cursor.execute(
            """
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
            )
        )

        self.connection.commit()

    def delete_ioc(self, ioc_id):

        self.cursor.execute(
            """
            DELETE FROM iocs
            WHERE id = ?
            """,
            (ioc_id,)
        )

        self.connection.commit()

    def close(self):

        self.connection.close()