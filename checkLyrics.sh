# cd ~/Library/Containers/com.netease.163music/Data/Caches/orpheus_path
$LPATH="~/Library/Containers/com.netease.163music/Data/Caches/orpheus_path"

if [-f netease.list]
then
    rm netease.list
fi

for t in $LPATH/*;
do
    if grep -q lrc $t;
        then greadlink -f $t >> netease.list
    fi
done
