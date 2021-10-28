import os
import logging
import settings
from pingbot_lib import Network
from pingbot_lib import Prometheus


def main:
    #make sure the git repo has not already been cloned
    if not os.path.exists(settings.CONFIG['GITROOT'])
        raise Exception("No gitroot directory present")
        
    #get the directory
    try:
        logging.info('Cloneing the git repo %s'%(settings.CONFIG['GITURL']))
        Network.gitclone()
    except Exception as e:
        logging.error('Could not clone the repo %s.'%(settings.CONFIG['GITURL']))
        logging.error(e)

    #read in the hosts file
    try:
        #open the hosts file and read it.
        hosts_file = settings.CONFIG['GITROOT']+'/'+IPFILE
        out = Network.read_hosts_file(hosts_file)
    except Exception as e:
        logging.error("Could not read the hosts file.")
        logging.error(e)
    
    #ping the hosts
    try:
        
    

if __name__ == '__main__':
    main()