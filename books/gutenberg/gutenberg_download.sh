#!/bin/bash

# set -x

function download_books(){
	lang=$1
	n=$2
	echo "=== Downloading n=$n; lang=$lang ..."
	# mkdir -p ${lang}
	# cd ${lang}
	# curl -s "https://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=${lang}" 2>&1 | grep -oE "http[^\"]*zip" | grep -v ".*-.\.zip" | wc
	# curl -s "https://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=${lang}" 2>&1 | grep -oE "http[^\"]*zip" | grep -v ".*-.\.zip" | head -n${n} | sort | uniq | head | while read url ; do echo wget -q ${lang} "$url" ; done
	curl -s "https://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=${lang}" 2>&1 | grep -oE "http[^\"]*\.zip" | sort | uniq |  head -n${n} | while read url ; do echo $url ; wget -q -O ${lang}-$(basename $url) "$url" ; done
	# sleep 2
	# cd ..
	echo "=== DONE n=$n; lang=$lang !!!"
	echo ""
}

rm -f *.zip *.txt

download_books "es" $1
download_books "en" $1
download_books "de" $1
download_books "fr" $1

# set -x

ls -l *.zip
ls -1 *.zip | while read zip ; do
	txt=$(basename "$zip" .zip).txt
	unzip -nq -p "$zip" > "$txt"
	charset=$(file -bi "$txt" | awk -F"=" '{print $2}')
	if [ "$charset" == "binary" ] ; then
		charset="CP1252"
	fi
	iconv -f $charset -t UTF-8 "$txt" > $(basename $txt .txt)_UTF8.txt
done

file *_UTF8.txt

mkdir -p utf8_books
file *.txt | grep UTF-8 | cut -d':' -f1 | xargs -I x cp x utf8_books/

rm -f *.txt *.zip

# echo "============="
# echo "=== RESULTS"
# head -n100 ./*.txt | grep -E "==>|Title:|Author:|Release Date:|Language:|Character set encoding:"



