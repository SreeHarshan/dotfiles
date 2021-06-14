#!/usr/bin/python3
import numpy as np
from PIL import Image

print('''------------------------------------------------------------------------
 CAVA COLOR CHANGER
------------------------------------------------------------------------
by Sree Harshan
 ''')
 
print("Starting program in wallpaper read mode")

f = open("/home/harshan/.cache/wal/sequences","r+")
#f = open("/home/harshan/scripts/curr_wall","r")

#convert colors to hex
def colors2hex(l):
    c = []
    for i in l:
        s = "#"
        for j in i:
            h = hex(j)[2:]
            if len(h) < 2:
                h += "0"
            s += h
        s = s.upper()
        c.append(s)
    return c
#difference
def diff(a,b):
    c = a - b
    if c > 0:
        return c
    return c * -1
def palette(img):
    """
    Return palette in descending order of frequency
    """
    arr = np.asarray(img)
    palette, index = np.unique(asvoid(arr).ravel(), return_inverse=True)
    palette = palette.view(arr.dtype).reshape(-1, arr.shape[-1])
    count = np.bincount(index)
    order = np.argsort(count)
    return palette[order[::-1]]

def asvoid(arr):
    """View the array as dtype np.void (bytes)
    This collapses ND-arrays to 1D-arrays, so you can perform 1D operations on them.
    http://stackoverflow.com/a/16216866/190597 (Jaime)
    http://stackoverflow.com/a/16840350/190597 (Jaime)
    Warning:
    >>> asvoid([-0.]) == asvoid([0.])
    array([False], dtype=bool)
    """
    arr = np.ascontiguousarray(arr)
    return arr.view(np.dtype((np.void, arr.dtype.itemsize * arr.shape[-1])))


#read from wall
colors_wal=[]
colors = []
curr=""
for i in f.read():
    if i == '#':
        curr="#"
    elif '#' in curr and len(curr) < 7:
        curr+=i
        if len(curr) == 7:
            colors_wal.append(curr)
            curr=""
print(colors_wal)
for i in colors_wal:
    r = int(i[1:3],16)
    g = int(i[3:5],16)
    b = int(i[5:7],16)
    colors.append([r,g,b])
