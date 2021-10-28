import os
import logging
import re
from git import Repo
from pythonping import ping
from prometheus_client import start_http_server
from prometheus_client import Gauge
from prometheus_client import Counter

class Operations():
    
    def __init__(self):
        pass
    
    def git_clone(self,input_dict):
        try:
            Repo.clone_from(settings.CONFIG['GITURL'], settings.CONFIG['GITROOT'], recursive=True)
        except Exception as e:
            logging.error(e)
            raise e
    
    def read_hosts_file(self,host_file):
        """
        DESC: return a list of ip and hostname dictionaries from a unix style hosts file.
        INPUT: host_file - fully qualified path to file
        OUTPUT: out_list of dict - ip
                                 - hostname
        NOTE: Get rid of the cruft in the file
        """
        comment = "#+"
        local = 'localhost+'
        colon = '^:+'
        valid_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        out = []
        try:
            file = open(host_file,'r')
            for line in file.readlines():
                if(re.search(comment,line) or re.search(local,line) or re.search(colon,line)):
                    continue
                else:
                    line = line.strip().split()
                    if(re.search(valid_ip,line[0])):
                        out.append({'ip':line[0],'hostname':line[1]})
                    else:
                        out.append({'ip':line[1],'hostname':line[0]})
        except IOError as i:
            logging.error('Could not open the file %s'%host_file)
            raise i
        
        return out
    
    def ping(self,ip):
        """
        DESC: Ping the host to see if it is on the network
        INPUT: ip - ip of the target host
        OUTPUT: False or Round trip time.
        NOTE: True if 
        """
        timeout = "^Request\ timed\ out"
        try:
            pinghost = ping(ip,count=1)
        except Exception as e:
            logging.error('Could not ping the host %s.'%ip)
            raise e
        
        if re.search(timeout,pinghost):
            return {'bool':False,'trip':0}
        else:
            #return True and the round trip time
            return {'bool':True,'trip':pinghost.rtt_avg_ms}

class Prometheus():
    
    def __init__(self):
        logging.info("Starting Prometheus scrape endpoint")
    
    
    def start_server(self,host):
        start_http_server(9002)
        self.total_success = Counter('pingbot_success_%s'%(host),'Successful ping')
        self.total_fail = Counter('pingbot_fail_%s'%(host),'Failure ping')
        self.ping = Guage('ping_%s'%(host),'Ping host %s'%(host))
    
    def pinghost(self,input_spec):
        pass
    
    