#LEDs

#Key type
|||
| ------------ | ------------ | 
|0x| led off|
|2x| bit value led on|
|xf| ?! d+2... just mail?|
|01| left button    key 10 all 0|
|02| middle button  "|
|03| right button   "|
|04| back           "|
|05| forward        "|
|06| dpi loop       "|
|07| show desktop|
|08| double click   "|
|09| fire|
|0a||
|0b| dpi+|
|0c| dpi-|
|0d| -MACRO-|
|0e| -KEY-|
|0f| mail           3 0 0 8a 01 c804 0 0 0|
|14| fn|
|15| led loop       "|
|16||
|17| level I        "|
|18| ....level IV - not available in windows software|
|19| level II       "|
|1a| level III      "|
|1b|

#Key definition
10 byte

| 0 |  1  |          2   |   3 | 4 | 5  |      6 |   7 |  8  |      9 |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | 
|3/7| 0/1/4/7  |    single key value |0 | 0 | macro address a+b|address c| 0 |  macro 0a| 0|


#Macro
