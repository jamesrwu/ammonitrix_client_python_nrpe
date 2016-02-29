#!/usr/bin/env python

from ammonitrixclient.client import *
from ammonitrixclient.nrpe import *


client = Client(name='clienttest.testname')

client.set_server(server_hostname='localhost', protocol='http')

# This is a fake nrpe.d folder that sends simulated test results
# for testing
nrpe = Nrpe('nrpe.d/')
#nrpe = Nrpe('/etc/nagios/nrpe.d')
results = nrpe.execute_commands()

for check, result in results.iteritems():
    name="clienttest.{}".format(check)
    client.set_name(name)
    client.set_tags(['foo', 'bar', 1])
    client.set_check_data(result)
    client.send_result()
    print "sent {}".format(name)
