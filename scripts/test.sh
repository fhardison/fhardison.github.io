#!/bin/zsh

# Get a list of filenames in the subdirectory
files=$(ls -1 ../blog/)


awk -v files="$files" '
    BEGIN {
        split(files, fileArray, "\n")
        links = "<ul>"
        for (i in fileArray) {
            links = links "<li><a href=\"" fileArray[i] "\">" fileArray[i] "</a></li>"
        }
        links = links "</ul>"
    }
    /\$links\$/ { $0 = gensub(/\$links\$/, links, 1) }
    { print }
' index.html > new_index.html

mv new_index.html index.html
