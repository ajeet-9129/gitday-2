from flask import Flask, render_template, request

# Create the Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Result route to handle form submission
@app.route('/result', methods=['POST'])
def result():
    # Get the value from the form input
    name = request.form['name']
    return f"Hello i am Ajeet, {name}!"

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)

