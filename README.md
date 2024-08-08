# Stock Price Prediction System

Welcome to the Stock Price Prediction System – an integrated solution that combines full-stack web development with machine learning to provide real-time insights into stock price movements.

## Overview

The Stock Price Prediction System is a web-based application that leverages advanced machine learning algorithms to predict stock prices based on historical data. Built with a combination of Python's Flask web framework, machine learning libraries like Keras, and real-time data integration using the Yahoo Finance API, this system offers users a powerful tool to forecast stock trends and make informed investment decisions.

## Features

### Full Stack Web Development:
- **Flask Framework:** The core of the application, managing web requests and rendering templates.
- **Frontend:** Built with HTML5, CSS3, Ajax, and jQuery, ensuring a responsive and user-friendly interface.
- **User Authentication:** Secure registration and login system using MySQL, providing personalized experiences.

### Real-time Stock Data:
- **Yahoo Finance API Integration:** Seamlessly retrieves up-to-date stock prices and historical data for analysis.

### Machine Learning:
- **Advanced Predictive Modeling:** Utilizes Python's Keras library to build and train a model on historical stock data, allowing the system to predict future stock prices based on trends and patterns.
- **Streamlit:** A framework for deploying the machine learning model, making it accessible and interactive for end users.

## Tech Stack

### Web Development:
- **Backend:** Flask (Python Web Framework)
- **Frontend:** HTML5, CSS3, Ajax, jQuery
- **Database:** MySQL (for user authentication and data storage)

### Data Source:
- **Yahoo Finance API (yfinance):** Provides real-time stock data for analysis.

### Machine Learning:
- **Python Libraries:** Streamlit, Keras (for building and deploying predictive models)

## Getting Started

### Clone the Repository:
```bash
git clone https://github.com/darshansadashiva/stock-market-prediction--app
cd stock-market-prediction--app
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Initial Setup:

1. **Install XAMPP:**
   - Download and install XAMPP to set up a local MySQL server.

2. **Create the Database:**
   - Open phpMyAdmin (or use the MySQL command line) and create a database named `userdb`.

3. **Create the User Data Table:**
   - Run the following MySQL query to create the necessary table:
   ```sql
   CREATE TABLE userdata (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50),
       name VARCHAR(50),
       email VARCHAR(50),
       gender VARCHAR(50),
       pswd VARCHAR(50),
       cfpswd VARCHAR(50)
   );
   ```

### Run the Application:

1. **Start the MySQL Server:**
   - Launch XAMPP and start the MySQL module.

2. **Run the Flask Application:**
   - Execute the following command in your project directory:
   ```bash
   python app.py
   ```
   - Alternatively, you can run the application using the provided batch script:
   ```bash
   app-run.bat
   ```

3. **Access the Application:**
   - Open a web browser and go to `http://127.0.0.1:5000/` to start using the Stock Price Prediction System.

## Usage

1. **Register or Log In:**
   - New users can register with their details, while existing users can log in with their credentials.

2. **Search for Stock Data:**
   - Enter a stock ticker symbol (e.g., AAPL for Apple) to retrieve real-time stock data and view historical trends.

3. **Predict Stock Prices:**
   - The system will analyze the data and provide a forecast for future stock prices, helping you make informed decisions.

4. **View Historical Data:**
   - Use the interactive charts to explore past stock performance and understand market trends.

## Author

- **Darshan Sadashiva**
  - LinkedIn: [Darshan Sadashiva](https://www.linkedin.com/in/darshansadashiva/)
  - GitHub: [Darshan Sadashiva](https://github.com/darshansadashiva)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Flask:** The Python web framework that made building this application seamless.
- **Keras:** For providing the deep learning tools necessary for accurate stock predictions.
- **Streamlit:** For creating an interactive environment for deploying the machine learning model.
- **Yahoo Finance API:** For offering real-time stock data, making the predictions both relevant and timely.

---
