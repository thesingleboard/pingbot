import os
import logging
import settings
from pingbot_lib import Operations as op
from pingbot_lib import Prometheus as prom


def ping_host():
    pass

def main:
    #make sure the git repo has not already been cloned
    if not os.path.exists(settings.CONFIG['GITROOT'])
        raise Exception("No gitroot directory present")
        
    #get the directory
    if settings.CONFIG['CLONE_REPO']:
        try:
            logging.info('Cloneing the git repo %s'%(settings.CONFIG['GITURL']))
            op.gitclone()
        except Exception as e:
            logging.error('Could not clone the repo %s.'%(settings.CONFIG['GITURL']))
            logging.error(e)

    #read in the hosts file
    try:
        #open the hosts file and read it.
        hosts_file = settings.CONFIG['GITROOT']+'/'+IPFILE
        out = op.read_hosts_file(hosts_file)
    except Exception as e:
        logging.error("Could not read the hosts file.")
        logging.error(e)
    
    try:
        split_list = op.split_up_list(out)
    except Exception as e:
        logging.error("Could not split up the ip list.")
        logging.error(e)
    
    
    

if __name__ == '__main__':
    main()