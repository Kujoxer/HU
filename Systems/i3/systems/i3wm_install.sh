#!/usr/bin/bash

## Здесь список команд для установки i3-wm и сопутствующих к нему программ соответственно 
# https://wiki.debian.org/i3

# Базовые программы и утилиты
sudo apt install curl git ranger npm;

# Собственно установка i3
## If you want to install i3 minimally without useful packages, such as i3lock and i3status, use:
sudo apt install i3 --no-install-recommends;
sudo apt install compton;
sudo apt install feh;

# Для работы буфера
sudo apt install xsel xclip;

# Без этих программ никак.
sudo apt install firefox;
