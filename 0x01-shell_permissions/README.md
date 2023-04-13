# 0x01. Shell permissions
## My name is Betty
This script simply switches the current user to the user betty using the su command

## 1-who_am_i
This is a script used to print the effective username of the current user using the id command

## 2-groups
This script prints all the groups the current user is part of.

## 3-new_owner
The script here changes the owner of the hello file from root to betty, using the chown command.

## 4-empty
Here is a script that creates an empty file named hello, and i used the touch command.

## 5-execute
This script would give the execute right to the hello file using chmod command.

## 6-multiple_permissions
 This is the script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello. The permissions where specified using symbolic mode.

## 7-everybody
This script adds execute permission to everyone, since we are not allowed to use "," i had to use the absolute mode while making sure to keep other permissions as they are for the hello file while adding the execute files only to them all.

## 8-James_Bond
This script gives permission all permissions only to others while owner and group is denied all permission and it forms the code in the movie james bond 007 hence the name of the script

## 9-John_Doe
This script gives all permissions to the owner and only read and execute to the group while it gives only write and execute to others.

## 10-mirror_permissions
This script would always set the file mode of the hello file to that of the olleh file.

## 11-directories_permissions
this script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. But will not change that of regular files.

## 12-directories_permissions
This script creates a directory my_dir and automaticaly assigns 751 permission mode

## 13-change_group
This script change only the group owner to school.

## 100-change_owner_and_group
This script changes the owner and group owner of all files and folders in the folder path specified.

## 101-symbolic_link_permissions
This is a script that changes the owner and the group owner of _hello to vincent and staff respectively.

## 102-if_only
This is a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.

## 103-Star_Wars
This is a script that will play the StarWars IV episode in the terminal.