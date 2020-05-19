import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import LegacyApplicationClient

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
client_id = 'FKaKm5a4Tgmfgn9SIpQUve2MGvTObi'
client_secret = 'cVyd7n2aTCwzINYNSwD4lvXsvd8KW9'
token_url = 'http://localhost:8069/api/authentication/oauth2/token'

username = 'admin'
password = 'admin'
scope = ['all']

oauth = OAuth2Session(
    client=LegacyApplicationClient(client_id=client_id)
)

token = oauth.fetch_token(
    token_url=token_url,
    username=username,
    password=password,
    client_id=client_id,
    client_secret=client_secret,
)

print(token)
print(oauth.put("http://localhost:8069/api/write/res.users?ids=2&{}".format(code)).json())
print(oauth.get("http://localhost:8069/api/user").json())
print(oauth.get("http://localhost:8069/api/custom/clientes").json())
print(oauth.get("http://localhost:8069/api/custom/product").json())
