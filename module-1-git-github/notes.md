# Module 1 — Git & GitHub

**Student:** Delfin, Cherrie Mae S.
**Date:** 09/27/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a tool used to track changes made to files in a project. It allows me to save different versions of my work, which makes it easier to review changes and recover an earlier version when needed.

GitHub is an online platform where Git repositories can be stored and managed. Git is mainly used to track and manage changes on my computer, while GitHub allows me to store, share, and collaborate on the project online.

---

## Key vocabulary (in your own words)

- repository: A location where the project files and their changes are stored and managed.
- commit: A saved record of changes made to the project, usually with a message describing the changes.
- branch: A separate version of a repository where changes can be made without directly affecting the main branch.
- push / pull: Push sends changes from the local repository to GitHub, while pull gets changes from GitHub and brings them to the local repository.
- pull request: A request to add the changes from one branch to another branch after the changes have been pushed to GitHub.
- merge conflict: A situation where Git cannot automatically combine changes because different changes were made to the same part of a file.

---

## Walking through what I did

First, I set up my Git username and email using the git config commands, although I do not remember the exact commands I used at the time. I then connected my local project to my GitHub repository and checked the remote connection. After that, I checked the available branches and created a new branch named mae. I pushed the new branch to GitHub, added my changes, created a commit, and pushed the changes to my branch. Finally, I opened a pull request on GitHub.

```
git config --global user.name "maesdlfn" 
git config --global user.email "cmaedelfin@gmail.com" 
git remote add origin "repo url" 
git remote -v 
git switch -c mae 
git push -u origin mae 
git add . git commit -m "Commited" 
git push

```

---

## A mistake I made (or one I want to avoid)

One thing I found confusing was remembering which Git command to use for each step. I understood the general process, but I sometimes had to check the commands again, especially when creating a branch, pushing it, and committing changes. This taught me that understanding what each command does is important instead of only memorizing the commands.
---

## How this connects to something else

Git is related to the coding projects and activities I work on because it helps me keep track of the changes I make. Instead of manually keeping different copies of my project, I can use commits and branches to organize my progress. This can also be useful when working with other people on the same project.