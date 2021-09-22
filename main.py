from flask import Flask, render_template

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page (now using the index.html file)
@app.route('/')
def index():
  return render_template('index.html')


#trollos
@app.route('/admin/<string:name>/')
def admin(name):
  return render_template('trolled.html', name=name)

#client
@app.route('/client/<string:username>/')
def client(username):
  return render_template('client.html', username=username)



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )