# - Почисти систему от старых конфигов nvim, vim
# - Установка nvim в debian 12 ➡️ Install neovim


## 1. УСТАНОВКА
``` shell
sudo apt install curl git npm;
mkdir ~/.config;
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage
chmod u+x nvim.appimage
```

## 2. НАСТРОЙКА
``` shell
./nvim.appimage --appimage-extract
./squashfs-root/AppRun --version
```

## 2.1 Optional: exposing nvim globally.
``` shell 
sudo mv squashfs-root /
sudo ln -s /squashfs-root/AppRun /usr/bin/vim
```


## 0. В ИТОГЕ nvim как бы vim 🙈
[Neovim-Wiki](https://github.com/neovim/neovim/wiki/)

# Атсюдова ...

## Раз 

``` shell
cd ~/.config
git clone git@github.com:Kujoxer/nvim.git
```

## Два

``` shell 
git clone --depth 1 https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/start/packer.nvim
```

## Три
    В nvim редакторе набрать =:PackerInstall=.
    В результате должно получиться:
        1. Никаких ошибок нету;
        1. Манеджер плагинов Packer - исправно работает;
        1. У нас первоначальная простая структура nvim конфигурации.


## Plugins install
### Telescope 

> https://github.com/nvim-telescope/telescope.nvim

``` lua
use {
    'nvim-telescope/telescope.nvim', tag = '0.1.5',
        -- or                            , branch = '0.1.x',
        requires = { {'nvim-lua/plenary.nvim'} }
}
```

### Цветовая схема rose-pine
https://github.com/rose-pine/neovim

``` lua
use({ 
        'rose-pine/neovim', as = 'rose-pine',
        config = function()
        vim.cmd('colorscheme rose-pine')
        end
})
```


### Nvim-Treesitter для раскраски кода

``` lua
use('nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'})
use("nvim-treesitter/playground")
```


### Harpoon

https://github.com/ThePrimeagen/harpoon/tree/harpoon2

``` lua
use {
    "ThePrimeagen/harpoon",
        branch = "harpoon2",
        requires = { {"nvim-lua/plenary.nvim"} }
}
```


### Дерево изменений 
https://github.com/mbbill/undotree?tab=readme-ov-file#download-and-install

``` lua
use("mbbill/undotree")
```


### Плагин для Git
https://github.com/tpope/vim-fugitive

``` lua
use("tpope/vim-fugitive")
```


### Lsp 
> https://github.com/VonHeikemen/lsp-zero.nvim

``` lua
use {
    'VonHeikemen/lsp-zero.nvim',
        branch = 'v3.x',
        requires = {
            --- Uncomment these if you want to manage the language servers from neovim
            {'williamboman/mason.nvim'},
            {'williamboman/mason-lspconfig.nvim'},

            -- LSP Support
            {'neovim/nvim-lspconfig'},
            -- Autocompletion
            {'hrsh7th/nvim-cmp'},
            {'hrsh7th/cmp-nvim-lsp'},
            {'L3MON4D3/LuaSnip'},
        }
}
```


## Автосохранение по нажатию `Esc`

``` lua 
vim.cmd('autocmd InsertLeave * write')
```


# Source
### По мотивам thePrimeagen
> https://youtu.be/w7i4amO_zaE?si=NT4aaByC_C-_-p0k

### Установка менеджера плагинов
> https://github.com/wbthomason/packer.nvim 

#### Packer
> https://github.com/lewis6991/pckr.nvim



