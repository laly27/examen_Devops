from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuration de la base SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle de réservation
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    heure = db.Column(db.String(10), nullable=False)
    personnes = db.Column(db.Integer, nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

# Page d'accueil
@app.route("/")
def accueil():
    return render_template("index.html")

# Page réservation
@app.route("/reserver", methods=['GET', 'POST'])
def reserver():
    if request.method == 'POST':
        nom = request.form['nom']
        telephone = request.form['telephone']
        date = request.form['date']
        heure = request.form['heure']
        personnes = request.form['personnes']
        nouvelle_resa = Reservation(nom=nom, telephone=telephone, date=date, heure=heure, personnes=personnes)
        db.session.add(nouvelle_resa)
        db.session.commit()
        return redirect(url_for('accueil'))
    return render_template("reservation.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)


