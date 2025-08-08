# -- Python Script for LDR Reading from Arduino --
# This script connects to an Arduino, reads the LDR sensor values
# sent over the serial port, and prints them to the console.
# It requires the 'pyserial' library: pip install pyserial

import serial
import time
import sys

# Define the serial port and baud rate.
# IMPORTANT: You must change 'COM3' to the correct port for your Arduino.
# On Linux, this is typically '/dev/ttyACM0' or '/dev/ttyUSB0'.
# On macOS, it might be '/dev/cu.usbmodem...'.
# The baud rate must match the Arduino sketch.
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

def main():
    """
    Establishes a serial connection and continuously reads LDR data.
    """
    try:
        # Open the serial port.
        print(f"Attempting to connect to {SERIAL_PORT} at {BAUD_RATE} baud...")
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Give the Arduino time to reset.
        print("Connection successful! Reading LDR values...")

        while True:
            # Read a line from the serial port.
            # .readline() waits until a newline character is received.
            if ser.in_waiting > 0:
                line = ser.readline()
                
                try:
                    # Decode the received bytes into a string and strip whitespace.
                    ldr_value = line.decode('utf-8').strip()
                    
                    # Print the LDR value.
                    print(f"LDR Value: {ldr_value}")
                
                except UnicodeDecodeError:
                    print("Error decoding data. Skipping...")
                
            time.sleep(0.1) # Small delay to prevent busy-waiting.

    except serial.SerialException as e:
        print(f"Error: Could not open serial port '{SERIAL_PORT}'.")
        print("Please check the port name and ensure the Arduino is connected and the port is not in use.")
        print(f"Details: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    main()
