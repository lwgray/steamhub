import requests
from flask import current_app
import json

def get_strapi_headers():
    token = current_app.config['STRAPI_API_TOKEN']
    headers = {
        'Content-Type': 'application/json'
    }
    
    if token:
        headers['Authorization'] = f'Bearer {token}'
        
    return headers

def get_streaming_services():
    """
    Fetch streaming services from Strapi
    """
    url = f"{current_app.config['STRAPI_URL']}/api/streaming-services?populate=*"
    
    try:
        response = requests.get(url, headers=get_strapi_headers())
        response.raise_for_status()
        
        data = response.json()
        return data.get('data', [])
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Error fetching streaming services: {e}")
        return []

def get_games():
    """
    Fetch games from Strapi
    """
    url = f"{current_app.config['STRAPI_URL']}/api/games?populate=*"
    
    try:
        response = requests.get(url, headers=get_strapi_headers())
        response.raise_for_status()
        
        data = response.json()
        return data.get('data', [])
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Error fetching games: {e}")
        return []

def get_featured_content():
    """
    Fetch featured content from Strapi
    """
    url = f"{current_app.config['STRAPI_URL']}/api/featured-contents?populate=*"
    
    try:
        response = requests.get(url, headers=get_strapi_headers())
        response.raise_for_status()
        
        data = response.json()
        return data.get('data', [])
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Error fetching featured content: {e}")
        return []

def get_content_by_id(content_type, id):
    """
    Fetch specific content by ID
    """
    url = f"{current_app.config['STRAPI_URL']}/api/{content_type}/{id}?populate=*"
    
    try:
        response = requests.get(url, headers=get_strapi_headers())
        response.raise_for_status()
        
        data = response.json()
        return data.get('data', {})
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Error fetching {content_type} with ID {id}: {e}")
        return {}