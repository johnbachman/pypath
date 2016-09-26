#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
#  Copyright (c) 2014-2015 - EMBL-EBI
#
#  File author(s): Dénes Türei (denes@ebi.ac.uk)
#
#  This code is not for public use.
#  Please do not redistribute.
#  For permission please contact me.
#
#  Website: http://www.ebi.ac.uk/~denes
#

import pypath
from pypath import chembl
from pypath.common import *
from pypath.data_formats import *
from pypath import server

net = pypath.Pypath(ncbi_tax_id = 9606, loops = True)
net = pypath.Pypath(ncbi_tax_id = 9606)


net.init_network()
net.init_network(pfile = 'cache/default_network_wo-intact_ltp-only.pickle')

net.load_resources(lst={'li2012': ugly['li2012']})
net.load_resources(lst={'acsn': ugly['acsn']})
net.load_resources(lst={'mimp': good['mimp']})
net.load_resources(lst={'pnetworks': good['pnetworks']})
net.load_resources(lst={'psite_noref': good['psite_noref']})
net.save_network(pfile = 'cache/default_plus_acsn_phospho.pickle')
net.init_network(pfile = 'cache/default_plus_acsn_phospho.pickle')

net.kegg_directions()

net.load_ptms()
# net.load_phospho_dmi('Li2012', trace = True)

#from pypath.data_formats import best
#net.read_data_file(best['hprd'], keep_raw = True)
# net.load_resources(lst = {'signor': best['signor']})

#tr = net.load_hprd_ptms(trace = True)
#len(tr['kinase_ambiguousity'])
#len([x for x in tr['kinase_ambiguousity'].values() if len(x) == 0])
#len([x for x in tr['kinase_ambiguousity'].values() if len(x) != 0])
#len(tr['substrate_ambiguousity'])
#len([x for x in tr['substrate_ambiguousity'].values() if len(x) == 0])
#len([x for x in tr['substrate_ambiguousity'].values() if len(x) != 0])
#from pypath import dataio
#import igraph
#h = dataio.get_hprd_ptms()
#hh = dataio.get_hprd_ptms()
#[net.mapper.map_name(h[i]['substrate_refseqp'].split('.')[0], 'refseqp', 'uniprot') for i in xrange(len(h))]
#[net.mapper.map_name(hi[3].split('.')[0], 'refseqp', 'uniprot') for hi in hh]
#net.load_resources(lst={'mimp': good['mimp']})
#net.load_resources(lst={'pnetworks': good['pnetworks']})
#net.load_resources(lst={'psite_noref': good['psite_noref']})
#net.load_resources(lst={'acsn': ugly['acsn']})
#net.save_network(pfile = 'cache/plus_phospho.pickle')

server.Rest(net, 33333)