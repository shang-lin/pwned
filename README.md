pwnedornot.py checks if your password as been exposed in one of the data breaches 
archived on https://haveibeenpwned.com. 

To use, clone the git repo, enter, the pwned directory, and run pwnedornot.py. When 
prompted, enter the password you want to check and hit the Enter key. The password 
will not be echoed on the command line.

pwndornot.py will send the first five characters of the SHA1 hash of the password
to the haveibweenpwned.com API. The API will return a list of password hashes from 
the data breaches database that start with the same five characters. pwnedornot.py will
look for your password in this list. If there is no match, then congratulations! Your 
password has not been exposed, at least in these data breaches. If it is on the list,
then pwnedornot.py will tell you how many times it has been exposed. You should change
this password ASAP if you are still actively using it. 

