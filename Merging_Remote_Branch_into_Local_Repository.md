
# Merging Remote Branch into Local Repository

* See the following links for more info:
  * https://stackoverflow.com/questions/1425892/how-do-you-merge-two-git-repositories
  * https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line

## Note on Cloning Github Repository

* Make sure that you create your own personal branch on the repository and this is what you work on. Make changes on your local machine which you commit to the remote version of this branch. Do a pull request to move changes from your branch of the repoistory to the main branch which contains the stable, best version of the code.

* **!!!You DO NOT need to run `git init` if you are cloning a github repository. This will just created nested git projects. `git clone` automatically creates the github project and does what you need it to do to link to to the remote repository.

### Look into Difference between Branching and Forking

* When is it good to Branch a github repository
* When is it good to Fork a github repoistory
  

## Example of Merging 

**Want to merge branch from remote repository project A into local repository B. "/path/to/project-a" would be the url from github for that the Project A repository.

```{Linux}

cd path/to/project-b
git remote add project-a /path/to/project-a
git fetch project-a --tags
git merge --allow-unrelated-histories project-a/master 
git remote remove project-a

```

## How Make Sure No Merge Conflict and Fix Ones if There Are

* Use `git status` to check for conflicts
* Use `git add` to make sure git is tracking new / renamed files
* Use `git rm` to remove files
* Use `git commit -m <message>` to commit any changes before continuing merge process
