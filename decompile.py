import sys

macro_adresses=''
k={
    #"0x00":"KEY_NONE",
    #"0x01":"KEY_ERR_OVF",
    "0x04":"KEY_A",
    "0x05":"KEY_B",
    "0x06":"KEY_C",
    "0x07":"KEY_D",
    "0x08":"KEY_E",
    "0x09":"KEY_F",
    "0x0a":"KEY_G",
    "0x0b":"KEY_H",
    "0x0c":"KEY_I",
    "0x0d":"KEY_J",
    "0x0e":"KEY_K",
    "0x0f":"KEY_L",
    "0x10":"KEY_M",
    "0x11":"KEY_N",
    "0x12":"KEY_O",
    "0x13":"KEY_P",
    "0x14":"KEY_Q",
    "0x15":"KEY_R",
    "0x16":"KEY_S",
    "0x17":"KEY_T",
    "0x18":"KEY_U",
    "0x19":"KEY_V",
    "0x1a":"KEY_W",
    "0x1b":"KEY_X",
    "0x1c":"KEY_Y",
    "0x1d":"KEY_Z", 
    "0x1e":"KEY_1",
    "0x1f":"KEY_2",
    "0x20":"KEY_3",
    "0x21":"KEY_4",
    "0x22":"KEY_5",
    "0x23":"KEY_6",
    "0x24":"KEY_7",
    "0x25":"KEY_8",
    "0x26":"KEY_9",
    "0x27":"KEY_0", 
    #"0x28":"KEY_ENTER",
    #"0x29":"KEY_ESC",
    #"0x2a":"KEY_BACKSPACE",
    #"0x2b":"KEY_TAB",
    #"0x2c":"KEY_SPACE",
    #"0x2d":"KEY_MINUS",
    #"0x2e":"KEY_EQUAL",
    #"0x2f":"KEY_LEFTBRACE",
    #"0x30":"KEY_RIGHTBRACE",
    #"0x31":"KEY_BACKSLASH",
    #"0x32":"KEY_HASHTILDE",
    #"0x33":"KEY_SEMICOLON",
    #"0x34":"KEY_APOSTROPHE",
    #"0x35":"KEY_GRAVE",
    "0x36":"KEY_COMMA",
    "0x37":"KEY_DOT",
    #"0x38":"KEY_SLASH",
    #"0x39":"KEY_CAPSLOCK", 
    "0x3a":"KEY_F1",
    "0x3b":"KEY_F2",
    "0x3c":"KEY_F3",
    "0x3d":"KEY_F4",
    "0x3e":"KEY_F5",
    "0x3f":"KEY_F6",
    "0x40":"KEY_F7",
    "0x41":"KEY_F8",
    "0x42":"KEY_F9",
    "0x43":"KEY_F10",
    "0x44":"KEY_F11",
    "0x45":"KEY_F12", 
    #"0x46":"KEY_SYSRQ",
    #"0x47":"KEY_SCROLLLOCK",
    #"0x48":"KEY_PAUSE",
    #"0x49":"KEY_INSERT",
    #"0x4a":"KEY_HOME",
    #"0x4b":"KEY_PAGEUP",
    #"0x4c":"KEY_DELETE",
    #"0x4d":"KEY_END",
    #"0x4e":"KEY_PAGEDOWN",
    #"0x4f":"KEY_RIGHT",
    #"0x50":"KEY_LEFT",
    #"0x51":"KEY_DOWN",
    #"0x52":"KEY_UP", "0x53":"KEY_NUMLOCK",
    #"0x54":"KEY_KPSLASH",
    #"0x55":"KEY_KPASTERISK",
    #"0x56":"KEY_KPMINUS",
    #"0x57":"KEY_KPPLUS",
    #"0x58":"KEY_KPENTER",
    #"0x59":"KEY_KP1",
    #"0x5a":"KEY_KP2",
    #"0x5b":"KEY_KP3",
    #"0x5c":"KEY_KP4",
    #"0x5d":"KEY_KP5",
    #"0x5e":"KEY_KP6",
    #"0x5f":"KEY_KP7",
    #"0x60":"KEY_KP8",
    #"0x61":"KEY_KP9",
    #"0x62":"KEY_KP0",
    #"0x63":"KEY_KPDOT", "0x64":"KEY_102ND",
    "0x65":"KEY_COMPOSE",
    "0x66":"KEY_POWER",
    #"0x67":"KEY_KPEQUAL", 
    "0x68":"KEY_F13",
    "0x69":"KEY_F14",
    "0x6a":"KEY_F15",
    "0x6b":"KEY_F16",
    "0x6c":"KEY_F17",
    "0x6d":"KEY_F18",
    "0x6e":"KEY_F19",
    "0x6f":"KEY_F20",
    #"0x70":"KEY_F21",
    "0x71":"KEY_F22",
    "0x72":"KEY_F23",
    "0x73":"KEY_F24", 
    #"0x74":"KEY_OPEN",
    #"0x75":"KEY_HELP",
    #"0x76":"KEY_PROPS",
    #"0x77":"KEY_FRONT",
    #"0x78":"KEY_STOP",
    #"0x79":"KEY_AGAIN",
    #"0x7a":"KEY_UNDO",
    "0x7b":"KEY_CUT",
    "0x7c":"KEY_COPY",
    "0x7d":"KEY_PASTE",
    #"0x7e":"KEY_FIND",
    #"0x7f":"KEY_MUTE",
    #"0x80":"KEY_VOLUMEUP",
    "0x81":"KEY_VOLUMEDOWN", 
    #"0x85":"KEY_KPCOMMA", "0x87":"KEY_RO",
    #"0x88":"KEY_KATAKANAHIRAGANA",
    #"0x89":"KEY_YEN",
    #"0x8a":"KEY_HENKAN",
    #"0x8b":"KEY_MUHENKAN",
    #"0x8c":"KEY_KPJPCOMMA", "0x90":"KEY_HANGEUL",
    #"0x91":"KEY_HANJA",
    #"0x92":"KEY_KATAKANA",
    #"0x93":"KEY_HIRAGANA",
    #"0x94":"KEY_ZENKAKUHANKAKU", "0xb6":"KEY_KPLEFTPAREN",
    #"0xb7":"KEY_KPRIGHTPAREN", 
    "0xe0":"KEY_LEFTCTRL",
    "0xe1":"KEY_LEFTSHIFT",
    "0xe2":"KEY_LEFTALT",
    "0xe3":"KEY_LEFTMETA",
    "0xe4":"KEY_RIGHTCTRL",
    "0xe5":"KEY_RIGHTSHIFT",
    "0xe6":"KEY_RIGHTALT",
    "0xe7":"KEY_RIGHTMETA", 
    "0xe8":"KEY_MEDIA_PLAYPAUSE",
    "0xe9":"KEY_MEDIA_STOPCD",
    "0xea":"KEY_MEDIA_PREVIOUSSONG",
    "0xeb":"KEY_MEDIA_NEXTSONG",
    "0xec":"KEY_MEDIA_EJECTCD",
    "0xed":"KEY_MEDIA_VOLUMEUP",
    "0xee":"KEY_MEDIA_VOLUMEDOWN",
    "0xef":"KEY_MEDIA_MUTE",
    #"0xf0":"KEY_MEDIA_WWW",
    #"0xf1":"KEY_MEDIA_BACK",
    #"0xf2":"KEY_MEDIA_FORWARD",
    #"0xf3":"KEY_MEDIA_STOP",
    #"0xf4":"KEY_MEDIA_FIND",
    #"0xf5":"KEY_MEDIA_SCROLLUP",
    #"0xf6":"KEY_MEDIA_SCROLLDOWN",
    #"0xf7":"KEY_MEDIA_EDIT",
    #"0xf8":"KEY_MEDIA_SLEEP",
    #"0xf9":"KEY_MEDIA_COFFEE",
    #"0xfa":"KEY_MEDIA_REFRESH",
    #"0xfb":"KEY_MEDIA_CALC",
}

