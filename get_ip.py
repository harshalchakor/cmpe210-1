import os
os.system("ifconfig | grep 'inet' | grep -v 127.0.0.1 | grep -v inet6 | cut -d: -f2 | awk '{print $1} | tail -1")
