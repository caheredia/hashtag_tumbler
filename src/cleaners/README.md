# Workers 

This workers are used for pruning the database of deletable hashtags. 

They do this by: 
- fetching a list of all unique tags, gouped by them themes and groups. 
- Sums the voting tables, if deletes outnumber keeps and use, then delete hashtage from hashtage table.
- does this process on a rotating process. 