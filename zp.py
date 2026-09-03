import zipfile, zopfli.zlib, struct, os, sys, time
src='dist/index.html'; out='dist/game.zip'
data=open(src,'rb').read()
c=zopfli.zlib.compress(data, numiterations=1000)[2:-4]
crc=zipfile.crc32(data)&0xffffffff
name=b'index.html'
dt=(1980,1,1,0,0,0)
def dosdt():
    return (0<<5|1, ((1980-1980)<<9)|(1<<5)|1)
t,d=dosdt()
lh=struct.pack('<IHHHHHIIIHH',0x04034b50,20,0,8,t,d,crc,len(c),len(data),len(name),0)+name
cd=struct.pack('<IHHHHHHIIIHHHHHII',0x02014b50,20,20,0,8,t,d,crc,len(c),len(data),len(name),0,0,0,0,0,0)+name
eo=struct.pack('<IHHHHIIH',0x06054b50,0,0,1,1,len(cd),len(lh)+len(c),0)
open(out,'wb').write(lh+c+cd+eo)
print(os.path.getsize(out))
