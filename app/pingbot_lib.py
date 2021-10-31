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
    
    def split_up_list(self,input_list):
        pass
    
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
        try:
            pinghost = os.system("ping -c 1 " + str(ip))
        except Exception as e:
            logging.error('Could not ping the host %s.'%ip)
            raise e
        
        if pinghost == 0:
            return True
        else:
            #return True and the round trip time
            return False

class Prometheus():
    
    def __init__(self):
        logging.info("Starting Prometheus scrape endpoint")
    
    
    def start_server(self,host):
        start_http_server(9002)
        self.total_success = Counter('pingbot_success_%s'%(host),'Successful ping')
        self.total_fail = Counter('pingbot_fail_%s'%(host),'Failure ping')
        self.ping = Guage('ping_%s'%(host),'Ping host %s'%(host))
    
    def start_server(self):
        start_http_server(9002)
        self.used_mem = Gauge('speedbot_used_memory', 'Speedbot Used Memory')
        self.free_mem = Gauge('speedbot_free_memory', 'Speedbot Free Memory')
        self.upload_speed = Gauge('speedbot_upload_in_Mbps', 'Upload speed in Mbps')
        self.download_speed = Gauge('speedbot_download_in_Mbps', 'Download speed in Mbps')
        self.packetloss = Gauge('speedbot_packetloss', 'Packet loss')
        self.jitter = Gauge('speedbot_jitter', 'jitter')
    
    def network_spec(self,input_dict):
        """
        DESC: Emit the used and free memory
        INPUT: input_dict - packetloss
                          - jitter
        OUTPUT: None
        NOTE: This is a Gauge
        """
        try:
            logging.info("Emitting network packetloss.")
            self.packetloss.set(input_dict['packetloss'])
        except Exception as e:
            logging.error(e)
            logging.error("Could not emit the network packetloss.")
            
        try:
            logging.info("Emitting network jitter.")
            self.jitter.set(input_dict['jitter'])
        except Exception as e:
            logging.error(e)
            logging.error("Could not emit the network jitter.")
        
        
    def memory(self,input_dict):
        """
        DESC: Emit the used and free memory
        INPUT: input_dict - free
                          - used
        OUTPUT: None
        NOTE: This is a Gauge
        """
        try:
            logging.info("Emitting the used memory.")
            self.used_mem.set(input_dict['used'])
        except Exception as e:
            logging.warn(e)
            logging.warn("Could not gauge used memory.")
        
        try:
            logging.info("Emitting the free memory.")
            self.free_mem.set(input_dict['free'])
        except Exception as e:
            logging.warn(e)
            logging.warn("Could not gauge free memory.")
        
    def network_speed(self,input_dict):
        """
        DESC: Emit the upload and download speed measured by the speedbot.
        INPUT: input_dict - upload
                          - download
        OUTPUT: None
        NOTE: This is a Gauge
        """
        try:
            logging.info("Emitting upload speed.")
            self.upload_speed.set(input_dict['upload'])
        except Exception as e:
            logging.warn(e)
            logging.warn("Could not gauge upload speed.")
        
        try:
            logging.info("Emitting download speed.")
            self.download_speed.set(input_dict['download'])
        except Exception as e:
            logging.warn(e)
            logging.warn("Could not gauge download speed.")
    
    