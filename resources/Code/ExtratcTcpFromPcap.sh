#!/bin/zsh

# infile = file to input
# outfile = file to output
# ext = extension of the output file

for stream in $(tshark -nlr $infile -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq | sed 's/\r//')
do
    echo "Processing stream $stream: ${outfile}_${stream}.${ext}"
    tshark -nlr $infile -qz "follow,tcp,raw,$stream" | tail -n +7 | sed 's/^\s\+//g' | xxd -r -p | tee ${outfile}_${stream}.${ext} >> ${outfile}_all.${ext}
done