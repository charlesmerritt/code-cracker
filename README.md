# code-cracker
This is a simple brute force program that reads through a dictionary txt file and automatically tries every password sequentially. 
No functionality for password lockouts, not tested on sites other than pastebin.co
REQUIRES GECKODRIVER.EXE TO BE PLACED IN PROJECT DIRECTORY IF USING WITH FIREFOX.

Admittedly it's not very fast, I would love to make it faster. I have another version of this program that is marginally faster, I'll add that one as a branch.

To use, simply place a dictionary file called list.txt in the project directory. This file will be most of the work, you can create list files using ophcrack on linux
or download them. Then in the source code, specify the link you want to attack. Then just run the program and have at it.