colors = colors[1:7]
'''

#read from background
path = '/home/harshan/'+f.read()[:-1]
print("Getting image from",path)
print()

#Colors from the image
img = Image.open(path, 'r').convert('RGB')
img = img.resize((320,180))
colors = palette(img)
print("Number of colors from image:",len(colors))
'''
f.close()
print()
f = open("/home/harshan/.config/cava/config","w")
part1='''## Configuration file for CAVA. Default values are commented out. Use either ';' or '#' for commenting.


[general]

# Smoothing mode. Can be 'normal', 'scientific' or 'waves'. DEPRECATED as of 0.6.0
; mode = normal

# Accepts only non-negative values.
; framerate = 60

# 'autosens' will attempt to decrease sensitivity if the bars peak. 1 = on, 0 = off
# new as of 0.6.0 autosens of low values (dynamic range)
# 'overshoot' allows bars to overshoot (in % of terminal height) without initiating autosens. DEPRECATED as of 0.6.0
; autosens = 1
; overshoot = 20

# Manual sensitivity in %. Autosens must be turned off for this to take effect.
# 200 means double height. Accepts only non-negative values.
; sensitivity = 100

# The number of bars (0-200). 0 sets it to auto (fill up console).
# Bars' width and space between bars in number of characters.
; bars = 0
; bar_width = 2
; bar_spacing = 1


# Lower and higher cutoff frequencies for lowest and highest bars
# the bandwidth of the visualizer.
# Note: there is a minimum total bandwidth of 43Mhz x number of bars.
# Cava will automatically increase the higher cutoff if a too low band is specified.
; lower_cutoff_freq = 50
; higher_cutoff_freq = 10000


# Seconds with no input before cava goes to sleep mode. Cava will not perform FFT or drawing and
# only check for input once per second. Cava will wake up once input is detected. 0 = disable.
; sleep_timer = 0


[input]

# Audio capturing method. Possible methods are: 'pulse', 'alsa', 'fifo', 'sndio' or 'shmem'
# Defaults to 'pulse', 'alsa' or 'fifo', in that order, dependent on what support cava was built with.
#
# All input methods uses the same config variable 'source'
# to define where it should get the audio.
#
# For pulseaudio 'source' will be the source. Default: 'auto', which uses the monitor source of the default sink
# (all pulseaudio sinks(outputs) have 'monitor' sources(inputs) associated with them).
#
# For alsa 'source' will be the capture device.
# For fifo 'source' will be the path to fifo-file.
# For shmem 'source' will be /squeezelite-AA:BB:CC:DD:EE:FF where 'AA:BB:CC:DD:EE:FF' will be squeezelite's MAC address
; method = pulse
; source = auto

; method = alsa
; source = hw:Loopback,1

; method = fifo
; source = /tmp/mpd.fifo
; sample_rate = 44100
; sample_bits = 16

; method = shmem
; source = /squeezelite-AA:BB:CC:DD:EE:FF

; method = portaudio
; source = auto


[output]

# Output method. Can be 'ncurses', 'noncurses' or 'raw'.
# 'noncurses' uses a custom framebuffer technique and draws only changes
# from frame to frame. 'ncurses' is default if supported
#

# 'raw' defaults to 200 bars, which can be adjusted in the 'bars' option above.
; method = ncurses

# Visual channels. Can be 'stereo' or 'mono'.
# 'stereo' mirrors both channels with low frequencies in center.
# 'mono' outputs left to right lowest to highest frequencies.
# 'mono_option' set mono to either take input from 'left', 'right' or 'average'.
; channels = stereo
; mono_option = average

# Raw output target. A fifo will be created if target does not exist.
; raw_target = /dev/stdout

# Raw data format. Can be 'binary' or 'ascii'.
; data_format = binary

# Binary bit format, can be '8bit' (0-255) or '16bit' (0-65530).
; bit_format = 16bit

# Ascii max value. In 'ascii' mode range will run from 0 to value specified here
; ascii_max_range = 1000

# Ascii delimiters. In ascii format each bar and frame is separated by a delimiters.
# Use decimal value in ascii table (i.e. 59 = ';' and 10 = 'n' (line feed)).
; bar_delimiter = 59
; frame_delimiter = 10

[color]

# Colors can be one of seven predefined: black, blue, cyan, green, magenta, red, white, yellow.
# Or defined by hex code '#xxxxxx' (hex code must be within ''). User defined colors requires
# ncurses output method and a terminal that can change color definitions such as Gnome-terminal or rxvt.
# if supported, ncurses mode will be forced on if user defined colors are used.
# default is to keep current terminal color
; background = default
; foreground = default

# Gradient mode, only hex defined colors (and thereby ncurses mode) are supported,
# background must also be defined in hex  or remain commented out. 1 = on, 0 = off.
# You can define as many as 8 different colors. They range from bottom to top of screen
 gradient = 1
; gradient_count = 8
; gradient_color_1 = '#59cc33'
; gradient_color_2 = '#80cc33'
; gradient_color_3 = '#a6cc33'
; gradient_color_4 = '#cccc33'
; gradient_color_5 = '#cca633'
; gradient_color_6 = '#cc8033'
; gradient_color_7 = '#cc5933'
; gradient_color_8 = '#cc3333'

 gradient_count = 8
; gradient_color_1 = '#00d7d7'
; gradient_color_2 = '#59cc33'
; gradient_color_3 = '#80cc33'
; gradient_color_4 = '#a6cc33'
; gradient_color_5 = '#cccc33'
; gradient_color_6 = '#cca633'
; gradient_color_7 = '#cc8033'
; gradient_color_8 = '#cc5933'


;gradient_count=3
;gradient_color_1 = '#f14457'
;gradient_color_2 = '#71265e'
;gradient_color_3 = '#130833'

 gradient_count=6

'''
part2='''[smoothing]

# Percentage value for integral smoothing. Takes values from 0 - 100.
# Higher values means smoother, but less precise. 0 to disable.
; integral = 77

# Disables or enables the so-called "Monstercat smoothing" with or without "waves". Set to 0 to disable.
; monstercat = 0
; waves = 0

# Set gravity percentage for "drop off". Higher values means bars will drop faster.
# Accepts only non-negative values. 50 means half gravity, 200 means double. Set to 0 to disable "drop off".
; gravity = 100


# In bar height, bars that would have been lower that this will not be drawn.
; ignore = 0


[eq]

# This one is tricky. You can have as much keys as you want.
# Remember to uncomment more then one key! More keys = more precision.
# Look at readme.md on github for further explanations and examples.
; 1 = 1 # bass
; 2 = 1
; 3 = 1 # midtone
; 4 = 1
; 5 = 1 # treble'''

