  #!/bin/bash
  
  echo "content-type: text/html"
  echo
  echo
  echo "<html> <head> <title> IPTV </title> </head>"
  echo "<body>"
  echo "#EXTM3U<br>"
  echo "#EXTINF:0, SBT RS<br>"
  ./youtube-dl -f 300 -g https://www.youtube.com/user/TVSBTRS/live && echo "<br>"
  echo "</body>"
  echo "</html>"
