from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
import config
import pymongo

#Récupération des variables d'environnement
cluster =config.environ['CLUSTER']
username =config.environ['USERNAME']
dbname =config.environ['DBNAME']
password =config.environ['PASSWORD']

# Connexion à la base de données MongoDB
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.kxpd59z.mongodb.net/")



class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    # Create the user object
    # Spécifiez la base de données que vous souhaitez utiliser
    db = client[f"{dbname}"]
    db = client.user_login_system
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Adresse Email déjà utilisée!" }), 400

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Création de compte échouée!" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):
    db = client[f"{dbname}"]
    db = client.user_login_system
    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Paramètres de connexion invalides!" }), 401
  

           

    
