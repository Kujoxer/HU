-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'

  -- Telescope
  use {
    'nvim-telescope/telescope.nvim', branch = '0.1.x',
    -- or tag = '0.1.x', branch = '0.1.x'
    requires = { {'nvim-lua/plenary.nvim'} }
  }

  -- Rose-pine colorscheme
  use {
	  'rose-pine/neovim', as = 'rose-pine',
	  config = function()
		  vim.cmd('colorscheme rose-pine')
	  end
  }

  -- Treesitter
  use('nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'})
  use("nvim-treesitter/playground")
  -- Harpoon "Прикалывает файлы"
  use("theprimeagen/harpoon")

  -- Дерево изменений 
  use("mbbill/undotree")

  -- Git
  use("tpope/vim-fugitive")

  -- Lsp
  use {
      'VonHeikemen/lsp-zero.nvim',
      branch = 'v1.x',
      requires = {
          -- LSP Support
          {'neovim/nvim-lspconfig'},
          {'williamboman/mason.nvim'},
          {'williamboman/mason-lspconfig.nvim'},

          -- Autocompletion
          {'hrsh7th/nvim-cmp'},
          {'hrsh7th/cmp-buffer'},
          {'hrsh7th/cmp-path'},
          {'saadparwaiz1/cmp_luasnip'},
          {'hrsh7th/cmp-nvim-lsp'},
          {'hrsh7th/cmp-nvim-lua'},

          -- Snippets
          {'L3MON4D3/LuaSnip'},
          {'rafamadriz/friendly-snippets'},
      }
  }


  -- Comment

  use {
      'numToStr/Comment.nvim',
      config = function()
          require('Comment').setup()
      end
  }

-- Highlight TODOs, notes, etc. in comments
use {
  'folke/todo-comments.nvim',
  event = 'VimEnter',
  requires = { 'nvim-lua/plenary.nvim' },
  config = function()
    require('todo-comments').setup {
      signs = false
    }
  end
}

-- Collection of various small independent plugins/modules
use {
    'echasnovski/mini.nvim',
    config = function()
        -- Better Around/Inside textobjects
        -- Examples:
        --  - va)  - [V]isually select [A]round [)]paren
        --  - yinq - [Y]ank [I]nside [N]ext [']quote
        --  - ci'  - [C]hange [I]nside [']quote
        require('mini.ai').setup { n_lines = 500 }

        -- Add/delete/replace surroundings (brackets, quotes, etc.)
        -- - saiw) - [S]urround [A]dd [I]nner [W]ord [)]Paren
        -- - sd'   - [S]urround [D]elete [']quotes
        -- - sr)'  - [S]urround [R]eplace [)] [']
        require('mini.surround').setup()

        -- Simple and easy statusline.
        --  You could remove this setup call if you don't like it,
        --  and try some other statusline plugin
        local statusline = require 'mini.statusline'
        -- set use_icons to true if you have a Nerd Font
        statusline.setup { use_icons = vim.g.have_nerd_font }

        -- You can configure sections in the statusline by overriding their
        -- default behavior. For example, here we set the section for
        -- cursor location to LINE:COLUMN
        statusline.section_location = function()
            return '%2l:%-2v'
        end

        -- ... and there is more!
        --  Check out: https://github.com/echasnovski/mini.nvim
    end,
}

  -- -- Prettier
  -- use {
  --     'prettier/vim-prettier',
  --     run = 'yarn install --frozen-lockfile --production',
  --     ft = {'javascript', 'typescript', 'css', 'scss', 'json', 'graphql', 'markdown', 'vue', 'yaml', 'html'}
  -- }




end)
