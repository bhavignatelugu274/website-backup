from flask import Flask, request, render_template

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
    
    return f"Welcome, {full_name}! Registration successful."

if __name__ == '__main__':
    app.run(debug=True) 
