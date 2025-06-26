# Creating our first flask app.
# Routing rules and options
# 1. Static Route: e.g @aap.route('/about')
# 2. Dynamic Route(with parameters): route with input from page or user. Usually followed by a function
# e.g: @app.route('/user/<username>)
# def greet_user(username)
#   return f"hello, {username} !"
# 3. Type-Specific Dynamic route: the input has a specific datatype
# e.g @app.route('post/<int:post_id>) : Here the variable post_id has to be of type: integer
# 4. Multiple Routes for one function : when there are different route address for the same function
# e.g:
#   @app.route('/')
#   @app.route('/home')
#   def home():
#       return "Welcome"
# 5. Custom Method(HTTP METHODS):
#    Whenever a user interacts with your app (visiting a page, submitting a form), the browser sends a request using one of these HTTP methods:
#    Method	            Purpose	                    Used For
#       GET	            Get data from server	    Loading a page or URL
#       POST	        Send data to server	        Submitting forms, uploading files
#       PUT	            Update existing resource	API updates
#       DELETE	        Delete a resource	        API deletions
# 
# In flask the default is GET, for example
# @app.route('/hello')
# def hello():
#     return "Hello"
# If you write the above code, It only responds to GET requests, like when a user visits the URL in a browser.

from flask import Flask

app = Flask(__name__)
# This line creates your Flask application object, which acts as the core of your web app.
# Flask(...) : This is a class provided by the Flask framework. When you do Flask(...), you're creating an instance of the Flask app.
#✅ __name__ : This is a special built-in variable in Python. It tells Flask where it is running from.

@app.route('/')                             # When someone goes to http://localhost:5000/
def home():
    return "Welcome to the Home Page!"

@app.route('/about')                        # When someone visits http://localhost:5000/about
def about():
    return "This is the About Page."

@app.route('/product/<int:product_id>')     
#/product/<int:product_id> is a dynamic route.
# <int:product_id> means the value in that part of the URL is an integer and will be passed to the function as a variable named product_id.
def product_detail(product_id):
    return f"Details for product ID: {product_id}"

# # To Allow both GET and POST:
# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         return "Form Submitted!"
#     return "This is the form page."
# If the user visits the page, it’s a GET → "This is the form page."
# If the user submits a form, it sends a POST → "Form Submitted!"


if __name__ == '__main__':
    app.run(debug=True)
