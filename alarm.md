# Alarm Clock in Python

## Overview
This project implements a simple alarm clock using Python. The alarm clock allows users to set a specific time for the alarm to ring, playing a sound when the time is reached. The program utilizes the `datetime` module to handle time and the `pygame` module to play the alarm sound.

## Features
- Set an alarm for a specific time.
- Play a sound when the alarm time is reached.
- Compare the current time with the set alarm time.
- Use `time.sleep()` to avoid constant checking of the time, making the program efficient.

## Requirements
To run this project, you need:
- Python 3.x
- `pygame` module (for playing sound)

### Installation
1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the `pygame` module using pip:
   ```bash
   pip install playgame
   ```

### How It Works

The user inputs the desired alarm time in the format HH:MM AM/PM.
The program continuously checks the current time against the set alarm time.    When the current time matches the alarm time, it plays the specified sound and notifies the user.

### Usage
Clone or download this repository to your local machine.
Run the script using Python:
```bash
python alarm_clock.py
```
Enter the alarm time when prompted.
The program will wait until the specified time to trigger the alarm.

### Customization
You can customize the alarm sound by replacing alarm.mp3 with your desired audio file. Ensure that the audio file is in the same directory as your script.
