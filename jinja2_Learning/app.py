from flask import Flask, render_template
app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return render_template('Welcome.html',username = name)

@app.route('/user/<name>')
def user(name):
    age = 25
    hobbies = ["Football", "Guitar", "Coding"]
    return render_template('profile.html', name=name, age=age, hobbies=hobbies)


if __name__ == '__main__':
    app.run(debug = True)

