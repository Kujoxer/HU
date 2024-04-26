#! /usr/bin/zsh
SESSION_NAME="vim"

# Check if the session already exists
if tmux has-session -t $SESSION_NAME 2>/dev/null; then
    echo "Session $SESSION_NAME already exists. Attaching to it."
    tmux attach-session -t $SESSION_NAME
else
    # Create a new session and name it
    tmux new-session -d -s $SESSION_NAME

    tmux rename-window -t $SESSION_NAME:1 'ranger'


    # Send a command to the first pane to open ranger

    tmux send-keys -t 1 'cd ~/.config/nvim/' C-m
    tmux send-keys -t 1 'ranger .' C-m

# Create a new window and open vim in it
    tmux new-window -t $SESSION_NAME:2 -n vim
    # Open file in second pane for editing
    tmux send-keys -t 2 'vim ~/.config/lua/kujoxer/set.lua' C-m

    # Rename the window to "vim"

    # Attach to the created session
    tmux attach-session -t $SESSION_NAME
fi
