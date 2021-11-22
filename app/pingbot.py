import os
import logging
import settings
import time
import multiprocessing

from pingbot_lib import Operations as op
from pingbot_lib import Prometheus as prom

#Instantiate prom
pr = prom()
o = op()

def pinghost(input_list):
    for host in input_list:
        success = o.ping(host['ip'])
        if success:
            print('abbadoo %s'%host['ip'])
            pr.current_ping({'hostname':host['hostname'],'ip':host['ip'],'status':True})
        else:
            print('boob %s'%host['ip'])
            pr.current_ping({'hostname':host['hostname'],'ip':host['ip'],'status':False})
            

def main():

    pr.start_server()

    #make sure the git repo has not already been cloned
    if not os.path.exists(settings.CONFIG['GITROOT']):
        logging.warn("No gitroot directory present")

        #get the directory
        if settings.CONFIG['CLONEREPO']:
            try:
                logging.info('Cloneing the git repo %s'%(settings.CONFIG['GITURL']))
                o.git_clone()
            except Exception as e:
                logging.error('Could not clone the repo %s.'%(settings.CONFIG['GITURL']))
                logging.error(e)

    while True:
        #read in the hosts file
        try:
            #open the hosts file and read it.
            hosts_file = settings.CONFIG['GITROOT'] + settings.CONFIG['HOSTS']
            out = o.read_hosts_file(hosts_file)
        except Exception as e:
            logging.error("Could not read the hosts file.")
            logging.error(e)

        try:
            split_list = o.split_up_list(out)
        except Exception as e:
            logging.error("Could not split up the ip list.")
            logging.error(e)

        for chunk in split_list:
            pinghost(chunk)

        """
        try:
            process = [multiprocessing.Process(target=pinghost, args=(chunk,)) for chunk in split_list]

            for p in process:
                p.start()

            for p in process:
                p.join()
                p.terminate()

        except Exception as e:
            logging.error("Could not process the chunk of hosts.")
            logging.error(e)
        """
        time.sleep(settings.CONFIG['INTERVAL'])

if __name__ == '__main__':
    main()