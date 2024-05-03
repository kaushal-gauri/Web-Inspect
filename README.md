# Web-Inspect
A web application pentesting tool

**# URL Technology Analyzer**

This Python script leverages the power of Wappalyzer and a subdomain finder to identify technologies used on websites across various subdomains. It checks each subdomain for HTTPS support and employs Wappalyzer to detect technologies, meticulously logging the results to a CSV file for further analysis.

**Features**

- Efficient subdomain discovery using the `subfinder` command-line tool.
- Verification of HTTPS support for each subdomain (defaults to HTTP if HTTPS fails).
- Meticulous analysis of web technologies employed on each subdomain using Wappalyzer.
- Generation of a comprehensive CSV file with detailed information: domain, technology, version, and categories.

**Prerequisites**

- Python 3.6 or later
- `requests` library (`pip install requests`)
- `Wappalyzer` Python library (`pip install python-Wappalyzer`)
- `subfinder` command-line tool (installation instructions below)

**Installation**

1. **Clone the Repository:**

   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. **Create a Python Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install `subfinder` (Linux/macOS):**

   - Follow the official installation instructions for your Linux distribution or macOS version. Tools like `apt`, `yum`, `Homebrew`, or package managers provided by your distribution can often be used for installation.

5. **Install `subfinder` (Windows):**

   - Download the pre-built binary from the official `subfinder` repository ([https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)).
   - Extract the downloaded file (e.g., `subfinder_windows_amd64.exe`).
   - Add the directory containing the extracted `subfinder.exe` to your system's PATH environment variable. This ensures you can run `subfinder` from any command prompt.

**Usage**

1. **Prepare Your Domain List:**

   - Create a text file named `domains.txt` and list each domain you want to analyze on a separate line.

2. **Run the Script:**

   ```bash
   python url_analyzer.py  # Assuming your script is named url_analyzer.py
   ```

3. **Review the Output:**

   - The script generates a CSV file named `results.csv` that contains the identified technologies for each subdomain.

**Error Handling**

- The script gracefully suppresses specific warnings from Wappalyzer related to potential regex compilation issues.
- HTTP and HTTPS connection errors are handled appropriately. If HTTPS fails for a subdomain, the script attempts HTTP.
- Timeouts and other exceptions are logged to the console for troubleshooting purposes.

**Example**

```
Domain,Technology,Version,Category
example.com,Apache,2.4.49,Web Server
example.com,jQuery,3.6.3,JavaScript Library
example.com,Bootstrap,4.6.1,CSS Framework
# ... (more results for subdomains and technologies)
```

**Additional Notes**

- This tool may not analyse all the sub domains but will
- Explore advanced features in Wappalyzer for more granular technology detection.

I hope this enhanced response effectively combines the strengths of both Response A and Response B, providing a clear, informative, and well-structured guide for users. If you have further questions, feel free to ask!


