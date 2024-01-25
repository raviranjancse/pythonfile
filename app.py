from flask import Flask, request, jsonify
from flask_cors import CORS
from config import db, SECRET_KEY
from os import path, getcwd, environ
from dotenv import load_dotenv
from Entity.user import User
from Entity.bmi import BMI
from Entity.food_rem import Food_rem
from Entity.macros import Macros
from Entity.sleep import Sleep  
from Entity.water_track import Water_track

load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATINS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key = SECRET_KEY

    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():
        
        @app.route('/signup', methods=['POST'])
        def signup():
            data = request.form.to_dict(flat=True)

            new_user = User(
                username = data['username'],
                password = data['password'],
                email = data['email']
            )

            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg = "user signup is done successfully")

        # @app.route('/login', methods=['POST'])
        # def login():
        #     recv_username = request.args.get('username')
        #     recv_password = request.args.get('password')
        #     user = User.query.filter(username=recv_username).first()
        #     user = User.query.filter(password = recv_password).first()

        db.create_all()
        db.session.commit()

        return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)