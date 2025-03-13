
Bank Management System

## Overview
This is a simple **Bank Management System** built with **Flask, HTML, CSS, and JavaScript**. It allows users to:
- Add new customers
- Deposit money
- Withdraw money
- View transactions

## Installation

1. Install Python (if not installed)
2. Clone the repository or create the folder manually.
3. Install dependencies:

pip install -r requirements.txt


4. Initialize the database:
python database.py


5. Run the application:

python app.py



6. Open **http://127.0.0.1:5000/** in a browser.

## Technologies Used
- Flask (Python)
- HTML, CSS, JavaScript
- SQLite Database

# **Bank Management System**

Overview
The **Bank Management System** is a simple web-based application built using **Flask, HTML, CSS, JavaScript, and SQLite**. It provides basic banking functionalities like adding customers, depositing money, withdrawing money, and viewing transactions.

## **Features**
- Add new customers with personal details.
- Deposit money into an account.
- Withdraw money from an account.
- View and manage transactions.
- User-friendly interface with responsive design.

## **Technologies Used**
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite

## **Installation & Setup**
Follow these steps to set up and run the project:

### **1. Install Python**
Ensure you have Python installed on your system. You can download it from [Python’s official website](https://www.python.org/).

### **2. Clone or Download the Repository**
If using Git, run:
```sh
git clone https://github.com/your-repository/bank_management_project.git
cd bank_management_project
```
Or manually create the project folder and files.

### **3. Install Required Dependencies**
Run the following command to install Flask and other required dependencies:
```sh
pip install -r requirements.txt
```

### **4. Set Up the Database**
Initialize the database by running:
```sh
python database.py
```
This will create `bank.db` with necessary tables.

### **5. Run the Application**
Start the Flask server by executing:
```sh
python app.py
```
The application will start on:
```
http://127.0.0.1:5000/
```

### **6. Open in Browser**
Visit **http://127.0.0.1:5000/** in your browser to access the application.
API Endpoints
Method	Endpoint	Description
POST	/add_customer	Add a new customer
POST	/deposit	Deposit money
POST	/withdraw	Withdraw money

Screenshots

This project is open-source under the MIT License.

## **Project Structure**
```
📁 bank_management_project
│── 📂 static
│   ├── 📂 css
│   │   ├── style.css
│   ├── 📂 js
│   │   ├── script.js
│── 📂 templates
│   ├── index.html
│   ├── dashboard.html
│   ├── transactions.html
│── app.py  # Flask Backend
│── database.py  # Database Connection
│── requirements.txt
│── README.md
│── bank.db  # SQLite Database (Generated)
```

## **Usage Guide**
1. **Add Customer**: Fill in customer details and submit.
2. **Deposit Money**: Enter the account ID and amount to deposit.
3. **Withdraw Money**: Enter the account ID and amount to withdraw.
4. **View Transactions**: Navigate to the transactions page.

## **Troubleshooting**
- If `.tables` shows no tables in SQLite, rerun `database.py` to create them.
- If `sqlite3` is not recognized, add it to system PATH or run SQLite commands manually.

## **Author**
N.Naveen
For queries, contact: nakkanaveen1817@gmail.com




