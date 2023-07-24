import urllib.parse
from urllib.request import urlopen
from xmltodict import parse

class UMDCASClient(object):
    '''
    A python client to access the University of Maryland Central Authentication Services (CAS) remote instance.

    >>> from umd_python_cas import UMDCASClient
    '''

    def __init__(self, host_name=None, post_auth_route=None) -> None:
        if host_name is None or post_auth_route is None:
            raise ValueError("host_name or post_auth_route is None")

        self.host_name = host_name
        self.post_auth_redirect_route = post_auth_route

    def get_login_cas_url(self):   
        return 'https://shib.idm.umd.edu/shibboleth-idp/profile/cas/login?service=' + urllib.parse.quote_plus(self.host_name + self.post_auth_redirect_route)

    def get_logout_cas_url(self):
        return 'https://shib.idm.umd.edu/shibboleth-idp/profile/cas/logout'
    
    def validate_ticket(self, req):
        xml_dict = {}

        try: 
            if (ticket := getattr(req, 'args', getattr(req, 'GET', {'ticket': req})).get('ticket')) is None:
                raise ValueError("ticket is None can't validate user")
            
            cas_validate_url = 'https://shib.idm.umd.edu/shibboleth-idp/profile/cas/serviceValidate?service=' \
                + urllib.parse.quote_plus(self.host_name + self.post_auth_redirect_route) + '&ticket=' + str(ticket)
            xml_dict = parse(urlopen(cas_validate_url).read().strip().decode('utf8', 'ignore'))
            return xml_dict["cas:serviceResponse"]["cas:authenticationSuccess"]["cas:user"]
            
        except Exception as err:
            raise Exception("incorrect or empty xml: " + str(err))
