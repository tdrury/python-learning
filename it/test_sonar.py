import unittest
import os
import requests
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning


class SonarITestCase(unittest.TestCase):

    def setUp(self):
        self.host = os.environ['sonar_host']
        self.auth_token = os.environ['sonar_auth_token']
        # Suppress only the single warning from urllib3 needed.
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    def test_types(self):

        project_key = 'com.sap.dm.dme:dme.integration.ms.parent:rc'
        path = '/sonar/api/qualitygates/project_status'
        auth = HTTPBasicAuth(self.auth_token, "")

        params = {'projectKey': project_key}

        r = requests.get(self.host+path, params=params, auth=auth, verify=False)
        print('url='+r.url)
        json = r.json()
        print('response='+str(json))

        self.assertEqual(200, r.status_code)
        self.assertEqual('OK', json['projectStatus']['status'])


if __name__ == '__main__':
    unittest.main()
