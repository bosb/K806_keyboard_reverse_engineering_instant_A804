# How to reverse ♻️

Keyboard itself is cool, no need to harm it, does already what I wanted...

But how does it work and is there some hidden feature? 💡

My workflow:
- record several buttonpress to 'apply' in windows software with pcap, takes some seconds
- load in wireshark ui to see whats happening in the beginning + end (try attached example setabcdef.pcap), filter for some data in file to look for reliable session seperation indicators
- for efficience do several changes in one recordng session, write down what changes were made between programming the keyboard
- get relevant data by wireshark commandline:
> `$ tshark -r setabcdef.pcap -T fields -e usb.data_fragment -Y "usbhid.setup.bRequest == 0x09" > setabcdef.pcap.txt`
- split result in programming session/apply parts:
> `$ csplit -f setabcdef.pcap.txt setabcdef.pcap.txt /0718100000000000/ {34}`
<br> `{*}` didn't work for me, so I start above the expected session number and go down until no error appears

I had several candidates for a session start/seperation: 0718030001000300 0718090001000000 0718000001000000

But most reliable is session end:   0718100000000000

I ended up in a bunch of files ca 18/21 kB

Now diff files with e.g vimdiff and guess what happens where

I scripted a 'decompiler' to visualize and verify my findings, not nice coded, but helped;

`python3 decompile.py setabcdef.pcap.txt`
<pre>
  1: 10
['001000000', '0718000001000000', '0718030008002e07', '0718030108002e07', '0718030208002e07', '0718030308002e07', '0718030408002e07', '0718030508002e07', '0718030608002e07', '0718030708000007']
# adress: 00; |a: 00 1 0; |v: 2e; |a: 10 1 0; |v: 2e; |a: 20 1 0; |v: 2e; |a: 30 1 0; |v: 2e; |a: 40 1 0; |v: 2e; |a: 50 1 0; |v: 2e; |a: 60 1 0; |v: 2e; |a: 70 1 0; |v:   ; 
2: 10
['008000007', '0718000008000000', '0718030010002e07', '0718030110000007', '0718030210000007', '0718030310003807', '0718030410000807', '0718030510006c07', '071803061000f207', '0718030710000207']
# adress: 0 1 0; # adress: 0 1 0; |a: 01 0 0; |v: 2e; |a: 11 0 0; |v:   ; |a: 21 0 0; |v:   ; |a: 31 0 0; |v: 38; |a: 41 0 0; |v: 08;E |a: 51 0 0; |v: 6c;F17 |a: 61 0 0; |v: f2; |a: 71 0 0; |v: 02; 
3: 10
['010000007', '0718000010000000', '0718030018001807', '0718030118000f07', '0718030218000607', '0718030318000007', '0718030418009b07', '0718030518005407', '0718030618000107', '0718030718000007']
# adress: 1 0 0; # adress: 1 0 0; |a: 01 1 0; |v: 18;U |a: 11 1 0; |v: 0f;L |a: 21 1 0; |v: 06;C |a: 31 1 0; |v:   ; |a: 41 1 0; |v: 9b; |a: 51 1 0; |v: 54; |a: 61 1 0; |v: 01; |a: 71 1 0; |v:   ; 
...
</pre>
