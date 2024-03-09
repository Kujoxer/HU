#!/usr/bin/bash

# Здесь список команд для установки i3-wm и сопутствующих к нему программ соответственно 
# Выполни ./install_i3wm.sh для установки i3 и ...
#
#https://wiki.debian.org/i3
#If you want to install i3 minimally without useful packages, such as i3lock and i3status, use: 

# Базовые программы и утелиты
sudo apt install curl ranger npm;

# Собственно установка i3
sudo apt install i3 --no-install-recommends;
sudo apt install compton;
sudo apt install feh;

# Для работы буфера
sudo apt install xsel xclip;

# Без этих программ никак.
sudo apt install firefox;
