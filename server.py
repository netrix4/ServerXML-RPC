from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(a, b):
    return a + b
def sub_numbers(a, b):
    return a - b
def mult_numbers(a, b):
    return a * b
def div_numbers(a, b):
    return a / b
def exp_numbers(a, b):
    result = a
    for count in range(b):
        result += result * a
    return result
def get():
    return "caites en el get"

server = SimpleXMLRPCServer(('localhost', 9000))
print("Listening on port 9000...")

server.register_function(add_numbers, 'add')
server.register_function(sub_numbers, 'sub')
server.register_function(mult_numbers, 'mult')
server.register_function(div_numbers, 'div')
server.register_function(exp_numbers, 'exp')
server.register_function(get, 'get')

server.serve_forever()