-- global options
vim.o.shell = "sh"  -- set shell to sh because we need POSIX compliance for some features

-- window-local options
vim.wo.number = true  -- current line will show the absolute line number
vim.wo.relativenumber = true  -- other lines will show relative line numbers

-- map ctrl c to copy to clipboard  
vim.api.nvim_set_keymap("v", "<C-c>", "\"+y", {noremap=true})

-- map jk to go to normal mode from insert mode
vim.api.nvim_set_keymap("i", "jk", "<Esc>", {})
