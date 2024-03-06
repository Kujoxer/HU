# Установка и настройка Neovim с прицелом на Debian 12

Особенность установки в том что Neovim будет установлен в /usr/bin.
Установка будет произведена из AppImage. Одна из причин - отсутствие свежей
версии Neovim в репозитории Debian.

Да, и сложно это будет назвать установкой... Просто скачаю AppImage Neovim,
поменяю его название на Vim и закину в /usr/bin. Это делается для того,
что бы в моей системе как бы существовал vim, хотя по факту это будет nvim. На 
случай если системе вдруг вздумается дергать vim для открытия каких либо файлов
по умолчанию. И как то набирать команду vim привычнее, чем nvim. 

## Start

Первым делом сносим vim который предустановила Debian 12
```shell
sudo apt autoremove --purge vim;
```

Ах, да - сразу установим зависимости, которые нам потом понадобятся для 
настройки конфигурации Neovim
```shell
sudo apt install fuse curl git npm yarn;
```

Скачиваю AppImage и проделываю с ним некоторые манипуляции, устанавливаю в /usr/bin
```shell
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage;
chmod u+x nvim.appimage;
mv nvim.appimage vim;
mv vim /usr/bin;
```

Осталось экспортировать настройки в .bashrc для удобства. Пусть наш редактор используется везде по умолчанию!!
```shell
sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 100;
sudo update-alternatives --set editor /usr/bin/vim;
echo "export EDITOR=/usr/bin/vim" >> /home/$USER/.bashrc;
source /home/$USER/.bashrc;
```

## Configuration 

Omg ...







