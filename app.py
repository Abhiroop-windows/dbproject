from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Sample data for players and formations
players = []
formations = []

# Dummy user data for authentication
users = {
    "admin": "password123",  # Replace with secure password management in a real app
}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', players=players, formations=formations)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password match
        if username in users and users[username] == password:
            session['username'] = username  # Store the username in the session
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/team_management', methods=['GET', 'POST'])
def team_management():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    if request.method == 'POST':
        if 'add_player' in request.form:
            # Code to add player
            name = request.form['name']
            position = request.form['position']
            team_name = request.form['team_name']
            jersey_number = request.form['jersey_number']
            players.append({'id': len(players) + 1, 'name': name, 'position': position, 'team_name': team_name, 'jersey_number': jersey_number})
            flash('Player added successfully!', 'success')
        
        elif 'add_formation' in request.form:
            # Code to add formation
            formation_name = request.form['formation_name']
            formation_type = request.form['formation']
            formations.append({'name': formation_name, 'formation_type': formation_type})
            flash('Formation added successfully!', 'success')

        elif 'clear_data' in request.form:
            players.clear()
            formations.clear()
            flash('All data cleared!', 'danger')

    return render_template('index.html', players=players, formations=formations)

if __name__ == '__main__':
    app.run(debug=True)