from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from .api.routes import api_bp
from .services.strapi_service import get_streaming_services, get_games, get_featured_content, get_strapi_headers
import requests
from flask import current_app

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
    

    @app.route('/test-connection')
    def test_connection():
        url = f"{current_app.config['STRAPI_URL']}/api/streaming-services?populate=*"
        headers = get_strapi_headers()
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return jsonify({"status": "success", "message": "Connected to Strapi successfully"})
            else:
                return jsonify({"status": "error", "message": f"Connection failed with status code {response.status_code}"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})

    return app


app = create_app()

if __name__ == '__main__':
    # Get the PORT from environment variable for Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)