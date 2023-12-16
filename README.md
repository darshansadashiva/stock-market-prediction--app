<h1>Stock Price Prediction System</h1>
<h3>Overview</h3>
Welcome to the Stock Price Prediction System – an integrated solution that combines full-stack web development with machine learning to provide real-time insights into stock price movements.

<h3>Features</h3>
<b>Full Stack Web Development:</b>
Utilizes Flask (Python Web Framework), HTML5, CSS3, Ajax, and jQuery for an intuitive and responsive web interface.
User-friendly registration and login pages for personalized experiences.

<b>Real-time Stock Data:</b>
Integrates Yahoo Finance API (yfinance) for seamless retrieval of real-time stock data.

<b>User Authentication:</b>
MySQL manages secure user registration and login credentials.

<b>Machine Learning:</b>
Employs Python, Streamlit, and Keras to develop an advanced predictive model.
Trained on historical stock data, the model analyzes trends and patterns for insightful predictions.
Tech Stack

<b>Web Development:</b>
Flask
HTML5, CSS3, Ajax, jQuery
MySQL for user authentication

<b>Data Source:</b>
Yahoo Finance API (yfinance)

<b>Machine Learning:</b>
Python, Streamlit, Keras

<h3>Getting Started</h3>
<b>Clone the Repository:</b>
git clone https://github.com/darshansadashiva/stock-market-prediction--app

<b>Install Dependencies:</b>
pip install -r requirements.txt    

Initial SetUp:
1.Install Xampp
2.Create a database named 'userdb'
3.Create a table by using below MySql Query:
      CREATE TABLE userdata
      (
        id int AUTO_INCREMENT Primary KEY,
        username varchar(50),
        name varchar(50),
        email varchar(50),
        gender varchar(50),
        pswd varchar(50),
        cfpswd varchar(50)
      )

Run the application:
app-run.bat

