from subprocess import call
from sys import argv

#python time.py testes.txt
git add testes.txt
git commit -m "argv-autoupdate"
git push origin master

call(["git" "add" "*"])
call(["git" "commit" "-m" "argv"])
call(["git" "push" "origin" "master"])
