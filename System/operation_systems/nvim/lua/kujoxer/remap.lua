vim.g.mapleader = " "
vim.keymap.set("n", "<leader>bv", vim.cmd.Ex)

vim.cmd('autocmd InsertLeave * write')

vim.api.nvim_set_keymap('i', 'zz', '<Esc>', {noremap = true})
