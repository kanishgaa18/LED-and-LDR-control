# LED and LDR Control with Arduino

A simple, interactive project showcasing how to control an LED and read light data via an LDR (Light-Dependent Resistor) using both Arduino and Python.

---

##  Repository Structure

- **`LEDControl.ino`**  
  Arduino sketch to receive serial commands ('1' to turn LED ON, '0' to turn LED OFF) and toggle an LED accordingly. Useful for remote control via USB serial.

- **`LDRcontrol.ino`**  
  Arduino sketch that reads analog values from an LDR sensor and sends them over serial, enabling ambient light monitoring.

- **`LEDControl.py`**  
  Python script for sending `"1"` or `"0"` commands to the Arduino, turning the LED on or off. Utilizes the `pyserial` library.

- **`LDRcontrol.py`**  
  Python script to request and/or continuously read the light sensor data from the Arduino. Also relies on `pyserial`.

---

##  Getting Started

### 1. Prerequisites

- **Arduino board** (Uno, Nano, etc.) connected via USB  
- **[Python 3](https://www.python.org/)** installed  
- Python library: `pyserial`  
  ```bash
  pip install pyserial
