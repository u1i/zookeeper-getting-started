from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

print zk.get_children("/")

try:
        zk.add_auth("digest", "jamesbond:password123")
        print zk.get("/area51")
except: 
        print "Auth error"

zk.stop()
