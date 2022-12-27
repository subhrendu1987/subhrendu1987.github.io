#!/bin/bash

ROOT="./"
HTTP="https://subhrendu1987.github.io/pub/papers"
OUTPUT="index.html" 

i=0
echo "<HTML><BODY><UL>" > $OUTPUT
  for i in `find "$ROOT" -maxdepth 1 -mindepth 1 -type f| sort`; do
    file=`basename "$i"`
    ### echo "$file, $0, $OUTPUT"
    if [ "$file" != `basename "$0"` ] && [ "$file" != `basename "$OUTPUT"` ]
    then
    	echo "    <LI><a href=\"$HTTP/$file\">$file</a></LI>" >> $OUTPUT
    fi
  done
  echo "  </UL></BODY></HTML>" >> $OUTPUT