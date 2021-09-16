# umd-python-cas
## Getting Started
To get started, follow the instructions on one of our demo repos, either [Flask](https://github.com/umd-python-cas/flask-demo) or [Django](https://github.com/umd-python-cas/django-demo). Those examples will help you get started with umd-python-cas in a web app environment. The rest of this readme has extra information.
## Install
```bash
pip install umd-python-cas
```
## Example Use
```python
from umd_python_cas import UMDCASClient

client = UMDCASClient(host_name="http://127.0.0.1:5000", post_auth_route="/secure")
```
## Install from Source
Installing from source is not necessary, but in case you want to do it, here's how. First, clone the repository, and navigate into the directory:
```bash
git clone https://github.com/umd-python-cas/umd-python-cas.git
cd umd-python-cas
```
Then, if you want to build a specific version, check out that version's tag. Find the list of tags [here](https://github.com/umd-python-cas/umd-python-cas/tags). If you want to build the latest commit, skip this step.
```bash
git checkout vX.X.X
```
Finally, install the package using pip
```
pip install .
```
## How It Works
### UMDCASClient class
`umd-python-cas` contains a single class, called `UMDCASClient`. This class manages the authentication to the UMD CAS servers. To create an instance of the class, you use the constructor, passing in both a `hostname` and a `post_auth_route`:
```python
from umd_python_cas import UMDCASClient

client = UMDCASClient(host_name="http://127.0.0.1:5000", post_auth_route="/secure")
```
The `hostname` tells the client what the base URL of your web sever is. For development, this is something like `127.0.0.1:5000` or `localhost:5000` as shown. For a production app, this could be something like `myapp.com`.

The `post_auth_route` tells the client where to return to after the user logs in. This depends on how you set up your web server, see the Flask and Django demos at the beginning of this repo for examples.
### get_login_cas_url
This returns the URL on the UMD CAS server that you can redirect to in order to log the user in. It contains an encoded version of the location to return to so that the CAS servers know how to redirect the user back after logging in. You should set up a route on your app for something like `/login` to return a redirect to this URL, as shown in the Flask and Django demos.
### get_logout_cas_url
This returns the URL on the UMD CAS server that you can redirect to in order to to log the user out. Map this to a route such as `/logout` just like the previous.
### validate_ticket
When the user has redirected back from the UMD CAS servers after logging in, they will return to your server (at the URL defined by `post_auth_route`) with a ticket. Pass the ticket to `validate_ticket` to verify that the user logged in correctly, in which case it will return the user's username. Store this in a session variable in your app, to keep track that the user is logged in and give access to the app.
## Authors
 * Jacob (Coby) Winfield
 * Johan Vandegriff
## Credits
 * Daniel Laurence
 * Jim Purtilo
 * Ronel Aguilar
## References
 * [python-cas](https://github.com/python-cas/python-cas)
