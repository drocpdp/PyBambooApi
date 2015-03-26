from bamboo_api_client import BambooApiClient
import json

class OpenxBuilds(object):
    
    def __init__(self):
        self.bamboo = BambooApiClient()
    
    def get_all_plans(self):
        all_plans = []
        plan = {}
        plans = self.bamboo.get_all_plans()
        for p in plans['plans']['plan']:
            if p['enabled'] == True:
                latest_version = self.get_latest_version(p['key'])
                if latest_version:
                    plan['key'] = p['key']                    
                    plan['result_key'] = latest_version[0]
                    plan['build_number'] = latest_version[1]
                    all_plans.append(plan)
                    plan = {}
        return all_plans
                
    
    def get_latest_version(self, key):
        results = self.bamboo.get_result(key)
        for r in results['results']['result']:
            if r['state'] == 'Successful':
                return [r['buildResultKey'], r['buildNumber']]
    
    def _print_json(self, j):
        return json.dumps(j, sort_keys=True,indent=4, separators=(',', ': '))
        
    def main(self):
        print (self._print_json(self.get_all_plans()))
            
if __name__=="__main__":
    OpenxBuilds().main()