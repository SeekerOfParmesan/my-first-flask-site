from flask import Flask, render_template, request
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


#legends
all = [
  ['Bloodhound', 'Season 0'],
  ['Gibraltar', 'Season 0'],
  ['Lifeline', 'Season 0'],
  ['Pathfinder', 'Season 0'],
  ['Wraith', 'Season 0'],
  ['Bangalore', 'Season 0'],
  ['Caustic', 'Season 0'],
  ['Mirage', 'Season 0'],
  ['Octane', 'Season 1'],
  ['Wattson', 'Season 2'],
  ['Crypto', 'Season 3'],
  ['Revenant', 'Season 4'],
  ['Loba', 'Season 5'],
  ['Rampart', 'Season 6'],
  ['Horizon', 'Season 7'],
  ['Fuse', 'Season 8'],
  ['Valkyrie', 'Season 9'],
  ['Seer', 'Season 10'],
  ['Ash', 'Season 11']


]


# legends = ['Bloodhound','Gibraltar','Lifeline','Pathfinder','Wraith','Bangalore','Caustic','Mirage','Octane','Wattson','Crypto','Revenant','Loba','Rampart','Horizon','Fuse','Valkyrie','Seer']
# seasons = ['Season 0','Season 0','Season 0','Season 0','Season 0','Season 0','Season 0','Season 0','Season 1','Season 2','Season 3','Season 4','Season 5','Season 6','Season 7','Season 8','Season 9','Season 10']


@app.route('/info/legends/')
def leg_ends():
  return render_template('legends.html', all=all)

#guns
gun_go_brr = ['R301','P2020']
@app.route('/info/guns/')
def guns():
  return render_template('guns.html',gun_go_brr=gun_go_brr)

main_legend = []

@app.route('/info/legends/mains/', methods=['POST'])
def mains():
  print("request ", request.form)
  main = request.form["main"]
  main_legend.append(main)

  return render_template('legend_main.html',
  main_legend = main_legend)













if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )