
# IDR 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Enhanced IDR Dashboard is a web-based interface designed to display real-time data from an Intrusion Detection and Response (IDR) system. It provides a comprehensive view of network traffic, alerts, threat statistics, and recent activities, helping security teams monitor and respond to security incidents effectively.

## Features

- Real-time network traffic chart using Chart.js
- Real-time alert distribution pie chart using Chart.js
- Alert summary table
- Recent activity logs
- Threat statistics table
- Geographic threat map using Leaflet.js
- Export data to PDF and CSV
- Advanced filters for date range and threat type

## Prerequisites

- Python 3.x
- Flask
- Chart.js
- Leaflet.js
- jQuery
- pandas (for CSV export)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SethVasvi/Identity-Detection-and-Response/
    cd Identity-Detection-and-Response
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Flask Server

1. **Navigate to the server directory and start the Flask server:**

    ```bash
    cd management_console
    python app.py
    ```

2. **Navigate to the agent directory and start the IDR agent script:**

    ```bash
    cd ids_agent
    python agent.py
    ```

### Accessing the Dashboard

Open a web browser and go to `http://localhost:5000`. Use the credentials (`admin` / `password`) to log in.


## Configuration

The configuration for the project, including credentials and server settings, can be adjusted in the respective configuration files within the `management_console` and `ids_agent` directories.

## Testing

1. **Run the Flask Server:**

    ```bash
    cd management_console
    python app.py
    ```

2. **Run the IDR Agent:**

    ```bash
    cd ids_agent
    python agent.py
    ```

3. **Access the Dashboard:**

    Navigate to `http://localhost:5000` and log in with the provided credentials.

4. **Verify Real-Time Data:**

    Ensure that the dashboard updates in real-time with the data being sent by the agent.

5. **Test Export and Filters:**

    Test the export buttons and filter form to ensure they work as expected. Check the browser console, Flask server logs, and agent script output for any error messages and troubleshoot accordingly.

## Contributing

We welcome contributions to the Enhanced IDR Dashboard project. If you would like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Feel free to customize the content as per your specific project requirements.
