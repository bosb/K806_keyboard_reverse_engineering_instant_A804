Just a few different 'commands' show up.
Layout of command:

<pre>
         |adresse d: 0-7
         | |a: 0-f 
         | | |just highest bit b:0/1
         | | |  |c: 0,1,2,4,5...?       
0718 09 01 f 8 01 00 07
     |            |   |? 0/7
     |            |value
     |00 03 05 09 command
</pre>

03: set byte
09: write 8 byte
00: in combination with 09 and last byte 00 instead of 07
05: ?

First 8 bytes are set with d: 0..7
Then command 09 + 00
