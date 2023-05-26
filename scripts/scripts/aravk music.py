import os
import time
import ueberzug.lib.v0 as ueberzug
from curses import wrapper
import curses
import dbus

MUSIC_DIR = "/home/aravk/Music/Exemplary"
ALBUM_ART_LOCATION = "/tmp/npmpd"


@ueberzug.Canvas()
def main(stdscr, canvas):
    
    cover_art = canvas.create_placement(
        "cover_art",
        x=1,
        y=1,
        width=30,
        height=curses.LINES,
        scaler=ueberzug.ScalerOption.CONTAIN.value
    )
    cover_art.path = metadata["mpris:artUrl"]
    cover_art.visibility = ueberzug.Visibility.VISIBLE
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.addstr(5, 36, "Title", curses.A_BOLD | curses.color_pair(1))
    stdscr.addstr(": " + metadata['xesam:title'])
    #stdscr.addstr(6, 36, "albumArtist", curses.A_BOLD | curses.color_pair(1))
    #stdscr.addstr(": " + metadata['xesam:albumArtist'])
    stdscr.addstr(7, 36, "Album", curses.A_BOLD | curses.color_pair(1))
    stdscr.addstr(": " + metadata['xesam:album'])
    #stdscr.addstr(9, 36, "Disc", curses.A_BOLD | curses.color_pair(1))
    #stdscr.addstr(": " + metadata['xesam:discNumber'])
    #stdscr.addstr(10, 36, "Track", curses.A_BOLD | curses.color_pair(1))
    #stdscr.addstr(": " + metadata['mpris:trackid'])
    stdscr.refresh()
    time.sleep(1)
    while True:
        c = stdscr.getch()
        if c == ord("q"):
            break
        elif c == ord("n"):
            cover_art.path = "/home/aravk/Pictures/space colony.png"


if __name__ == "__main__":
     session_bus = dbus.SessionBus()
     spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify","/org/mpris/MediaPlayer2")
     spotify_properties = dbus.Interface(spotify_bus,"org.freedesktop.DBus.Properties")
     metadata=spotify_properties.Get("org.mpris.MediaPlayer2.Player","Metadata")
     for key,value in metadata.items():
    	 print(key, value)
     wrapper(main)
