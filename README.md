# Web-Inspect
A web application pentesting tool

# URL Technology Analyzer
This Python script leverages the power of Wappalyzer and a subdomain finder to identify technologies used on websites across various subdomains. It checks each subdomain for HTTPS support and employs Wappalyzer to detect technologies, meticulously logging the results to a CSV file for further analysis.

# Features
1. Efficient subdomain discovery using the subfinder command-line tool.
2. Verification of HTTPS support for each subdomain (defaults to HTTP if HTTPS fails).
3. Meticulous analysis of web technologies employed on each subdomain using Wappalyzer.
4. Generation of a comprehensive CSV file with detailed information: domain, technology, version, and categories.

# Prerequisites
Python 3.6 or later
requests library (pip install requests)
Wappalyzer Python library (pip install python-Wappalyzer)
subfinder command-line tool (installation instructions below)
