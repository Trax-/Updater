__author__ = 'tlo'

import re
import requests
import json


class Server(object):
    def __init__(self, name: str=None,
                 dns_host_id: str=None):
        """

        :type self: basestring
        """
        self.name = name
        self.dns_host_id = dns_host_id
        self.api_key = u"AAb619912c519ef1786a6372f6e1ed77c5"
        self.api_password = u"8a3786d1b9504086e8e3573642489c8caae03b3a"
        self.url = u"https://api.dnspark.com/v2/dns/"

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.getter
    def ip_address(self):
        http_request = requests.get(self.url + self.dns_host_id,
                                    auth=(self.api_key, self.api_password))
        return http_request.json()['records'][0]['rdata']

    @ip_address.setter
    def ip_address(self, new_ip_address):
        headers = {'content-type': 'application/json'}
        payload = {"rname": self.name,
                   "rtype": "A",
                   "ttl": "60",
                   "rdata": new_ip_address,
                   "dynamic": "Y"}

        http_put = requests.put(self.url + self.dns_host_id,
                                data=json.dumps(payload),
                                headers=headers,
                                auth=(self.api_key, self.api_password))
        print(http_put.json()['message'])
