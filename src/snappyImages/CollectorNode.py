from utils.binhex import hexValues3

@setHook(HOOK_STARTUP)
def startup():
    mcastRpc(1,2,"imAlive")
    print "imAlive"

def sendAck(addr, command, result):
    rpc(addr, "ack", command, result)
    print "ack:" + addr_as_text() + "(" + command + ", " + result + ")"

def echo(this):
    addr = rpcSourceAddr()
    sendAck(addr, "echo", this)
    print "echoing: " + this

def announceHub():
    command = "announceHub"
    addr = rpcSourceAddr()
    print command + ": " + addr_as_text(addr)
    sendAck(addr, "announceHub", "-")

def addr_as_text(addr):
    return hexValues3(ord(addr[0]), ord(addr[1]), ord(addr[2]))
