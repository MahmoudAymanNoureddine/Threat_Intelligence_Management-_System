# Threat Intelligence Engine

A Python-based Threat Intelligence Engine designed for IOC Management, Threat Hunting, Security Analysis, Campaign Tracking, Reputation Management, and Reporting.

The project provides an analyst-oriented environment for storing, classifying, correlating, tracking, and analyzing threat intelligence data through both a CLI interface and an evolving Flask Web Dashboard.

---

## Features

### IOC Management

- Add IOC
- View All IOCs
- Search IOC
- Update IOC
- Delete IOC

### Threat Analysis

- Threat Classification
- Threat Scoring
- Reputation Analysis
- Whitelisting Support

### Threat Hunting

- Critical IOC Detection
- High-Risk Indicator Discovery
- Threat Investigation Support

### Threat Intelligence

- IOC Correlation Engine
- Threat Campaign Management
- Activity Timeline Tracking
- IOC Tagging System

### Dashboards

- Statistics Dashboard
- Executive Dashboard
- Advanced Dashboard
- Flask Web Dashboard

### Reporting

- JSON Reports
- HTML Reports
- CSV Reports

### Database

- SQLite Backend
- Structured IOC Storage
- Campaign Storage
- Timeline Storage
- Reputation Storage

---

## Technologies Used

- Python 3
- Flask
- SQLite
- HTML
- CSS
- Jinja2

---

## Project Structure
Threat_Intelligence_Platform
│
├── data/
│   └── threat_intelligence.db
│
├── reports/
│   ├── threat_report.json
│   ├── threat_report.html
│   └── threat_report.csv
│
├── screenshots/
│
├── static/
│
├── templates/
│
├── threat_intel/
│
├── app.py
├── main.py
├── requirements.txt
├── LICENSE
└── README.md

---

## Core Components

### IOC Management Engine

Responsible for IOC lifecycle operations including:

- Creation
- Storage
- Search
- Update
- Deletion

### Threat Hunting Engine

Allows analysts to identify:

- Critical Threats
- Malicious Indicators
- High-Risk IOC Records

### Reputation Engine

Supports:

- MALICIOUS
- SUSPICIOUS
- MONITOR
- WHITELISTED
- INTERNAL_ASSET

### Campaign Management Engine

Tracks:

- Threat Campaigns
- Related Threat Types
- Campaign Severity Levels

### Correlation Engine

Correlates multiple indicators sharing:

- Threat Type
- Campaign Context
- Investigation Scope

---

## Running The Project

### CLI Version
python main.py


## Future Development

The current release focuses on the Threat Intelligence Engine.

Planned Platform Enhancements:

- Advanced Flask Dashboard
- IOC Web Forms
- Campaign Management Pages
- Interactive Statistics
- Threat Intelligence Visualization
- User Authentication
- Analyst Workspace

---

## Screenshots

### Dashboard

Add image here.

### IOC Management

Add image here.

### Threat Reports

Add image here.

### Flask Dashboard

Add image here.

---

## License

This project is released under the MIT License.

---

## Author

Mahmoud Ayman Noureddine

Cybersecurity & Network Security 

Threat Intelligence | SOC | Blue Team | Security Operations
