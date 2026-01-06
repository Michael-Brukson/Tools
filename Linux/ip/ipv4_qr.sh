# qrencode -t ansiutf8  ""

# "protocol" parameter- string representation of SEC parameter. Allows waving of headache-y if statements.
_PROT="http"
# "port" parameter- what port to send to qrenco.de. 80 default
_PORT="80"
# "verbose" parameter- whether to log parameters. default false.
_VERBOSE=0
# "route" parameter- name of additional string at end of route. Defaults to empty.
_ROUTE=""

# TODO: Add option for long argument (i.e. --port)
while getopts ":svp:r:" option; do
    case $option in
        s)
            _SEC=1
            _PROT="https";;
        v)
            _VERBOSE=1;;
        p) 
            _PORT=${OPTARG};;
        r)
            _ROUTE=${OPTARG};;
    esac    
done
shift $((OPTIND-1))

function log () {
	echo "Using: $_PROT"
	echo "Port: $_PORT"
	echo "Host: $_HOST"
	echo "Route: $_ROUTE"
	echo "curling: $_URL"
}

_HOST=`./ipv4.sh`
_URL="$_PROT://$_HOST:$_PORT/$_ROUTE"
# replace route spaces with %20 for urls
_URL="${_URL// /"%20"}"

if [[ $_VERBOSE -eq 1 ]]; then 
    log
fi

# TODO: Add option to output to image
qrencode -t utf8 $_URL