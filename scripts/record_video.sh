#!/usr/bin/env bash 
if [ $# -ne 2 ]
  then
    echo "Usage: $0 commit_id [start|stop]"
fi

OUTPUTFILE=video_$1_$(date +%s).mp4

if [ "$2" == "start" ]; then
  echo "[software/video] Starting record to $OUTPUTFILE"
  ffmpeg -loglevel panic -f oss -f video4linux2 -i /dev/video0 \
    -vf "drawtext=fontfile=/nix/store/z32n1b8r06v5py3higzs2rww5dq4s58z-dejavu-fonts-2.37/share/fonts/truetype/DejaVuSans-Bold.ttf: \
    text='$1 | %{localtime} | %{pts}': x=(w-tw)/2: y=h-(2*lh): fontcolor=white: box=1: boxcolor=0x00000000@1: fontsize=15" $OUTPUTFILE &
  export VPID=$!
elif [ "$2" == "stop" ]; then
  echo "[software/video] Stopping the recording of $OUTPUTFILE"
  pkill ffmpeg
fi
