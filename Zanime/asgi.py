"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from anime.routing import ws_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Zanime.settings") #  your_project_name.settings

application = ProtocolTypeRouter({
	'http': get_asgi_application(),
	'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
	})