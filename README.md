Add this to your .bashrc:
```bash
alias cp='<ADD_PATH_HERE>/custom-linux-commands/cp_custom.py'
alias rm='<ADD_PATH_HERE>/custom-linux-commands/rm_custom.py'
```
Additionaly you may have to change the execute permissions on the files like this:
```bash
cd custom-linux-commands
chmod +x cp_custom.py
chmod +x rm_custom.py
```

