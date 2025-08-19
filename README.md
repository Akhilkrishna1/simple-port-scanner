# Simple Port Scanner

A minimal Python tool for TCP port scanning. Created for cybersecurity demonstration purposes.

## Usage

Run from the command line:

```sh
python main.py <host> [-p PORTS]
```

- `<host>`: Target IP address or domain
- `-p`, `--ports`: Port range (default: 1-1024), example: -p 20-80

## Example

```sh
python main.py scanme.nmap.org -p 20-25
```

## Legal Disclaimer

> This tool is provided for educational and authorized security testing only. Unauthorized scanning is illegal. The author assumes no liability for misuse or damage caused.

## Requirements
- Python 3.x
- No third-party dependencies

---

Feel free to fork/use and submit improvements.
