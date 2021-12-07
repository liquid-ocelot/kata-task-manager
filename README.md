# Task Manager kata

*Goal: practice TDD and clean architecture by implementing a task manager*

# Specification

Each task is made of

* A description
* A number that identifies it
* A status "done" or "to do"

The task manager must start an interaction loop where the user can enter
some commands, like this:

* `+ description>` Add a task
* `- <id>` Remove the task matching the given id
* `x <id>` Set the status of the task matching the id to "done"
* `o <id>` Set the status of the task matching the id to "to do"
* `q` Exit the interaction loop

At each step, the task manager must show the list of tasks:

Here's an example of using the task manager:

```
No task yet
>>> + Learn Python
1 [ ] Learn Python
>>> + Learn TDD
1 [ ] Learn Python
2 [ ] Learn SQL
>>> x 1
1 [x] Learn Python
2 [ ] Learn TDD
>>> q
Bye!
```

# Instructions

* Follow the TDD rules as close as possible to implement the
  above specifications.

* *Note*: you can assume the user only enters *valid inputs*.

* Use an iterative process - going through the following steps, in order:

1.  Parse user input (+, -, x, o)
2.  Update the task list
3.  Display the tasks
4.  Run the interaction loop

* Feel free to use source control and make a commit at the
  end of each refactor phase.

# Notes

* The task list does not need to be *persistent* - it's OK if the task
  manager always starts empty
