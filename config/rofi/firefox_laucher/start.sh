# Profiles
default='❤ Default'
school='🕮  School'
anime='☯ Anime'
programming='🖥️ Programming'


rofi_cmd(){
    rofi -p "Firefox" -dmenu -i -theme ~/.config/rofi/firefox_laucher/config.rasi
}

run_rofi() {
	echo -e "$default\n$school\n$anime\n$programming" | rofi_cmd
}

chosen="$(run_rofi)"

case ${chosen} in
    $default)
        firefox
        ;;
    $school)
        firefox --p school
        ;;
    $anime)
        firefox --p anime
        ;;
    $programming)
        firefox --p programming	
        ;;
esac
