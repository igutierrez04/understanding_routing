from flask import Flask
app = Flask(__name__)


# Create a URL request that return "Hello World!"
@app.route('/')
def hello():
    return "Hello World!"

# Create a URL request that returns "Dojo!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

# Create a URL pattern that can handle the following examples
# Have it say "Hi Flask!"
# Have it say "Hi Michael!"
# Have it say "Hi Jhon!"

@app.route('/say/<string:name>')
def say(name):
    print(name)
    return f"Hi {name}!"

# Create one URL pattern that can handle the following examples
# Have it say "hello" 35 times
# Have it say "bye" 80 times
# Have it say "dogs" 99 times

@app.route('/repeat/<int:num>/<string:word>')
def repeat(word, num):
    print(num)
    print(word)
    return f"{word * num}"




if __name__ =="__main__":
    app.run(debug=True)