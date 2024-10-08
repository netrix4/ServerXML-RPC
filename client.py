import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
results = []
count = 0

results.append( ["addition", proxy.add(5, 5)] )
results.append( ["substraction", proxy.sub(5, 5)] )
results.append( ["multiplication", proxy.mult(5, 5)] )
results.append( ["division", proxy.div()] )
results.append( ["exponitiation", proxy.exp(5, 5)] )

for i in results:
    count+=1
    print("Result of the " + i[0]  +" is:", i[1])
    
