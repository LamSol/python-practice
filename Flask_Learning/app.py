# Creating our first flask app.
# 
from flask import Flask

# This line creates your Flask application object, which acts as the core of your web app.
# Flask(...) : This is a class provided by the Flask framework. When you do Flask(...), you're creating an instance of the Flask app.
#✅ __name__ : This is a special built-in variable in Python. It tells Flask where it is running from.
app = Flask(__name__)

@app.route('/')                             # When someone goes to http://localhost:5000/
def home():
    return "Welcome to the Home Page!"

@app.route('/about')                        # When someone visits http://localhost:5000/about
def about():
    return "This is the About Page."

@app.route('/product/<int:product_id>')     #/product/<int:product_id> is a dynamic route.
# <int:product_id> means the value in that part of the URL is an integer and will be passed to the function as a variable named product_id.
def product_detail(product_id):
    return f"Details for product ID: {product_id}"

if __name__ == '__main__':
    app.run(debug=True)
