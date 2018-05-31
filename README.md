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
--headless: True/False 
	whether run in headless mode or note
--upper_bound: n 
	max number of reposts to make
--comment: True/False 
	whether repost with comment
--lyrics: True/False
	whether repost with lyrics or with random pre-set repost messages
```

## Check local lyrics file generate by NetEase Music
To check which of the local caches generate by NetEase Music are lyrics files:
```
bash ./checkLyrics.sh
```


## Generate txt file for lyrics

To convert lrc files to txt files:
```
python get_lyrics.py
```

This will generate txt files from lrc files listed in netease.list. Currently lyrics are stored using numbers.
- [ ] Need to find a way to get song titles

## TODO
- [x] Store Cookies
- [x] Check repost message length
- [ ] IP issues
- [ ] Get Page response
- [ ] Implement lyrics scrapper to update lyrics database
