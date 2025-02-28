
# BeamNG.compress
**BeamNG.compress** is a Python script designed to compress assets for BeamNG.drive, which are stored without any compression by default.

## Installation
If you want to, you can download the script itself and run it from anywhere. Although, for debugging purposes, here is the detailed installation guide:
1. Clone the repository
```bash
git clone https://github.com/x7k3e21/BeamNG.compress
```
2. Create a virtual environment (optional)
```bash
python -m venv ./path/to/venv
```
3. Install dependencies (optional)
```bash
# Without using venv
pip install -r requirements.txt

# Running inside venv
./path/to/venv/bin/pip install -r requirements.txt
```
4. Run the tool 
```bash
# Using system-wide installed Python
python compress.py

# Using Python inside a virtual environment
./path/to/venv/python compress.py
```

## Usage
You need to simply run the script and then enter the path to a directory where your BeamNG.drive was installed. Execution may take a significant amount of time, especially on low-end machines.

## License
This project is licensed under the GNU General Public License v3.0.