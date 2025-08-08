from flask import Flask, render_template, request, redirect, url_for, flash
from space_explorer import Player, Spacecraft, Planet

app = Flask(__name__)
app.secret_key = 'space_explorer_secret'

# Global game state
player = Player()
spacecraft = Spacecraft()

@app.route('/')
def index():
    return render_template('index.html', player=player, spacecraft=spacecraft)

@app.route('/add_fuel', methods=['POST'])
def add_fuel():
    fuel_amount = int(request.form['fuel_amount'])
    spacecraft.add_fuel(fuel_amount)
    flash(f'Added {fuel_amount} fuel')
    return redirect(url_for('index'))

@app.route('/add_planet', methods=['POST'])
def add_planet():
    name = request.form['name']
    coords = list(map(int, request.form['coordinates'].split(',')))
    danger = int(request.form['danger'])
    resources = int(request.form['resources'])
    atmosphere = request.form['atmosphere']
    
    planet = Planet(name, coords, danger, resources, atmosphere)
    player.planets.append(planet)
    flash(f'Added planet: {name}')
    return redirect(url_for('index'))

@app.route('/launch_mission', methods=['POST'])
def launch_mission():
    planet_name = request.form['planet']
    selected_planet = None
    
    for planet in player.planets:
        if planet.name == planet_name:
            selected_planet = planet
            break
    
    if selected_planet:
        fuel_required = selected_planet.calc_fuel_required(selected_planet.coordinates, spacecraft.fuel_efficiency)
        if spacecraft.fuel_level >= fuel_required:
            spacecraft.fuel_level -= fuel_required
            player.credits += 100
            flash(f'Mission to {selected_planet.name} successful! Earned 100 credits.')
        else:
            flash(f'Not enough fuel! Need {fuel_required}, have {spacecraft.fuel_level}')
    else:
        flash('Planet not found!')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)