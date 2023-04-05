### Extract first page and store in `tempx.pdf`
`ls *.pdf| grep -v '\FirstPage.pdf$'| xargs -n 1 | awk '{print $1" "NR}'|xargs -l bash -c 'pdftk A=$0 cat A1 output temp$1.pdf'`
### Merge first pages together
`pdftk temp*.pdf cat output JournalFirstPage.pdf`
or `pdftk temp*.pdf cat output ConfFirstPage.pdf`
### Remove temp files
`rm temp*.pdf`