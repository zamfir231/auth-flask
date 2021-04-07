from flask import Blueprint, render_template, url_for, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 character.', category="error")

        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category="error")

        elif password1 != password2:
            flash('Passwords don\'t match!', category="error")

        elif len(password1) < 7:
            flash('Password must be at least 7 characters long.', category="error")

        else:
            flash('Account created!', category="success")

    return render_template('sign_up.html')
