from flask import Flask, render_template, request, jsonify
from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (name, age, gender, address, phone, adhaar_no, pin, balance) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (data['name'], data['age'], data['gender'], data['address'], data['phone'], data['adhaar_no'], data['pin'], data['balance'])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Customer added successfully!"})

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET balance = balance + ? WHERE id = ?", (data['amount'], data['account_id']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deposit successful!"})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET balance = balance - ? WHERE id = ?", (data['amount'], data['account_id']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Withdrawal successful!"})

if __name__ == '__main__':
    app.run(debug=True)
