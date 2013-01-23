Cross-origin resource sharing example!

I keep making web servers that do fun stuff, and then hosting websites that want to talk to those servers with ajax and json, but the websites and the json-serving servers are often not hosted in the same place. 

The twisted web server will be over on http://mymagicalmachine.com:8080 and then the website is hosted on http://websitehostingfuntimes.com. 

If you try to use ajax to have the webhostingfuntimes.com webpage talk to the mymagicalmachine.com:8080 server, there will be an error that if you examine says:

    XMLHttpRequest cannot load http://mymagicamachine.com:8080/gimmejson. Origin null is not allowed by Access-Control-Allow-Origin.

What you need is for the mymagicalmachine server to set some headers that make things okay. Here's the sneak peek:

    # these are the CROSS-ORIGIN RESOURCE SHARING headers required
    # learned from here: http://msoulier.wordpress.com/2010/06/05/cross-origin-requests-in-twisted/
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Methods', 'GET')
    request.setHeader('Access-Control-Allow-Headers', 'x-prototype-version,x-requested-with')
    request.setHeader('Access-Control-Max-Age', 2520) # 42 hours

The code includes 
- twisted web server that serves up the json with the headers        
    - also serves up a static webpage, so if you remove the headers, you can see that it works if it's all on the same domain
- webpage with some javascript that tries to get json from the webserver
- some pictures of stuff in action 
