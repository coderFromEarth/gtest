
#  Append the /home/usename/.bashrc file with this function
command_not_found_handle ()
{
    if [ -x /usr/lib/command-not-found ]; then
        /usr/bin/python /usr/lib/command-not-found -- "$1";
        return $?;
    else
        if [ -x /usr/share/command-not-found/command-not-found ]; then
            /usr/bin/python /usr/share/command-not-found/command-not-found -- "$1";
            return $?;
        else
            printf "%s: Come on! You can do it! \n" "$1" 1>&2;
            return 127;
        fi;
    fi
}
