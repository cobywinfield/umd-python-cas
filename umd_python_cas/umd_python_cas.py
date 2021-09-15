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
        self.umd_cas_ticket_url = 'https://shib.idm.umd.edu/shibboleth-idp/profile/cas/login?service='
        self.umd_cas_logout_url = 'https://shib.idm.umd.edu/shibboleth-idp/profile/cas/logout'
        self.umd_cas_validate_url = 'https://shib.idm.umd.edu/shibboleth-idp/profile/cas/serviceValidate?service='
        self.umd_cas_login_url = self.umd_cas_ticket_url + urllib.parse.quote_plus(self.host_name + self.post_auth_redirect_route)

    def get_login_cas_url(self):   
        return self.umd_cas_login_url

    def get_logout_cas_url(self):
        return self.umd_cas_logout_url

    
    def validate_ticket(self, req):
        ticket = getattr(req, 'args', getattr(req, 'GET', {'ticket': req})).get('ticket')

        if ticket is None:
            raise ValueError("ticket is None can't validate user")
        
        xml_dict = {}
        cas_validate_url = self.umd_cas_validate_url + urllib.parse.quote_plus(self.host_name + self.post_auth_redirect_route) + '&ticket=' + str(ticket)
        xml_dict = parse(urlopen(cas_validate_url).read().strip().decode('utf8', 'ignore'))

        try:
            return xml_dict["cas:serviceResponse"]["cas:authenticationSuccess"]["cas:user"]
        except Exception as err:
            raise Exception("incorrect or empty xml: " + str(err))
