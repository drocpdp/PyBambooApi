import sys, json, requests, base64
from config import config
from jira.resources import Project

class BambooApiClient(object):
    
    #--- """Utilities"""
    
    def _bamboo_http(self, full_url, method):
        if method == 'GET':
            response = requests.get(full_url, headers=self._get_headers())
        return json.loads(response.text)
    
    def _bamboo_GET(self, resource, query=None):
        full_url = self._form_http(resource, query)
        return self._bamboo_http(full_url, 'GET')
    
    def _form_http(self, tail_url, query=None):
        """
        Formatting and formation of url. Mostly string manips.
        """
        tail_url = tail_url + '.json'
        if query:
            full_url = self._get_bamboo_url() + tail_url + "?" + query
            print full_url
        else:
            full_url = self._get_bamboo_url() + tail_url
        return full_url
    
    #--- """Configs"""
    
    def _get_bamboo_url(self):
        return config['bamboo_url']
    
    def _get_content_type(self):
        return config['content_type']
    
    def _get_headers(self):
        return config['headers']
    
    def _get_username(self):
        return config['username']
    
    def _get_password(self):
        return config['password']
    
    #--- """API Resources"""
    
    def _GET_plans(self, query=None):
        resource = 'plan'
        return self._bamboo_GET(resource, query)
    
    def _GET_plan(self, plan, query=None):
        resource = 'plan/%s' % project
        return self._bamboo_GET(resource, query)
    
    def _GET_projects(self, query=None):
        resource = 'project'
        return self._bamboo_GET(resource, query)
    
    def _GET_project(self, project, query=None):
        resource = 'project/%s' % project
        return self._bamboo_GET(resource, query)
    
    def _GET_result(self, project=None, query=None):
        if project:
            resource = 'result/%s' % project
        else:
            resource = 'result'
        return self._bamboo_GET(resource, query)
    
    #--- """Methods"""
    
    def get_all_plans(self, max_result=5000):
        return self._GET_plans(query='max-result=%s' % max_result)
    
    def get_plan(self, plan, query=None):
        return self._GET_plan(plan, query)
    
    def get_all_projects(self, max_result=5000):
        return self._GET_projects(query='max=result=%s' % max_result)
    
    def get_project(self, project, query=None):
        return self._GET_project(project, query)
    
    def get_result(self, plan=None, query=None):
        return self._GET_result(plan, query)
    
    #--- """Main (Test)"""
    
    def main(self):
        print (self.get_all_plans())

        
if __name__=="__main__":
    BambooApiClient().main()
        