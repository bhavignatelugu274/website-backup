from flask import Flask, request, render_template
import subprocess, psycopg2


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_id=request.form['user_id']
    full_name=request.form['full_name']
    email = request.form['email']
    password = request.form['password']
    phone=request.form['phone']
    registration_date=request.form['registration_date']
    
    # 🔽 Your logic here: print/save/send data
    print(f"user_id: {user_id},full_Name: {full_name}, Email: {email}, Password: {password},phone:{phone},registration_date:{registration_date}")
        
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="bhavi",
        host="localhost",  # or your server IP
        port="5432"         # default PostgreSQL port
    )

    # Create a cursor
    cur = conn.cursor()

    #cur.execute("""
    # INSERT INTO users (user_id, full_name,email,password,phone,registration_date) VALUES (%d,%s,%c,%d,%d,%d) """, ("1","Alice", "alice@example.com","alice","1234","123456","2025-07-18"))

    # cur.execute("INSERT INTO registration_form (user_id, full_name,email,password,phone,registration_date) VALUES (user_id,full_name,email,password,phone,registration_date)")

    cur.execute("""
        INSERT INTO registration_form (user_id, full_name,email,password,phone,registration_date)
        VALUES (%s,%s,%s,%s,%s,%s);
        """,
        (user_id,full_name,email,password,phone,registration_date)
    )

    # Commit the transaction
    conn.commit()

    # Close connection
    cur.close()
    conn.close()

    return f"Welcome, {full_name}! Registration successful."

if __name__ == '__main__':
    app.run(debug=True)
   # subprocess.run(["python", "insert_postgreSQlpt.py"])

