from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from .api.routes import api_bp
from .services.strapi_service import get_streaming_services, get_games, get_featured_content

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Config
    app.config.from_object('flask_app.config.Config')
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Main routes
    @app.route('/')
    def index():
        featured = get_featured_content()
        if not isinstance(featured, list):
            featured = []
        return render_template('index.html', featured=featured)
    
    @app.route('/streaming')
    def streaming():
        services = get_streaming_services()
        return render_template('streaming.html', services=services)
    
    @app.route('/gaming')
    def gaming():
        games = get_games()
        return render_template('gaming.html', games=games)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)