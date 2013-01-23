from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.web import server, http, static
from twisted.python import log
from twisted.internet import defer, utils

###################################
#### Root and utility resources ###
###################################

class RootResource(Resource):
    def __init__(self):
        Resource.__init__(self)
        
        # the resource that returns JSON
        self.putChild('hello', HelloResource())
        
        # statically serve the file on the same server
        self.putChild('webpage', File('webpage.html'))        
        
        
class HelloResource(Resource):
    def __init__(self):
        Resource.__init__(self)
        
    def render_GET(self, request):
        print "serving up the json now"
        
        # these are the CROSS-ORIGIN RESOURCE SHARING headers required
        # learned from here: http://msoulier.wordpress.com/2010/06/05/cross-origin-requests-in-twisted/
        request.setHeader('Access-Control-Allow-Origin', '*')
        request.setHeader('Access-Control-Allow-Methods', 'GET')
        request.setHeader('Access-Control-Allow-Headers', 'x-prototype-version,x-requested-with')
        request.setHeader('Access-Control-Max-Age', 2520) # 42 hours
        
        # normal JSON header
        request.setHeader('Content-type', 'application/json')
        request.write('{"cats": "meow"}') # gotta use double-quotes in JSON apparently 
        request.finish()
        
        # return this even though the request really is finished by now
        return server.NOT_DONE_YET
        
        
##########################
#### Main! ###############
#### Go, little server! ##
##########################

if __name__ == "__main__":
    from twisted.internet import reactor  
    from sys import stdout
    import sys
        
    log.startLogging(stdout)
    
    reactor.listenTCP(8080,server.Site(RootResource()))

    log.msg("running...")
    reactor.run()
