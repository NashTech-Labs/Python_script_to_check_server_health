# Server Health Check Script

## Description

This Python script checks the availability of servers by making HTTP requests to URLs and verifying that the responses have a status code of 200. It can be configured to run periodically to ensure that your servers are up and running.

## Usage

To use this script, you will need Python and the `requests` library installed on your system. You can install the `requests` library using `pip`:
```
pip install requests
```

Once you have the `requests` library installed, you can run the script with:
```
python server_check.py
```

The script will iterate through a list of URLs and print whether each server is up or down.

## Customizing the Script

You can customize the list of URLs to check by editing the `urls` list in the script:
```
python urls = ["http://example.com", "http://example2.com"]
```

Replace the example URLs with the actual URLs of the servers you want to monitor.

## Scheduling the Script

To have the script check your servers periodically, there are multiple ways:

1. You can schedule it using `cron` on Unix-like systems or Task Scheduler on Windows. The following `cron` entry will run the script every hour:

Open the terminal and enter `crontab -e`
Add a new line in the in the crontab with following values:
`0 * * * * /usr/bin/python /path/to/server_check.py >> /path/to/logfile.log 2>&1`

Make sure to replace `/path/to/server_check.py` with the actual path to the script and `/path/to/logfile.log` with the path to the log file where you want to store the output.

2. Secondly you can use Jenkins, GitHub Actions or any other CI/CD tool to run this python script on regular intervals.
