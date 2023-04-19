## Abstract submission count down ##
https://www.timeanddate.com/countdown/generic?p0=4214&iso=20180426T15&year=2018&month=4&day=26&hour=15&min=0&sec=0&msg=03%3a00%20-%20Apr%2026,%202018%20%28PDT%29

### Font embeding and greyscale pdf
make embeded
make greyscale
make check


### Merge bib files
bibtool -s -d Chapter1.bib total2.bib >total3.bib

### .tex to .txt for grammerly checking
detex ../2_Task1/3_probdef.tex > test.txt

### draw.io to eps
Save as PDF or PNG
#### PNG
sam2p in.png 
#### PDF
pdf2ps MPTCP-Flow.pdf
ps2eps -f MPTCP-Flow.ps

# GIT References #
## First time pull from GitHub website ##
```
git clone https://github.com/subhrendu1987/2016-mptcp-sandip
```
## View local changes ##
```
git status
```
## Commit and push data to server ##
```
git commit -a --allow-empty-message -m ''
git push
```
## Pull from server ##
```
git pull
```

## Git conflict resolution ##
Accept server copy
```
git merge --strategy-option theirs
git pull -Xtheirs
```
Upload local copy
```
git merge --strategy-option ours
git pull -Xours
```
# New repository creation #
Create a folder <PROJECTNAME>
