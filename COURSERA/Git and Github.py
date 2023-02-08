################################################
# GIT and GITHUB via Coursera
#
#
#################################################

# The git init command creates a new Git repository. In our case, it transformed the current directory into a Git repository. It can also be used to convert an existing, unversioned project 
# to a Git repository or to initialize a new, empty repository.

# Executing git init creates a .git subdirectory in the current working directory, which contains all of the necessary Git metadata for the new repository. 
# This metadata includes subdirectories for objects, refs, and template files. A HEAD file is also created which points to the currently checked out commit.

# SETTING up my local REPO

$ cd C:\Github
$ git init

# SETUP config to associate commits with an identity
#########################################################
# use "git config --list" to view all existing parameters
# use "git config --global --unset"  to unset a parameter
#########################################################
$ git config --global user.name "Tu Chung"  
$ git config --global user.email "tu.chung@iag.com.au"


###############
# Actually works only if PROXY is NOT set
# A push command will raise a prompt to authenticate in the browser
################
#  now configure to allow through proxy
$ git config --global http.proxy "http://proxy.auiag.corp:8080"
#
###############

###################
# Now create README
#
###################
# check status with "Git status"

$ git add README
$ git commit -m "Our first commit"

# "git diff README" can be used to view the changes
#  You can see the differences between the older file and the new file. New additions are denoted by green-colored text and a + sign at the start of the line. 
#  Any replacements/removal are denoted by text in red-colored text and a - sign at the start of the line.

# view all activity and commits using "git log"

#################
# REMOTE REPO
#################
# Now lets connect to our remote repo - https://github.com/tuchung23/Cheatsheets.git -  and push it
# use "git remote add origin https://github.com/tuchung23/Cheatsheets.git"

# to unlink a remote repo
$ git remote remove origin
# now to check
$ git remote -v

## Now push the README to the repo as it's already been committed!
$ git branch -M main
# this creates a "main" branch and goes to it. Though a "git init" already creates a default main
# This branch still points to the first commit 
$ git push -u origin main
# The cheatsheets repo will now have the README!!!!!
# "git push -u origin head"  will also work if head points to main

#####################
# Think of branches as LOGICAL OBJECTS with pointers to the original file WITH CHANGES
#
#####################
# Delete a branch
# git branch -d [name]
######################


###################
# Push a local branch to a remote branch
# 
###################
$ git branch -m "new_branch"
$ vi New_file
$ git add New_file
# now commit and point the new branch to this new commit
$ git commit -m "Commit New_file to the new_branch"
# push to the remote repo into a new branch called "new_branch"
$ git push -u origin new_branch
# now check all the branches on the remote repo
$ git branch -r
# we can now do a pull request on the remote GITHUB to merge it into the main origin repo


#####################
# Using git FETCH to syn local against remote origin
#  eg. on REMOTE , I updated the README file with new text, which is not in the local README
######################
$ git fetch        
or
$ git fetch origin
# This just fetches the contents into the LOCAL REPO which is the .git file
# check git status

#####################
# Using git PULL to syn local against remote origin
#  eg. on REMOTE , I updated the README file with new text, which is not in the local README
######################

$ git pull
# this will update the README file on local
# this command pretty much syncs LOCAL to that of REMOTE

###########################
# Revert back to a working version if something has broken
#
############################
$ git log
# get the commit id and check the messages to see the last working version
$ git revert [commit ID]

###########################
# MERGE a branch into the main/master
# 
# Make sure you checkout into the target branch first
############################
$ git checkout master
# switch to the target master branch first
$ git merge [branch]


###########################
# How to sync my entire local repo to my GITHUB repo called "study"
#
###########################
# Unitialise a repo to start over by:
# First, navigate to the local repository on your computer using the command line.
# Next, remove the git-related files and directories by running the command "rm -rf .git"
# This command will delete the .git directory, which contains all the information about the repository, including the commit history.
#
#################################

