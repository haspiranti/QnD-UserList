# QnD-UserList
Quick and dirty username wordlist generation tool 

This is a tool that takes either a single name or a list of names.
The script parses the names in a variety of ways that are common for usernames.

Example:
```
python3 gen-users.py -f names.txt
python3 gen-users.py -n "John J Smith"
Output file saving to usernames.txt

# Contents of usernames.txt
John
Smith
JohnSmith
John.Smith
JSmith
J.Smith
JohnS
John.S
SmithJohn
Smith.John
SmithJ
Smith.J
SJohn
S.John
JJSmith
JJ.Smith
JohnJSmith
John.J.Smith
JohnJSmith
John.J.Smith
John-Smith
J-Smith
John-S
Smith-John
Smith-J
S-John
JJ-Smith
John-J-Smith
John-J-Smith
John_Smith
J_Smith
John_S
Smith_John
Smith_J
S_John
JJ_Smith
John_J_Smith
John_J_Smith
```
