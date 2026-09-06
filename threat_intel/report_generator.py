import json


class ReportGenerator:

    @staticmethod
    def generate_json(data):

        with open(
            "reports/threat_report.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def generate_html(data):

        html = """
        <html>
        <head>

            <title>
                Threat Intelligence Report
            </title>

        </head>

        <body>

            <h1>
                Threat Intelligence Report
            </h1>

            <table border="1">

                <tr>

                    <th>ID</th>
                    <th>IOC Type</th>
                    <th>IOC Value</th>
                    <th>Threat Type</th>
                    <th>Score</th>
                    <th>Severity</th>

                </tr>
        """

        for row in data:

            html += f"""
            <tr>

                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td>{row[3]}</td>
                <td>{row[4]}</td>
                <td>{row[5]}</td>

            </tr>
            """

        html += """
            </table>

        </body>
        </html>
        """

        with open(
            "reports/threat_report.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)