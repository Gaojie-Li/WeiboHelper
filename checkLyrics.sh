cd ~/Library/Containers/com.netease.163music/Data/Caches/orpheus_path

for t in *;
do
    if grep -q lrc $t;
        then greadlink -f $t
    fi
done
