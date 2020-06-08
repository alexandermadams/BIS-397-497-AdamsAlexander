# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:01:26 2020

@author: alexa
"""

from operator import itemgetter

invoices = [(83,'Electric Sander',7,57.98),
            (24,'Power Saw',18,99.99),
            (7,'Sledge Hammer',11,21.50),
            (77,'Hammer',76,11.99),
            (39,'Jig Saw',3,79.50)]


#b
byprice = sorted(invoices,key=itemgetter(2))
byprice

#c
d_q = [(item[1],item[2]) for item in invoices]
d_q_byquantity = sorted(d_q,key=itemgetter(1))
d_q_byquantity

#d
d_v = [(item[1],item[2]*item[3]) for item in invoices]
d_v_byval = sorted(d_v,key=itemgetter(1))
d_v_byval

#e
d_v_rang = list(filter(lambda x: x[1]>=200 and x[1]<=500,d_v_byval))
    
#f
runsum = 0
for i in range(len(d_v)):
    runsum = runsum+d_v[i][1]

runsum
    

