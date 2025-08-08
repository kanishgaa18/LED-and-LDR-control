# -- Python Script for Arduino LED Control --
# This script communicates with an Arduino to control an LED.
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
    Main function to handle user input and send commands to the Arduino.
    """
    try:
        # Open the serial port.
        print(f"Attempting to connect to {SERIAL_PORT} at {BAUD_RATE} baud...")
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Give the Arduino time to reset.
        print("Connection successful! Use commands below.")

        print("\nCommands:")
        print(" '1' - Turn LED On")
        print(" '0' - Turn LED Off")
        print(" 'q' - Quit")
        
        while True:
            command = input("\nEnter command: ")
            
            if command == 'q':
                print("Exiting program.")
                break
            
            if command in ('1', '0'):
                # Send the command to the Arduino.
                # Encode the string command into bytes before sending.
                ser.write(command.encode('utf-8'))
                print(f"Sent command '{command}' to Arduino.")
            else:
                print("Invalid command. Please enter '1', '0', or 'q'.")

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
