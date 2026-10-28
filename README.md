# TCP Banner Grabber 🔍🐍

A simple, effective Python 3 utility built using socket programming to connect to specific IP addresses and ports, retrieving running service banners for vulnerability assessment and enumeration.

## Features
- Connects to target hosts over TCP.
- Sends service probes to elicit application response banners.
- Identifies version strings for pre-screening software versions.

## Usage
```bash
python3 banner_grabber.py <target_ip> <port>