print(sys.argv)

f = open(sys.argv[1], "r")
f_pcap_txt = f.read()

makro=False
keystart=100

sections = f_pcap_txt.split('0718090')
print('sections: ',len(sections))
s=0
for section in sections:
    lines = section.splitlines()
    print(str(s)+': '+str(len(lines)))
    print (lines)
    if (len(lines)>10):
        # stupid copy of below code to print adress in this case
        #0: 0 9 0/8 0 1 0007
        if (lines[0][0]=='0' and (lines[0][2]=='0' or lines[0][2]=='8' )and lines[0][3]=='0' and lines[0][5:]=='0007'):
            adress=lines[0][1]
            if (lines[0][2]=='0'):
                adress+=' 0 '
            elif (int(lines[0][2]) & 8):
            #else:
                adress+=' 1 '
            adress+=lines[0][4]
            print ('# adress: '+adress, end='; ')
        #1: 0 9 0/8 0 1 0000
        if (lines[1][0:7]=='0718000'):
            lines[1]=lines[1][7:]
        if (lines[1][0]=='0' and (lines[1][2]=='0' or lines[1][2]=='8' )and lines[1][3]=='0' and lines[1][5:]=='0000'):
            adress=lines[1][1]
            if (lines[1][2]=='0'):
                adress+=' 0 '
            elif (int(lines[1][2]) & 8):
            #else:
                adress+=' 1 '
            adress+=lines[1][4]
            print ('# adress: '+adress, end='; ')
        lines = section.split('0718050')
        lines = lines[1].splitlines()
        print ('\033[94m'+'----------------------------------------------------------------- 0718 05 0 line'+'\033[0m')
        print (lines)
    if (len(lines)==10 or (len(lines)<10 and len(lines)>1)): # to also decode last adress
        try:
            if (makro==False and lines[2][11]=='4'): #makro area start
                makro=True
                print ('\033[1m'+'\033[94m'+'----------------------------------------------------------------- M A C R O area start'+'\033[0m')
                keystart=100
        except:
            print('',end='')
        #0: 0 9 0/8 0 1 0007
        #if (lines[0][0]=='0' and (lines[0][2]=='0' or lines[0][2]=='8' )and lines[0][3]=='0' and lines[0][5:]=='0007'):
        if (lines[0][0]=='0' and (lines[0][2]=='0' or lines[0][2]=='8' or lines[0][2]=='1' )and lines[0][3]=='0' ):
            adress=lines[0][1]
            if (lines[0][2]=='0'):
                adress+=' 0 '
            elif (int(lines[0][2]) & 8):
            #else:
                adress+=' 1 '
            adress+=lines[0][4]
            print ('# adress: '+adress, end='; ')
        #1: 0 9 0/8 0 1 0000
        if (lines[1][0:7]=='0718000'):
            lines[1]=lines[1][7:]
        if (lines[1][0]=='0' and (lines[1][2]=='0' or lines[1][2]=='8' )and lines[1][3]=='0' and lines[1][5:]=='0000'):
            adress=lines[1][1]
            if (lines[1][2]=='0'):
                adress+=' 0 '
            elif (int(lines[1][2]) & 8):
            #else:
                adress+=' 1 '
            adress+=lines[1][4]
            print ('# adress: '+adress, end='; ')
        #2-10: 0718030 28 8 0 2 14 07
        #1  6d 6f 28
        #2  6b 6c 25
        #3  4a 4c 05
        #4  2a 2b 64
        #5  2f 20 69
        #6  4d 4e 07
        #7  2c 2e 66
        #8  0c 0d 46
        key_adresses='#1  |6d 1 0 |6f 0 1 |28 0 2  \
                      #2  |6b 0 0 |6c 1 1 |25 1 2 \
                      #3  |4a 1 0 |4c 0 1 |05 0 2  \
                      #4  |2a 0 0 |2b 1 1 |64 0 2  \
                      #5  |2f 0 0 |20 1 2 |69 0 2 \
                      #6  |4d 0 0 |4e 1 1 |07 1 2  \
                      #7  |2c 1 0 |2e 0 1 |66 1 2  \
                      #8  |0c 0 0 |0d 1 1 |46 0 2'
        if (len(lines)==10):
            if (s==16): #start key ebene 0
                keystart=0
            for i in range(2,10):
                if (keystart==0):
                    print ('\033[1m\033[4;95m'+'|'+'\033[0m', end='') #purple
                if (keystart==5):
                    #print ('///// '+lines[i][12:14]+' /////////', end='')
                    macro_adresses+=';'+lines[i][12:14]
                if (keystart==6):
                    #print ('///// '+lines[i][12:14]+' /////////')
                    macro_adresses+='0'+lines[i][13:14]+';'   # somehow an adress of 84 - filternig 8....
                keystart+=1
                if (keystart==10):
                    keystart=0
                if (lines[i][0:7]=='0718030' and lines[i][10]=='0' and lines[i][14:]=='07'):
                    lines[i]=lines[i][7:]
                    adress=lines[i][0:2]
                    if (lines[i][2]=='0'):
                        adress+=' 0 '
                    else:
                        adress+=' 1 '
                    adress+=lines[i][4]
                    if (adress in key_adresses):
                        print ('\033[1m\033[35m'+'|a: '+adress+'\033[0m', end='; ') #purple
                    else:
                        print ('|a: '+adress, end='; ')
                    if (int(lines[i][4:5]) & 4):
                        if (lines[i][5:7]=='00' and lines[i-1][5:7]=='00'): #makro ende
                            print ('|v:'+'\033[1m'+'\033[94m'+'-! '+'\033[0m', end='; ') #blue
                        #elif (lines[i][5:7]=='01' and i==2 and lines[i+1][12:14]=='00'): #makro anfang
                        elif (';'+lines[i][1:5]+';' in macro_adresses and i==2):
                            print ('|v: '+'\033[1m'+'\033[94m'+'++'+'\033[0m', end='; ') #blue
                        elif (lines[i][5:7]=='00'):
                            print ('|v:  ', end='; ')
                        else:
                            print ('|v:'+'\033[1m'+lines[i][5:7]+'\033[0m', end=';')  #bold
                        try:
                            if (str(i) in "3579"): # filter 04 makro keys only every 2nd
                                print ('\033[1m\033[91m'+k['0x'+str(lines[i][5:7])][4:]+'\033[0m', end=' ') #red
                        except:
                            print('', end=' ')
                        if (str(i) in "2468"): # filter 04 makro delay every other
                            if (int('0x'+lines[i][5:7],16) & 0x80): # key down 
                                print ('\033[1m\033[31m_\033[0m', end='')
                            elif (lines[i][5:7]=='01' and i==2): # key down 
                                print('',end='')
                            elif (lines[i][5:7]!='00'): # key down 
                                print ('\033[1m\033[31m^\033[0m', end='')
                    elif (lines[i][5:7]=='00'):
                        print ('|v:   ', end='; ')
                    else:
                        print ('|v: '+'\033[1m'+lines[i][5:7]+'\033[0m', end=';')  #bold
                        try:
                            if (lines[i][3:5]!='04'):
                                print ('\033[1m\033[91m'+k['0x'+str(lines[i][5:7])][4:]+'\033[0m', end=' ') #red
                            else:
                                print('', end=' ')
                        except:
                            print('', end=' ')
                
    else:
        print ('\033[94m'+'----------------------------------------------------------------- exeption !=10 lines'+'\033[0m', end=' ')
    s+=1
    print ('')
print(macro_adresses)

