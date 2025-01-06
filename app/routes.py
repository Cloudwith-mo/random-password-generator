from flask import Blueprint, render_template, request
import random
import string

# Create a Blueprint instance
main = Blueprint('main', __name__)

# Password generation function
def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Route to handle the password generation
@main.route('/', methods=['GET', 'POST'])
def index():
    password = None

    if request.method == 'POST':
        # Get the length from the form input
        length = int(request.form['length'])
        # Generate the password based on the given length
        password = generate_random_password(length)

    return render_template('password.html', password=password)
