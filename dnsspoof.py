from dnslib.server import DNSServer, BaseResolver
from dnslib import RR, QTYPE, A

class Resolver(BaseResolver):
    def resolve(self, request, handler):
        reply = request.reply()
        qname = str(request.q.qname)

        print("DNS Request Received:", qname)

        if "google.com" in qname:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("192.168.1.100"), ttl=60))
        elif "youtube.com" in qname:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("192.168.1.101"), ttl=60))
        else:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("8.8.8.8"), ttl=60))

        return reply

resolver = Resolver()
server = DNSServer(resolver, port=53, address="0.0.0.0")
print(" DNS Server Running...\n")
server.start()
