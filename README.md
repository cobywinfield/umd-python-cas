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
## Credits
 * Daniel Laurence
 * Jim Purtilo
 * Ronel Aguilar
## References
 * [python-cas](https://github.com/python-cas/python-cas)
