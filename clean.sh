#!/usr/bin/env bash

# this script is used to clean all .html files.

find $1 -name "*.html" > html_tmp
while read line
do
    rm "$line"
done < html_tmp

rm html_tmp