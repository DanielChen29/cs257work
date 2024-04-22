import flask

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Green">' + word1 + '</h1>'

@app.route('/add/<int1>/<int2>')
def my_display(int1, int2):
    the_string = int1 + " + " + int2 + " = " + (int1 + int2);
    return the_string

if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 