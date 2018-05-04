# WeiboHelper
Featuring auto-search, auto-refresh, and possibly auto reposting in the future.

To build and enable the project, open terminal, run
```
bash ./install.sh
```
## Repost
### Required file
1. config.txt/config_test.txt
Username and password saved in these two files. Using delimiter of "----".

E.g.:
MyUserName----MyPassWord

To run:
```
python main.py
```

## Check local lyrics file generate by NetEase Music
run
```
bash ./checkLyrics.sh
```


## Generate txt file for lyrics
This will generate txt files from lrc files listed in netease.list. Currently lyrics are stored using numbers.
- [ ] Need to find a way to get song titles
run
```
python get_lyrics.py
```

## TODO
- [ ] Store Cookies
- [x] Check repost message length
- [ ] IP issues
- [ ] Get Page response
