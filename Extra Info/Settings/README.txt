Settings for OAuth 

Modify and put into the working directory when you want to. If you don't use this,
PyDrive automatically sets default values that should work 

These are what each function does:

client_config_backend (str):
 	From where to read client configuration(API application settings such as client_id and client_secrets) from. Valid values are ‘file’ and ‘settings’. 
		Default: ‘file’. Required: No.

client_config_file (str):
 	When client_config_backend is ‘file’, path to the file containing client configuration. 
		Default: ‘client_secrets.json’. Required: No.

client_config (dict):
 	Place holding dictionary for client configuration when client_config_backend is ‘settings’. 
		Required: Yes, only if client_config_backend is ‘settings’

client_config[‘client_id’] (str):
 	Client ID of the application. 
		Required: Yes, only if client_config_backend is ‘settings’

client_config[‘client_secret’] (str):
 	Client secret of the application. 
		Required: Yes, only if client_config_backend is ‘settings’

client_config[‘auth_uri’] (str):
 	The authorization server endpoint URI. 
		Default: ‘https://accounts.google.com/o/oauth2/auth‘. Required: No.

client_config[‘token_uri’] (str):
 	The token server endpoint URI. 
		Default: ‘https://accounts.google.com/o/oauth2/token‘. Required: No.

client_config[‘redirect_uri’] (str):
 	Redirection endpoint URI. 
		Default: ‘urn:ietf:wg:oauth:2.0:oob‘. Required: No.

client_config[‘revoke_uri’] (str):
 	Revoke endpoint URI. 
		Default: None. Required: No.

save_credentials (bool):
 	True if you want to save credentials. 
		Default: False. Required: No.

save_credentials_backend (str):
 	Backend to save credentials to. ‘file’ is the only valid value for now. 
		Default: ‘file’. Required: No.

save_credentials_file (str):
 	Destination of credentials file. 
		Required: Yes, only if save_credentials_backend is ‘file’.

get_refresh_token (bool):
 	True if you want to retrieve refresh token along with access token. 
		Default: False. Required: No.

oauth_scope (list of str):
 	OAuth scope to authenticate. 
		Default: [‘https://www.googleapis.com/auth/drive‘]. Required: No.