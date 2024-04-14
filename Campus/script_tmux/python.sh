#! /usr/bin/zsh

SESSION_NAME="python"

# Check if the session already exists
if tmux has-session -t $SESSION_NAME 2>/dev/null; then
    echo "Session $SESSION_NAME already exists. Attaching to it."
    tmux attach-session -t $SESSION_NAME
else
    # Create a new session and name it
    tmux new-session -d -s $SESSION_NAME

    tmux send-keys -t 1 'cd ~/Sync/Python/' C-m

    # Send a command to the first pane to open ranger
    tmux send-keys -t 1 'ranger' C-m

    # Rename the window to "ranger"
    tmux rename-window -t $SESSION_NAME:1 'ranger'

    # Attach to the created session
    tmux attach-session -t $SESSION_NAME
fi

