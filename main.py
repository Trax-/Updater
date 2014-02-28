__author__ = 'tlo'

import router
import server

router2 = router.Routers(u"router2.ocsnet.com", u"zJntFuxn3d8C#qKS")
router3 = router.Routers(u"router3.ocsnet.com")
router5 = router.Routers(u"router5.ocsnet.com", u"4ceful")

ns2 = server.Server(u"ns2.ocsnet.com", u"10928350")
ns3 = server.Server(u"ns3.ocsnet.com", u"10928352")
ns5 = server.Server(u"ns5.ocsnet.com", u"10928354")
ocsnet2 = server.Server("@", "10928312")
ocsnet3 = server.Server("@", "10928310")
ocsnet5 = server.Server("@", "10928314")

router2_address = router2.ip_address
ns2_address = ns2.ip_address
router3_address = router3.ip_address
ns3_address = ns3.ip_address
router5_address = router5.ip_address
ns5_address = ns5.ip_address
flag = False

if ns2_address != router2_address:
    ns2.ip_address = router2_address
    ocsnet2.ip_address = router2_address
    print("router 2 changed to: " + router2_address)
    flag = True

if ns3_address != router3_address:
    ns3.ip_address = router3_address
    ocsnet3.ip_address = router3_address
    print("router 3 changed to: " + router3_address)
    flag = True

if ns5_address != router5_address:
    ns5.ip_address = router5_address
    ocsnet5.ip_address = router5_address
    print("router 5 changed to: " + router5_address)
    flag = True

if flag:
    print("routers updated as above")
else:
    print("routers up to date no changes needed")
