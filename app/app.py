from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Home route to display the password generator form
@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML template for the homepage

# Route to handle password generation after form submission
@app.route('/generate', methods=['POST'])
def generate_password():
    if request.method == 'POST':
        # Get the password length from the form input
        password_length = int(request.form['length'])
        
        # Generate a random password with letters, digits, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        
        return render_template('index.html', password=password)  # Display the generated password on the same page

if __name__ == '__main__':
    app.run(debug=True)
