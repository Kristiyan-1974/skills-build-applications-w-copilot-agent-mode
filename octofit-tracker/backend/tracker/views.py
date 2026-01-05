from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    """Root API endpoint returning available top-level routes."""
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'routes': {
            'users': '/api/users/',
            'activities': '/api/activities/',
        }
    })
