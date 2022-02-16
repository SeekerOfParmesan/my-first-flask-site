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
  ['Revenant', 'Season 4',"https://kraber.herokuapp.com/info/legends/Revenant/"],
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
  ['R-301 carbine', 'Light ammo', 'R201', "https://kraber.herokuapp.com/info/guns/R301/"],
  ['P2020', 'Light ammo', 'P2019', "https://kraber.herokuapp.com/info/guns/P2020/"],
  ['RE-45 auto', 'Light ammo', 'RE-45', "https://kraber.herokuapp.com/info/guns/RE45/"],
  ['R-99', 'Light ammo', 'R-97', "https://kraber.herokuapp.com/info/guns/R99/"],
  ['G7 scout', 'Carepackage(Light ammo)', 'G7 scout', "https://kraber.herokuapp.com/info/guns/Scout/"],
  ['Alternator', 'Carepackage(Light ammo)', 'Alternator', "https://kraber.herokuapp.com/info/guns/Alternator/"],
  ['VK-47 flatline', 'Heavy ammo', 'VK-47 flatline', "https://kraber.herokuapp.com/info/guns/Flatline/"],
  ['Rampage', 'Heavy ammo', 'N.A', "https://kraber.herokuapp.com/info/guns/Rampage/"],
  ['Prowler burst PDW', 'Heavy ammo', 'N.A', "https://kraber.herokuapp.com/info/guns/Prowler/"],
  ['CAR smg', 'Heavy/light ammo', 'CAR SMG', "https://kraber.herokuapp.com/info/guns/CAR/"],
  ['Hemlok burst AR', 'Heavy ammo', 'Hemlok burst AR', "https://kraber.herokuapp.com/info/guns/Hemlok/"],
  ['Wingman', 'Heavy ammo', 'Wingman', "https://kraber.herokuapp.com/info/guns/Wingman/"],
  ['30-30 Repeater', 'Heavy ammo', 'N.A', "https://kraber.herokuapp.com/info/guns/3030/"],
  ['M600 Spitfire', 'Carepackage(Heavy ammo)', 'M600 Spitfire', "https://kraber.herokuapp.com/info/guns/Spitfire/"],
  ['Bocek compound bow', 'Arrows', 'N.A', "https://kraber.herokuapp.com/info/guns/Bocek/"],
  ['HAVOC Rifle', 'Energy ammo', 'N.A', "https://kraber.herokuapp.com/info/guns/HAVOC/"],
  ['Devotion LMG', 'Energy ammo', 'Devotion LMG', "https://kraber.herokuapp.com/info/guns/Devotion/"],
  ['Volt SMG', 'Energy ammo', 'Volt SMG', "https://kraber.herokuapp.com/info/guns/Volt/"],
  ['L-STAR EMG', 'Energy ammo', 'L-STAR EMG', "https://kraber.herokuapp.com/info/guns/Lstar/"],
  ['Triple Take', 'Energy ammo', 'Double Take', "https://kraber.herokuapp.com/info/guns/Triple/"],
  ['EVA-8 Auto', 'Shotgun ammo', 'EVA-8 Auto', "https://kraber.herokuapp.com/info/guns/EVA/"],
  ['Mastiff Shotgun', 'Shotgun ammo', 'Mastiff Shotgun', "https://kraber.herokuapp.com/info/guns/Mastiff/"],
  ['Mozambique Shotgun', 'Shotgun ammo', 'Mozambique Shotgun', "https://kraber.herokuapp.com/info/guns/Mozambique/"],
  ['Peacekeaper', 'Shotgun ammo', 'N.A', "https://kraber.herokuapp.com/info/guns/Peacekeeper/"],
  ['Charge Rifle', 'Sniper ammo', 'Charge Rifle', "https://kraber.herokuapp.com/info/guns/Charge/"],
  ['Longbow DMR', 'Sniper ammo', 'DMR', "https://kraber.herokuapp.com/info/guns/Longbow/"],
  ['Sentinel', 'Sniper ammo', 'N.A', "https://kraber.herokuapp.com/info/guns/Sentinel/"],
  ['Kraber .50 cal', 'Carepackage(Sniper)', 'Kraber', "https://kraber.herokuapp.com/info/guns/Kraber/"],
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

