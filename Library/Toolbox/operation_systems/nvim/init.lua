require("kujoxer")

vim.cmd('autocmd InsertLeave * write')

vim.api.nvim_set_keymap('i', 'jj', '<Esc>', {noremap = true})

vim.opt.wrap = true

