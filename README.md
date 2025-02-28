
# BeamNG.compress
BeamNG.compress is a Python script designed to compress assets for BeamNG.drive, which are stored without any compression by default.

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
- If you haven't created venv in the previous step, you can install script dependencies globally by running
```bash
pip install -r requirements.txt
```
- Or you can use pip installed inside your venv
```bash
./path/to/venv/bin/pip install -r requirements.txt
```
4. Run the tool 
- Once again, if you are using your system-wide installed Python, run
```bash
python compress.py
```
- In case you are using venv, you'll need to run:
```bash
./path/to/venv/python compress.py
```

## Usage
You need to simply run the script and then enter the path to a directory where your BeamNG.drive was installed.

## License
This project is licensed under the GNU GPLv3 License - see the LICENSE file for details.