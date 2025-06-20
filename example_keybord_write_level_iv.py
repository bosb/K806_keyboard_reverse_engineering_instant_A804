import hid

VENDOR_ID = 0x30fa
PRODUCT_ID = 0x1340

# available devices on usb
devices = hid.enumerate()
print(devices)

# 8-key keyboard
device = hid.Device(VENDOR_ID, PRODUCT_ID)
print(device.product)

#session frame calls adden?

# set hidden level IV key type
a0=b'\x40'
a1=b'\x48'
b=b'\x00'
c=b'\x00'
v=b'\x0e'# key type: single key
print(device.write(b'\x07\x18\x03\x00'+a0+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x01'+a0+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x02'+a0+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x03'+a0+c+b'\x39'+b'\x07')) #key 8 switch to level II; also tried 19.. does not work :-(
print(device.write(b'\x07\x18\x03\x04'+a0+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x05'+a0+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x06'+a0+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x07'+a0+c+v+b'\x07'))

print(device.write(b'\x07\x18\x09\x00'+a0+c+b'\x00\x07'))
print(device.write(b'\x07\x18\x00\x00'+a0+c+b'\x00\x00'))

print(device.write(b'\x07\x18\x03\x00'+a1+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x01'+a1+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x02'+a1+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x03'+a1+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x04'+a1+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x05'+a1+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x06'+a1+c+v+b'\x07'))
print(device.write(b'\x07\x18\x03\x07'+a1+c+v+b'\x07'))

print(device.write(b'\x07\x18\x09\x00'+a1+c+b'\x00\x07'))
print(device.write(b'\x07\x18\x00\x00'+a1+c+b'\x00\x00'))

# key definitions for level IV
a=0x20
b=8
c=b'\x01'
v=3# 04-27 start value:04:a 05:b 06:c 07:d .... HID values
x=6 # 0-9 which byte to start with out of 8 to write the first ot of 10 bytes per key
for i in range(0,12): # 9 keys: 90 bytes / 8 bytes per 'adress' = 11.25
    for j in range(0,8): # 8 bytes
        value=0
        if v==7: # this would be key 8, which should switch to level II
            value=0
        else:
            if x==0: # x first index of 10 bytes key definition
                value=3
            elif x==1: # second index of 10 bytes...
                value=1
            elif x==2: # third index gets the HID value
                value=v
            else:
                value=0
        x+=1
        print (device.write(b'\x07\x18\x03'+j.to_bytes(1, 'big')+(a+b).to_bytes(1, 'big')+c+value.to_bytes(1, 'big')+b'\x07'))
        if x>=10:
            v+=1 # next HID key value
            x=0 # start new 10 bytes key definition sequence
    # write bytes to adress
    print(device.write(b'\x07\x18\x09\x00'+(a+b).to_bytes(1, 'big')+c+b'\x00\x07'))
    print(device.write(b'\x07\x18\x00\x00'+(a+b).to_bytes(1, 'big')+c+b'\x00\x00'))
    print('----- '+str(a)+' '+str(b))
    if b==8: # switch b level adress 0/1
        b=0
        a+=0x10 # next adress part of a
    else:
        b=8

# modify my existing key definition level I to add the switch to level IV
print(device.write(b'\x07\x18\x03\x00\x08\x00\x35\x07'))
print(device.write(b'\x07\x18\x03\x01\x08\x00\x2d\x07'))
print(device.write(b'\x07\x18\x03\x02\x08\x00\x2d\x07'))
print(device.write(b'\x07\x18\x03\x03\x08\x00\x38\x07')) # was 39 level II; gets 38 level IV; key 8
print(device.write(b'\x07\x18\x03\x04\x08\x00\x2d\x07'))
print(device.write(b'\x07\x18\x03\x05\x08\x00\x2d\x07'))
print(device.write(b'\x07\x18\x03\x06\x08\x00\x2d\x07')) 
print(device.write(b'\x07\x18\x03\x07\x08\x00\x00\x07'))

print(device.write(b'\x07\x18\x09\x00\x08\x00\x00\x07'))
print(device.write(b'\x07\x18\x00\x00\x08\x00\x00\x00'))

