from flask import Blueprint, jsonify, request
from ..services.strapi_service import (
    get_streaming_services, 
    get_games, 
    get_featured_content,
    get_content_by_id
)

api_bp = Blueprint('api', __name__)

@api_bp.route('/streaming-services', methods=['GET'])
def streaming_services():
    services = get_streaming_services()
    return jsonify(services)

@api_bp.route('/games', methods=['GET'])
def games():
    games_data = get_games()
    return jsonify(games_data)

@api_bp.route('/featured', methods=['GET'])
def featured():
    featured_content = get_featured_content()
    return jsonify(featured_content)

@api_bp.route('/streaming-services/<id>', methods=['GET'])
def get_streaming_service(id):
    service = get_content_by_id('streaming-services', id)
    return jsonify(service)

@api_bp.route('/games/<id>', methods=['GET'])
def get_game(id):
    game = get_content_by_id('games', id)
    return jsonify(game)