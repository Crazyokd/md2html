#!/usr/bin/env bash

# this script is used to convert md to html

# reset alias
nameRM="rm"
nameCP="cp"

function resetAlias() {
    alias $1 > error 2>&1
    if [ $? -eq 0 ]; then
        echo "reset $1"
        name=`alias $1 | awk 'BEGIN{FS="="}{ print $(NF)}'`
        name=${name//\'/}
        name=${name//\"/}
        if [ $1 == "cp" ]; then
            nameCP=$name
            unalias cp
        else 
            nameRM=$name
            unalias rm
        fi
    fi
}

resetAlias "rm"
resetAlias "cp"




# md to html
function mdToHtml() {
    find $1 -name "*.md" > error
    while read line
    do
        python3 md2html.py "$line"
    done < error
}



# convert .md file to .html file
python3 -m venv .venv
source ./.venv/bin/activate
pip3 list | grep mistune > error 2>&1
if [ $? -ne 0 ]; then
    echo "install mistune."
    pip3 install mistune > error
fi


mdToHtml "md"


rm error

# restore alias
if [ "rm" != "$nameRM" ]; then
    alias rm="$nameRM"
fi
if [ "cp" != "$nameCP" ]; then
    alias cp="$nameCP"
fi