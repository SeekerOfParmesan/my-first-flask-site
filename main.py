from flask import Flask, render_template, request
# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# home page
@app.route('/')
def index():
  return render_template('index.html')



#Funny meme
@app.route('/client/<string:username>/')
def client(username):
  return render_template('client.html', username=username)


#Dit is een dictonary met lijsten voor legends.html
all_legends = [
  ['Bloodhound', 'Season 0',"https://kraber.herokuapp.com/info/legends/Bloodhound/"],
  ['Gibraltar', 'Season 0',"https://kraber.herokuapp.com/info/legends/Gibraltar/"],
  ['Lifeline', 'Season 0',"https://kraber.herokuapp.com/info/legends/Lifeline/"],
  ['Pathfinder', 'Season 0',"https://kraber.herokuapp.com/info/legends/Pathfinder/"],
  ['Wraith', 'Season 0',"https://kraber.herokuapp.com/info/legends/Wraith/"],
  ['Bangalore', 'Season 0',"https://kraber.herokuapp.com/info/legends/Bangalore/"],
  ['Caustic', 'Season 0',"https://kraber.herokuapp.com/info/legends/Caustic/"],
  ['Mirage', 'Season 0',"https://kraber.herokuapp.com/info/legends/Mirage/"],
  ['Octane', 'Season 1',"https://kraber.herokuapp.com/info/legends/Octane/"],
  ['Wattson', 'Season 2',"https://kraber.herokuapp.com/info/legends/Wattson/"],
  ['Crypto', 'Season 3',"https://kraber.herokuapp.com/info/legends/Crypto/"],
  ['Revenant', 'Season 4',"https://kraber.herokuapp.com/info/legends/Revanant/"],
  ['Loba', 'Season 5',"https://kraber.herokuapp.com/info/legends/Loba/"],
  ['Rampart', 'Season 6',"https://kraber.herokuapp.com/info/legends/Rampart/"],
  ['Horizon', 'Season 7',"https://kraber.herokuapp.com/info/legends/Horizon/"],
  ['Fuse', 'Season 8',"https://kraber.herokuapp.com/info/legends/Fuse/"],
  ['Valkyrie', 'Season 9',"https://kraber.herokuapp.com/info/legends/Valkyrie/"],
  ['Seer', 'Season 10',"https://kraber.herokuapp.com/info/legends/Seer/"],
  ['Ash', 'Season 11',"https://kraber.herokuapp.com/info/legends/Ash/"]


]

@app.route('/info/legends/')
def leg_ends():
  return render_template('legends.html', all_legends=all_legends)

#Dit is een dictonary met lijsten voor guns.html
all_guns = [
  ['R-301 carbine', 'Light ammo', 'R201'],
  ['P2020', 'Light ammo', 'P2019'],
  ['RE-45 auto', 'Light ammo', 'RE-45'],
  ['R-99', 'Light ammo', 'R-97'],
  ['G7 scout', 'Light ammo', 'G7 scout'],
  ['Alternator', 'Carepackage(Light ammo)', 'Alternator'],
  ['VK-47 flatline', 'Heavy ammo', 'VK-47 flatline'],
  ['Rampage', 'Heavy ammo', 'N.A'],
  ['Prowler burst PDW', 'Heavy ammo', 'N.A'],
  ['Hemlok burst AR', 'Heavy ammo', 'Hemlok burst AR'],
  ['Wingman', 'Heavy ammo', 'Wingman'],
  ['30-30 Repeater', 'Heavy ammo', 'N.A'],
  ['M600 Spitfire', 'Carepackage(Heavy ammo)', 'M600 Spitfire'],
  ['Bocek compound bow', 'Arrows', 'N.A'],
  ['HAVOC Rifle', 'Energy ammo', 'N.A'],
  ['Devotion LMG', 'Energy ammo', 'Devotion LMG'],
  ['Volt SMG', 'Energy ammo', 'Volt SMG'],
  ['L-STAR EMG', 'Energy ammo', 'L-STAR EMG'],
  ['Triple Take', 'Carepackage(Energy ammo)', 'Double Take'],
  ['EVA-8 Auto', 'Shotgun ammo', 'EVA-8 Auto'],
  ['Mastiff Shotgun', 'Shotgun ammo', 'Mastiff Shotgun'],
  ['Mozambique Shotgun', 'Shotgun ammo', 'Mozambique Shotgun'],
  ['Peacekeaper', 'Shotgun ammo', 'N.A'],
  ['Charge Rifle', 'Sniper ammo', 'Charge Rifle'],
  ['Longbow DMR', 'Sniper ammo', 'DMR'],
  ['Sentinel', 'Sniper ammo', 'N.A'],
  ['Kraber .50 cal', 'Carepackage(Sniper)', 'Kraber'],
]
@app.route('/info/guns/')
def guns():
  return render_template('guns.html', all_guns=all_guns)

main_legend = []

@app.route('/info/legends/mains/', methods=['POST'])
def mains():
  print("request ", request.form)
  main = request.form["main"]
  main_legend.append(main)

  return render_template('legend_main.html',
  main_legend = main_legend)

@app.route('/info/legends/Bloodhound/')
def Blood():
  return render_template('fold-legends/blood.html')

@app.route('/info/legends/Gibraltar/')
def Gibby():
  return render_template('fold-legends/gibby.html')

@app.route('/info/legends/Lifeline/')
def Lifeline():
  return render_template('fold-legends/lifeline.html')

@app.route('/info/legends/Pathfinder/')
def Path():
  return render_template('fold-legends/path.html')

@app.route('/info/legends/Wraith/')
def Wraith():
  return render_template('fold-legends/wraith.html')

@app.route('/info/legends/Bangalore/')
def Bangalore():
  return render_template('fold-legends/bangalore.html')

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )