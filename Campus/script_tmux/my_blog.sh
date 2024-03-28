#! /usr/bin/zsh

SESSION_NAME="blog"

# Check if the session already exists
if tmux has-session -t $SESSION_NAME 2>/dev/null; then
    echo "Session $SESSION_NAME already exists. Attaching to it."
    tmux attach-session -t $SESSION_NAME
else
    # Create a new session and name it
    tmux new-session -d -s $SESSION_NAME

    # Send a command to the first pane to open vim with the file 61_day.md
    tmux send-keys -t 1 'vim ~/Sync/Processes/Designing/my_blog.md' C-m

    # Create a new window and open ranger in it
    tmux new-window -t $SESSION_NAME:2 -n ranger -c ~/Sync/Processes/Designing/

    tmux send-keys -t $SESSION_NAME:2 'ranger' C-m

        # Attach to the created session
    tmux attach-session -t $SESSION_NAME
fi

