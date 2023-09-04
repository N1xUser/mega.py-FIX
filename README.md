# mega.py-FIX
The mega.py project https://pypi.org/project/mega.py/ has some issues that the owner didn't fix, this tool will fix some of them

Fix list:
 - Asyncio / Tenacity -> Make it work with newer versions of Python
 - Temporary output files mega.py, now it will finish downloading the files instead of an infinite loop.

Characteristics:
 - Create a backup file for each modified file (2)
 - If a problem occurs while importing the libraries to get the directory, it will go to the paths using native libraries

I know, it is spaghetti code but i don't care, i was boring of make the modifications manually every time i had to update my computer or install python again
