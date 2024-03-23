-- vim.cmd('autocmd InsertLeave * write')
vim.api.nvim_set_keymap('i', 'zz', '<Esc>', {noremap = true})

vim.g.mapleader = " "
vim.keymap.set("n", "<leader>bv", vim.cmd.Ex)

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

vim.keymap.set("n", "J", "mzJ`z")
vim.keymap.set("n", "<C-d>", "<C-d>z.")
vim.keymap.set("n", "<C-u>", "<C-u>z.")
vim.keymap.set("n", "n", "nz..v")
vim.keymap.set("n", "N", "Nz..v")

-- vim.keymap.set("n", "<leader>vwm", function()
--     require("vim-with-me").StartVimWithME()
-- end)
--
-- vim.keymap.set("n", "<leader>svwm", function()
--     require("vim-with-me").StopVimWithME()
-- end)
--

-- vim.keymap.set("", "", "")

