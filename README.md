# PI-1
# SafeDesk: Intelligent Security System for University Computers

## Project Overview

SafeDesk is an advanced security system designed to protect university computers using a combination of IoT hardware, facial recognition, and real-time alerts. Unlike traditional security cameras, SafeDesk prevents theft by detecting unauthorized movements and immediately notifying security personnel with relevant details, including the photo of the person who removed the equipment.

## Key Features

- **Real-time Monitoring** – Detects unauthorized movements of computers near classroom exits.
- **Instant Alerts** – Sends notifications within 5 seconds to security personnel.
- **Facial Recognition AI** – Identifies unauthorized users using a database of authorized personnel.
- **Wireless Connectivity** – Ensures remote access and communication.
- **Web-based Management** – Allows admin control over users, devices, and security logs.
- **History Log** – Stores alerts with date, time, location, and user details.

## System Requirements

### Hardware
- IoT sensors for proximity detection
- Camera for facial recognition
- Wireless communication module (Wi-Fi/Bluetooth)
- Alarm system for audible alerts

### Software
- Web application for system management
- AI-powered facial recognition API
- Database for storing authorized personnel and equipment data
- Integration with messaging services (e.g., Telegram) for alerts

## Installation and Setup

### 1. Hardware Deployment:
- Install IoT sensors and cameras near classroom exits.
- Connect devices to the SafeDesk network.
- Ensure cameras have a clear field of view for facial recognition.

### 2. Software Installation:
- Deploy the web application on a university server.
- Configure the database for users and computers.
- Set up the alert system with real-time notifications.

### 3. Configuration:
- Register authorized personnel in the system.
- Define security policies, including allowed removal times.
- Test facial recognition and notification delivery.

## Usage

1. **Detection:** If a computer is moved near a door, the system triggers an alert.
2. **Validation:** SafeDesk performs facial recognition within 3 minutes.
3. **Alert Transmission:** If unauthorized, the system sends a photo and alert to security staff.
4. **Logging:** All events are stored for future review and analysis.

   # SafeDesk – Library Installation
   ## Prerequisites

- Python 3.10 or higher.
- pip (Python package manager).

## Installing the Required Libraries

Follow these steps to install the necessary libraries:

1. Open a terminal or command prompt.
2. Navigate to the root directory of the project
3. clone our project using git clone [link of our project]

4. Run the following command to install the dependencies:

   ```bash
   pip install django
   
5.verify the intallation by running:
python -m django --version

6. you will find an archive called requirements.txt
7. use the next commant to install the libraries that you found in the .txt
    ```bash
    pip install -r requirements.txt
    
8. Once the libraries are installed, you can proceed with project setup and then run the server:
   
   python manage.py migrate
   
   python manage.py 

9. Access http://127.0.0.1:8000 to see the project in action.

10. You can use This users and passwords to test the system
   As an administrator Rol:
   User: Administrador123
   Password:  eafit123*

   As an User Rol:
   User: mvc0212
   Password: mari123
## System use like an administrator
1. On the main page you will find access to several of the main tabs such as:
    Alerts, authorized personnel, computer and user management.
2. If you enter any page you will find information about each component.
3. 





## Contributors
Alexandra Hurtado 
Mariana Valderrama 
Luis Angel Nerio
Isabella Camacho

SafeDesk is a proactive solution to enhance campus security, ensuring a safer and smarter environment for students and staff.

