#Step 25: Bash/shell basics — navigation, piping, grep, chaining commands
#TODO comments for grep 
# pwd          # print current directory
# ls -la       # list all files, including hidden, with details
# cd ~/aqa-portfolio    # change directory
# cd ..        # go up one level
# cd -         # go back to previous directory

# ls -la | grep ".py"        # list files, filter for .py files only
# cat test_run.log | grep ERROR    # show only lines containing ERROR
# history | grep pyenv        # search your command history

# command1 && command2    # run command2 ONLY IF command1 succeeded
# command1 ; command2      # run command2 regardless of command1's success
# command1 || command2    # run command2 ONLY IF command1 FAILED

#grep -r "TODO" .          # recursively search all files for "TODO"
#find . -name "*.py"        # find all .py files from current directory down
#wc -l file.txt              # count lines in a file
#head -20 file.txt           # first 20 lines
#tail -20 file.txt           # last 20 lines
#tail -f test_run.log       # follow a file live as it's written (great for watching logs in real time)

#echo "test" > output.txt     # write (overwrite) to file
#echo "more" >> output.txt    # append to file
#command 2>&1                  # redirect errors (stderr) to same place as normal output (stdout)

#Step 26: Git branching strategy — feature branches, pull requests, code review etiquette
#Changes to push from a feature branch to main

#Step 27: README.md — structure, badges, setup instructions
