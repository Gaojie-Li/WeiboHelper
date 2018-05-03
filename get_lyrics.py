import json
from pprint import pprint

with open("netease.list","r") as file:
    sCount = 1
    for _ in file:
        data = json.load(open(_.strip()))
        # print(data)
        lyrics = data["lrc"]["lyric"].split("\n")
        i= 1
        outfile = open("lyrics/{0}.txt".format(sCount),"w")
        for l in lyrics:
            l = l.split("]")
            if len(l) > 1 and len(l[1]) > 0:
                if ":" in l[1] or "：" in l[1]:
                    continue
                else:
                    outfile.write("{0}. {1}\n".format(i, l[1]))
                    i += 1
        sCount += 1
        # print("="*30)
        # print("NEXT SONG")
