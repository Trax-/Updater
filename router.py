__author__ = 'tlo'
import re

import requests


class Routers(object):
    def __init__(self, name: str=None, dns_host_id: str=None,
                 password: str=None) -> object:
        """
            :type name; str
            :type dns_host_id: str
            :type password; str

        """
        self._ipaddress = None
        self.name = name
        self.dns_host_id = dns_host_id
        self.searchpat = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

        if password is None:
            self.url = u"http://ipdetect.dnspark.com"
            self.password = None
        else:
            self.url = u"http://{0}/wancfg.cmd".format(self.name)
            self.password = password
            self.payload = {'action': 'view'}

    @property
    def ipaddress(self) -> str:
        return self.ipaddress

    @ipaddress.getter
    def ipaddress(self):
        """
            Set the routers IP address thru lookup
            :return: ipaddress
    
            """
        if self.password is None:
            httprequest = requests.get(self.url)
        else:
            httprequest = requests.get(self.url, params=self.payload, auth=('admin', self.password))
        self._ipaddress = re.search(self.searchpat, httprequest.text).group()
        return self._ipaddress
