# parupager.py
Crappy python script to parse `paru`'s output into something more readable when searching for packages

## Usage

    pacman -Ss <search> | parupager.py

## Issues

Unfortunately, parupager currently does not work with a pager, because it uses `os.get_terminal_size()` which doesn't like being piped anywhere.\
I don't know if I will fix this. This project was mostly because I wanted to have *something* better than `paru -Ss`
