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

@app.route('/info/legends/')
def leg_ends():
  return render_template('legends.html', all=all)

#guns
all = [
  ['R-301 carbine', 'Light ammo', 'R201'],
  ['P2020', 'Light ammo', 'P2019'],
  ['RE-45 auto', 'Light ammo', 'RE-45'],
  ['R-99', 'Light ammo', 'R-97']
  ['G7 scout', 'Light ammo', 'G7 scout']
  ['Alternator', 'Carepackage(Light ammo)', 'Alternator']
  ['VK-47 flatline', 'Heavy ammo', 'VK-47 flatline']
  ['Rampage', 'Heavy ammo', 'N.A']
  ['Prowler burst PDW', 'Heavy ammo', 'N.A']
  ['Hemlok burst AR', 'Heavy ammo', 'Hemlok burst AR']
  ['Wingman', 'Heavy ammo', 'Wingman']
  ['30-30 Repeater', 'Heavy ammo', 'N.A']
  ['M600 Spitfire', 'Carepackage(Heavy ammo)', 'M600 Spitfire']
  ['Bocek compound bow', 'Arrows', 'N.A']
  ['HAVOC Rifle', 'Energy ammo', 'N.A']
  ['Devotion LMG', 'Energy ammo', 'Devotion LMG']
  ['Volt SMG', 'Energy ammo', 'Volt SMG']
  ['L-STAR EMG', 'Energy ammo', 'L-STAR EMG']
  ['Triple Take', 'Carepackage(Energy ammo)', 'Double Take']
  ['EVA-8 Auto', 'Shotgun ammo', 'EVA-8 Auto']
  ['Mastiff Shotgun', 'Shotgun ammo', 'Mastiff Shotgun']
  ['Mozambique Shotgun', 'Shotgun ammo', 'Mozambique Shotgun']
  ['Peacekeaper', 'Shotgun ammo', 'N.A']
  ['Charge Rifle', 'Sniper ammo', 'Charge Rifle']
  ['Longbow DMR', 'Sniper ammo', 'DMR']
  ['Sentinel', 'Sniper ammo', 'N.A']
  ['Kraber .50 cal', 'Carepackage(Sniper)', 'Kraber']
]
@app.route('/info/guns/')
def guns():
  return render_template('guns.html', all=all)

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