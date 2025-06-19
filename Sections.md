# LEDs

| led mode |  | 
| ------------ | ------------ | 
|90 |cycle min speed|
|91 |...|
|92 |...|
|93 |...|
|94 |...|
|95 |cycle max speed|
|97 |all off|
|98 |individual led on/off via led definition|

| color |  | 
| ------------ | ------------ | 
|55 |blue pink red lila|
|x4 |pink|
|x1 |blue|
|1x |red|
|4x |lila|
|00 |none|

| fire |  | 
| ------------ | ------------ | 
|00| 0|
|06| 50|
|0c| 151|
|12| 200|
|19| 248|
|1f| 300|

# Key type
||| |
| ------------ | ------------ |  ------------ | 
|0x| led off| |
|2x| bit value led on| |
|xf| ?! d+2... just mail?| |
|01| left button   |  key definition section all 10 bytes are 0 (")|
|02| middle button  | "|
|03| right button  |  "|
|04| back           | "|
|05| forward        | "|
|06| dpi loop       | "|
|07| show desktop| |
|08| double click  |  "|
|09| fire| |
|0a|| |
|0b| dpi+| |
|0c| dpi-| |
|0d| -MACRO-| |
|0e| -KEY-| |
|0f| mail     |       3 0 0 8a 01 c804 0 0 0|
|14| fn| |
|15| led loop    |    "|
|16|| |
|17| level I    |     "|
|18| ....level IV | - not available in windows software|
|19| level II      |  "|
|1a| level III     |  "|
|1b| |

# Key definition
10 byte

| 0 |  1  |          2   |   3 | 4 | 5  |      6 |   7 |  8  |      9 |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | 
|3/7| 0/1/4/7  |    single key value |0 | 0 | macro address a+b|address c| 0 |  macro 0a| 0|


# Macro

...