$ cd c:\github
$ git init
# Now add ALL the files under c:\github. This will include the README
$ git add .
$ git commit -m "Duplicating my local repo"
$ git branch -M main
# now link to remote "study" repo
# unlink any existin remote repo with 
$ git remote remove origin
$ git remote -v  # to check
# note that we are calling the remote repo "origin"
$ git remote add origin https://github.com/tuchung23/study.git
# now push ALL committed files to remote github
$ git push -u origin master     # or main. Depending on if you do it from the main branch or from a new branch
## The above steps 100% work to create a blank GITHUB repo of my local git
# 
###############################
# Now to sync it to my macbook air, we need to pull it down
#   
############################### 

$ cd Github   # on macbook
$ git clone https://github.com/tuchung23/study.git
# make changes on github directly or pushed from work laptop
# then just issue the git pull command to sync local to remote
$ git pull
# Visual source code will automatically update on MAC


##################
# 2/2/23 - Wanting to add a new local folder "MY PYTHON PROGRAMS"
#
##################
# $ git branch -M new_branch
# $ git add .
# $ git commit -m "My local python files"
# $ git push -u origin new_branch
# Then confirm pull request from main <- new_branch
# git branch -d new_branch

##################
# 2/2/23 - Updating the Git file from the main branch (not creating a new one)
#
##################
# $ git add Git\ and\ Github.py
# $ git commit -m "updated Git file"
# $ git push -u origin main   
# running this from the main local branch. As not a new branch, Pull Request not required




#######################################
# 7/2/23 - Scenario: 
# If github has a change and local git has a COMMITTED change
# A "git pull" will result in a MERGE CONFLICT
#
# A prompt will allow you to choose which version to accept or both
#
# If a github has a change and a local git has NOT COMMITTED
# The github change will appear in the local file
# 
########################################


#######################################
# 8/2/23 Scenario: 
# Should I do github changes from a branch or main?
#
# $ git add Git\ and\ Github.py
# $ git commit -m "updating Giithub"
# $ git push -u origin new_branch
# $ git checkout main
# $ git branch -d new_branch
#
# This will ask for a PR to be created to merge main <- new_branch
#
# ELSE
#
# Do it from the main branch
########################################
# My MERGE philosiphy:
# Since I am working on this myself and not in collaboration with others
# Just making the changes in main and pushing to origin is more than sufficient
#
# small and low risk changes can use the main branch
# major or more risky changes should use a branch
# 
# ######################################## 
# GIT FLOW using branches:
# create the new branch
# edit the file
# commit the file
# push it up for a PR
#
##########################################
# GIT Checkout will see the file in question with and without the new contents
#
# if i am on the newer_branch , I will see the additional edited changes
# if i "git checkout main" back to main branch, the additional text will disappear
# so the file essentially shows its non edited state 
# thats why switching between branches, it will remind you to commit first
##########################################


###########################################
# 8/2/23
# Should I create my commits from a branch?
#  $ git branch -M new_branch
#  $ git add Git\ and\ Github.py
#  $ git commit -m "updating Giithub"
#  $ git push -u origin new_branch
#  GITHUB will ask you to create a PR to merge main <- new_branch
#
# ELSE
# If i just commit from the main branch , there is no need for a PR
#
#
########################################
# My MERGE philosiphy:
# Since I am working on this myself and not in collaboration with others
# Just making the changes in main and pushing to origin is usually sufficient
#
# small and low risk changes can use the main branch
# major or more risky changes should use a branch
# 
# ######################################## 
# GIT FLOW using branches ( branches offer change security):
# create the new branch
# edit the file
# commit the file
# push it up for a PR
#
##########################################
# GIT Checkout will see the file in question with and without the new contents
#
# if i am on the newer_branch , I will see the additional edited changes
# if i "git checkout main" back to main branch, the additional text will disappear
# so the file essentially shows its non edited state 
# thats why switching between branches, it will remind you to commit first
##########################################
# Let's say I am working in a branch
# I edit my file and attempt to push it to remote origin but get the error 
# >> hint: Updates were rejected because the tip of your current branch is behind
# >>hint: its remote counterpart. Integrate the remote changes (e.g.
# >>hint: 'git pull ...') before pushing again.
# >> hint: See the 'Note about fast-forwards' in 'git push --help' for details.
#
# To keep the main branch safe of changes thus far
# I can use "git pull origin new_branch"  to pull changes to the branch only
# it will ask me about wanting to merge
############################################