@app.route('/info/legends/Mirage/')
def mirage():
  return render_template('fold-legends/mirage.html')

@app.route('/info/legends/Octane/')
def Octane():
  return render_template('fold-legends/octane.html')

@app.route('/info/legends/Wattson/')
def Wattson():
  return render_template('fold-legends/wattson.html')

@app.route('/info/legends/Crypto/')
def crypto():
  return render_template('fold-legends/crypto.html')

@app.route('/info/legends/Revenant/')
def Rev():
  return render_template('fold-legends/revenant.html')
  
@app.route('/info/legends/Loba/')
def loba():
  return render_template('fold-legends/loba.html')

@app.route('/info/legends/Rampart/')
def rampart():
  return render_template('fold-legends/rampart.html')

@app.route('/info/legends/Horizon/')
def Horizon():
  return render_template('fold-legends/horizon.html')

@app.route('/info/legends/Fuse/')
def fuse():
  return render_template('fold-legends/fuse.html')

@app.route('/info/legends/Valkyrie/')
def Valk():
  return render_template('fold-legends/valk.html')

@app.route('/info/legends/Seer/')
def seer():
  return render_template('fold-legends/seer.html')

@app.route('/info/legends/Ash/')
def ash():
  return render_template('fold-legends/ash.html')

#-------------------------------------------------
#hier starten de gun htmls

@app.route('/info/guns/R301/')
def r3():
  return render_template('fold-guns/r301.html')

@app.route('/info/guns/P2020/')
def p20():
  return render_template('fold-guns/p20.html')

@app.route('/info/guns/RE45/')
def re45():
  return render_template('fold-guns/re45.html')

@app.route('/info/guns/R99/')
def r9():
  return render_template('fold-guns/r9.html')

@app.route('/info/guns/Scout/')
def g7():
  return render_template('fold-guns/g7.html')

@app.route('/info/guns/Alternator/')
def alt():
  return render_template('fold-guns/alt.html')

@app.route('/info/guns/Flatline/')
def flatline():
  return render_template('fold-guns/flatline.html')

@app.route('/info/guns/Rampage/')
def rampage():
  return render_template('fold-guns/rampage.html')

@app.route('/info/guns/Prowler/')
def PDW():
  return render_template('fold-guns/PDW.html')

@app.route('/info/guns/Hemlok/')
def hemlok():
  return render_template('fold-guns/hemlok.html')

@app.route('/info/guns/Wingman/')
def wingman():
  return render_template('fold-guns/wingman.html')

@app.route('/info/guns/3030/')
def repeater():
  return render_template('fold-guns/repeater.html')

@app.route('/info/guns/Spitfire/')
def spitfire():
  return render_template('fold-guns/spitfire.html')

@app.route('/info/guns/Bocek/')
def bow():
  return render_template('fold-guns/bow.html')

@app.route('/info/guns/HAVOC/')
def havoc():
  return render_template('fold-guns/havoc.html')

@app.route('/info/guns/Devotion/')
def devo():
  return render_template('fold-guns/devo.html')

@app.route('/info/guns/Volt/')
def volt():
  return render_template('fold-guns/volt.html')

@app.route('/info/guns/Lstar/')
def EMG():
  return render_template('fold-guns/EMG.html')

@app.route('/info/guns/Triple/')
def take():
  return render_template('fold-guns/take.html')

@app.route('/info/guns/EVA/')
def aa12():
  return render_template('fold-guns/aa12.html')

@app.route('/info/guns/Mastiff/')
def mastiff():
  return render_template('fold-guns/mastiff.html')

@app.route('/info/guns/Mozambique/')
def mozam():
  return render_template('fold-guns/mozam.html')

@app.route('/info/guns/Peacekeeper')
def pk():
  return render_template('fold-guns/pk.html')

@app.route('/info/guns/Charge/')
def charge():
  return render_template('fold-guns/charge.html')

@app.route('/info/guns/Longbow/')
def DMR():
  return render_template('fold-guns/DMR.html')

@app.route('/info/guns/Sentinel/')
def sentinel():
  return render_template('fold-guns/sentinel.html')

@app.route('/info/guns/Kraber/')
def kraber():
  return render_template('fold-guns/kraber.html')

@app.route('/info/guns/Car/')
def car():
  return render_template('fold-guns/car.html')


if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )