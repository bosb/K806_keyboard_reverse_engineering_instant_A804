# How it all started 🐇

I was looking for something to control Teams during standup without mouse and multi key shortcuts.
* Mute/unmute
* Camera on/off
* Raise/lower hand
* Hangup

# Sending USB HID sequences somehow.
Closest I had laying around was a Nordic Semiconductor nrf5340 DK dev board, which had 4 switches onboard 🧑‍💻.
https://www.nordicsemi.com/Products/Development-hardware/nRF5340-DK
As starting point Zephyr samples/subsys/usb/hid-keyboard
https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/hid-keyboard/src/main.c
I was satisfied how efficient it brought me through standup and other meetings.
I was not satisfied with the switches and having bare metal board lying around next to a metal laptop ⚡.

# 💡 Idea was to look for a cheap small makro keyboard, 
that looks easy to open and close, that I could use to hookup the keys via I2C multiplexer to an µC, or maybe that is working out of the box... 🎁

# Browsing Aliexpress, 
looking for some Welcome offer around macro keyboards, I ended up spending 0,99 € including shipping to Germany on this 8 key thing:
- screws are visible, easy to dismantle
- nice keys 1️⃣ 3️⃣ 2️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣
- a little more than 4 keys, but keeping it small in size
- even somehow programable, no software link in my offer, but expecting some windows proprietary app
Didn't look deeper in it before ordering, was good enough for my plans and knowledge at that point of time 🎯.

![K806 keyboard](https://github.com/user-attachments/assets/eb761348-c1c0-4dad-a415-7a4df1a5fbfd)

Titles from Aliexpress:
- 8 Key Macro Programmable Fully Hot Swappable Mechanical Switch 4 Color RGB Light Gaming Mini Keyboard
- 8 Key Shortcut Macro Programmable Fully Hot Swappable Mechanical Switch Gaming Mini Keyboard One-piece Computer Accessories
- USB-C Wired Mechanical Gaming Keyboard 8Keys Mini Keypad 4 Color RGB Light Customize Programmable Macro Keyboard Numeric Keypad
black/white/orange with red switch

The nice thing about using a new account for every order on Aliexpress:
- Welcome offer of 0,99 € for things that cost ca. up to 10-15 €
- Free shipping ca. 7 days +/- 1 day

# So, while waiting I started some deeper digging... 🕵️
One offer had a review with dismantled pictures and naming the chip on the board:
Instant A804f 14 pins
Only pdf datasheet to that is https://www.instant-sys.com/uploads/pdf/norm/A804_en.pdf
Where it is advertised as:
"A804 is a high performance single chip CMOS process optical mouse sensor."

Software found: http://www.mkespnhk.com/Download.aspx?ClassID=37&page=3
- -> K806 drive A804 Size：4548.94kb 2024-08-19 http://www.mkespnhk.com/upload/20240926133937.zip
- Or from homepage http://www.mkespnhk.com/Default.aspx -> Download -> Driver Download and switch through pages...

# While looking for the software and possible alternatives... 🐇
- I stumbled uppon QMK https://docs.qmk.fm/
- https://www.reddit.com/r/MechanicalKeyboards/wiki/firmware/
- 'hot swapable'
- making a keyboard bluetooth able
All interesting, a whole new world finding out about keyboard fimware, customizable switches, but all (macro) keyboards supporting this were above the amount I wanted to spend 💸, I was more in investing time exploring how to get my ordered keyboard working.

Some candidate on aliexpress:
ZUOYA GMK26 QMK/VIA Gasket Number Pad Bluetooth 5.0/2.4ghz/Wired Hot Swappable Numpad Programmable for Win/Mac

(But if all fails I found a suitable fully documented open source makro keyboard that I can use for sure to my needs:
Adafruit MacroPad RP2040 Starter Kit - 3x4 Keys + Encoder + OLED - ADABOX019 Essentials ~ 50 €
https://www.adafruit.com/product/5128)

# Idea to get rid of windows software 
and also use, (ok, it is useable on all systems, but programable only on windows) on my mac was to sniff 🐽 the USB bus:
- wireshark
- https://wiki.wireshark.org/CaptureSetup/USB
- USBPcap https://desowin.org/usbpcap/ 

Searched for other chip documentation from same manufacturer...
Overview of chips from Instand Microelectronics https://instant-sys.com/en/page-20.html

Found some inspiration from others while digging on github:
- https://github.com/rOzzy1987/MacroPad/tree/main vendor 4489 Trisat IndTry Computer Co. LTD.ustrial Co., Ltd.
- https://github.com/kriomant/ch57x-keyboard-tool/tree/master Vendor ID: 0x1189 (Trisat Industrial Co., Ltd.)
- https://github.com/santeri3700/hyperx_pulsefire_dart_reverse_engineering
- https://bytepunk.wordpress.com/2017/03/25/reverse-engineering-a-usb-mouse/
- 🥇 https://blog.lx862.com/blog/2024-05-13-reverse-engineering-a-mouse/ uses 'same software' closest doc I found
- https://github.com/Kenny-Hui/Instant-A704F-Mouse-Utilities/blob/main/SPECS.md

# Arrived:
K806 8 key macro programming game keyboard
Dongguan Shixingsheng Electronic Technology Co.,Ltd
Execution Standard: GB/T 26245-2010
6 972543 650226
MKESPN
![PXL_20250609_133801125](https://github.com/user-attachments/assets/64c07b7a-2ffa-496a-b448-86561ebd979b)
![PXL_20250609_133844599](https://github.com/user-attachments/assets/f25cdb70-a03a-4988-b892-adba8916f9e9)
![PXL_20250609_133906108](https://github.com/user-attachments/assets/49e4190b-2966-4681-886e-8638bfff0c95)
![PXL_20250609_133850413](https://github.com/user-attachments/assets/1df2e3cc-8f0f-4ea4-a4ff-ca6f57ce5ed1)
