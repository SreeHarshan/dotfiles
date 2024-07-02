
send_notif(){
	sink=`pactl list short sinks | sed -e 's,^\([0-9][0-9]*\)[^0-9].*,\1,' | head -n 1`
	volume=`pactl list sinks | grep '^[[:space:]]Volume:' | head -n 1 | sed -e 's,.* \([0-9][0-9]*\)%.*,\1,'`
	muted=`pactl list sinks | awk '/^\s*Mute: / {if($2=="yes"){print "!"}; exit}'`

	dunstctl close-all
	notify-send "Volume: $volume" -t 1000

}

# Execute accordingly
case "$1" in
	"--inc")
		pactl set-sink-volume @DEFAULT_SINK@ +1%
		;;
	"--dec")
		pactl set-sink-volume @DEFAULT_SINK@ -1%
		;;
	*)
		send_notif
		;;
esac

send_notif