colors_main = []
colors_sorted = []
colors_lightness = []
colors_lightness_original = []
print(colors)
#Select 6 colors
l = len(colors)
#for i in range(int(l/8),l,int(l/7)):
for i in range(l):
    R = colors[i][0]
    G = colors[i][1]
    B = colors[i][2]
    colors_main.append(colors[i])
    colors_lightness.append(0.212 * R + 0.701 * G + 0.087 * B)
    colors_lightness_original.append(0.212 * R + 0.701 * G + 0.087 * B)

#Sort them by lightness of the colors
colors_lightness.sort()
for i in colors_lightness:
    idx = colors_lightness_original.index(i)
    colors_sorted.append(colors_main[idx])
'''
#Sort them based on shades
shades = {
'r' : list(),
'g' : list(),
'b' : list(),
'y' : list(),
'p' : list(),
'a' : list(), 
'b' : list(),
'w' : list()
}
for i in colors_sorted:
    R = i[0]
    G = i[1]
    B = i[2]
    l = [R,G,B]
    if R < 20 and G < 20 and B < 20:
        shades['b'].append(l)
    elif R > 200 and G >  200 and B > 200:
        shades['w'].append(l)
    elif diff(R,G) < 20 and diff(R,B) > 20 and diff(G,B) > 20:
        shades['y'].append(l)
    elif diff(R,B) < 20 and diff(R,G) > 20 and diff(B,G) > 20:
        shades['p'].append(l)
    elif diff(B,G) < 20 and diff(R,B) > 20 and  diff(R,G) > 20:
        shades['a'].append(l)
    elif R > B and R > G:
        shades['r'].append(l)
    elif B > R and B > G:
        shades['b'].append(l)
    else:
        shades['g'].append(l) 


colors_sorted2 = []
shades_sorted = []
shades_sorted2 = []
color_list = []

for i in shades.values():
    shades_sorted.append(len(i))
    shades_sorted2.append(len(i))
    color_list.append(i)

print()
print("Shades sorted:",shades_sorted)
print("Color list:",color_list)
print("Shades:",shades)

while len(shades_sorted) > 0:
    m = max(shades_sorted)
    idx = shades_sorted.index(m)
    if m == 0:
        break
    shades_sorted.remove(m)
    colors_sorted2.extend(color_list[idx])
    color_list.pop(idx)

print()
print("Colors sorted method 2:",colors_sorted2)

colors_sorted2 = colors2hex(colors_sorted2)

print("Colors sorted method 2(hex):",colors_sorted2)
print()
'''
#Convert them to hex
colors_main = colors2hex(colors_main)
colors_sorted = colors2hex(colors_sorted)

#Log 

print("Colors chosen:",colors_main)
print("Colors sorted:",colors_sorted)
print("Colors(sorted) lightness:",colors_lightness)
print("Colors sorted_index:", end = " ")

#for i in colors_sorted:
#    print(colors_main.index(i),end=" ")
print()

#old method ( works better than the new one
colors_sorted.sort()
#colors_sorted = colors_sorted2

colors_in_str='''
 gradient_color_1 = '{}'
 gradient_color_2 = '{}'
 gradient_color_3 = '{}'
 gradient_color_4 = '{}'
 gradient_color_5 = '{}'
 gradient_color_6 = '{}'
'''.format(colors_sorted[0],colors_sorted[1],colors_sorted[2],colors_sorted[3],colors_sorted[4],colors_sorted[5])



print("Colors used: ",colors_in_str)
    
s = part1 + colors_in_str + part2
f.write(s)
f.close()
