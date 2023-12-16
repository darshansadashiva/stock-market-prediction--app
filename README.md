<h1>Stock Price Prediction System</h1>
<h2>Overview</h2>
Welcome to the Stock Price Prediction System – an integrated solution that combines full-stack web development with machine learning to provide real-time insights into stock price movements.

<h2>Features</h2>
<b>Full Stack Web Development:</b><br>
Utilizes Flask (Python Web Framework), HTML5, CSS3, Ajax, and jQuery for an intuitive and responsive web interface.
User-friendly registration and login pages for personalized experiences.

<b>Real-time Stock Data:</b><br>
Integrates Yahoo Finance API (yfinance) for seamless retrieval of real-time stock data.

<b>User Authentication:</b> <br>
MySQL manages secure user registration and login credentials.

<b>Machine Learning:</b><br>
Employs Python, Streamlit, and Keras to develop an advanced predictive model.
Trained on historical stock data, the model analyzes trends and patterns for insightful predictions.
Tech Stack

<b>Web Development:</b> <br>
Flask <br>
HTML5, CSS3, Ajax, jQuery <br>
MySQL for user authentication <br>

<b>Data Source:</b> <br>
Yahoo Finance API (yfinance)

<b>Machine Learning:</b> <br>
Python, Streamlit, Keras

<h2>Getting Started</h2>
<b>Clone the Repository:</b> <br>
git clone https://github.com/darshansadashiva/stock-market-prediction--app <br>

<b>Install Dependencies:</b> <br>
pip install -r requirements.txt    

<b>Initial SetUp:</b> <br>
1.Install Xampp <br>
2.Create a database named 'userdb' <br>
3.Create a table by using below MySql Query: <br>
      CREATE TABLE userdata <br>
      ( <br>
        id int AUTO_INCREMENT Primary KEY, <br>
        username varchar(50), <br>
        name varchar(50), <br>
        email varchar(50), <br>
        gender varchar(50), <br>
        pswd varchar(50), <br>
        cfpswd varchar(50) <br>
      ) <br>

<b>Run the application:</b> <br>
app-run.bat
