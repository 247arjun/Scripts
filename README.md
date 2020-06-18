# WindowsTaskSchedulerScripts
Scripts that can be added to Windows Task Scheduler tasks, for automatic execution on when certain conditions are met. When the PC enters a state that `triggers` a task, the `actions` associated with that task are completed.

# Setting up Task Scheduler tasks
1. Launch `Task Scheduler` from the Start Menu
2. `Create a Task` (from the right menu)
3. Name your Task - you cannot rename the task once it has been created.
4. Open the `Triggers` tab in the "Create Task" window, and add triggers that the Task Scheduler listens for - example: Workstation Lock will run the task when the PC is locked.
5. Open the `Actions` tab in the "Create Task" window, and add actions that the PC will run, when the task is triggered - example: powershell.exe invoked on a certain script.
6. (Optional) Review the `Conditions` and `Settings` tabs for any other settings of interest.
7. Click `OK` to save the task

# Scripts
## MutePC.ps1
This PowerShell script mutes the output volume on your PC.

## UnmutePC-CustomVolumeLevel.ps1
This PowerShell script unmutes the output volume on your PC, and sets its value at a custom level (default set to 10% of max).
