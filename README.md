# Automated Visa Appointment Checker and Rescheduler

This project provides a Python script to automate the process of checking for available visa appointment slots on the US embassy website and rescheduling to the earliest available slot before December 2024.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (version 3.6 or above)
- Selenium Python package (install using `pip install selenium`)
- ChromeDriver executable (download from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it matches your Chrome browser version)

## Configuration

1. Update the `username` and `password` variables in the script with your login credentials for the US embassy website.

2. Set the correct path to the ChromeDriver executable by updating the `chromedriver_path` variable in the script.

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script using the command: `python visa_appointment.py`

4. The script will open a Chrome browser, login to the US embassy website, accept the privacy policy, check for available slots, and reschedule to the earliest available slot before December 2024. The output will be displayed in the terminal.

## Note

- This script is intended for educational and personal use only. Please use it responsibly and in compliance with the terms of service and usage policies of the US embassy website.

- The script assumes that the HTML structure and element identifiers on the website have not changed. If there are any changes to the website's structure or identifiers, you may need to modify the script accordingly.

- If you encounter any issues or have any suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
