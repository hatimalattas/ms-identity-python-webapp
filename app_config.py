import os

# Application (client) ID of app registration
# CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_ID = os.environ.get("CLIENT_ID_TAH_APP")

# Application (client) Secret
CLIENT_SECRET = os.environ.get("CLIENT_SECRET_TAH_APP")

SECRET_KEY = "123"

if not CLIENT_SECRET:
    raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = os.environ.get("AUTHORITY")

# Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

REDIRECT_PATH = "/callback"

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/me'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
# SCOPE = ["User.Read"]
SCOPE = [os.environ.get("SCOPE_TAH_APP"), "User.Read"]

# Specifies the token cache should be stored in server-side session
SESSION_TYPE = "filesystem"

DEBUG = True