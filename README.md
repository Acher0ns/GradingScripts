# GradingScripts
Welcome to the GradingScripts, home of all the scripts needed to grade the class GCIS-123/124!

Here is a brief guide for how to use the grading scripts for GCIS-123/124. In this quick guide, I’ll be going over how to use these scripts, each of there purposes, and how to use them for the first time. If you’re not a CA for GCIS-123/124, please stop reading. Or don’t. Not like this will be a very entertaining read.

![](https://user-images.githubusercontent.com/12210881/148610094-7e0d17f6-fb2f-457d-83b6-9b6ee35eb291.png)

# Prerequisites
 - Git 2.30 or newer
 - Python 3 or newer
 - PyGithub 1.5 or newer

Before we get started with other things, let’s make sure you have installed what you need to actually run the scripts.

If you don't have Python installed already, lets get that installed. Head to https://www.python.org/downloads/ and download the latest version, make sure to check the `Add Python 3.X to PATH` button if you're on Windows.

In order to make life easier, we’re going to start out with a tool called pip. After you installed Python, pip should already be on your computer, but in case it isn’t, go to this link and follow the instructions: https://pip.pypa.io/en/stable/installing/. It’s ok. I’ll wait for you to get back.

By now you should have pip (yay!). That means you’re on your way to being able to run the scripts at all! Now the next step is really easy. Now that you have pip, you just need to use it to install 1 package that the scripts require. Those command is as follows:

>pip install PyGithub

NOTE: If this doesn't work, try `python -m pip install PyGithub` or `python3 -m pip install PyGithub`

## How to get Github O-Auth token
Now that you have the package installed you can now run the scripts, huzzah! But wait, what’s this information you need? It doesn’t just work? Blasphemy!

Well, that’s what we’re going over next, what you should have access to for grading. We have 2 scripts, each of which does the same thing but can be run differently. Included is also a `tmp` folder. This folder contains config.txt which will be created after running the script for the first time and is used for storing information that should be consistent across the semester, primarily your Github Authentication token and the Github Organization name. There is also a logs.log file to help with troubleshooting potential issues.

You’re probably thinking, “What’s a Github Authentication token?”. Basically it’s a token generated by Github that can be used to login to your Github account through the scripts. Needless to say, if you plan on using these scripts, you need to make a token. So let’s go over that now.

Steps | Guiding Images
:-----: | :-----------:
Log into your Github account | 
Go to the upper right-hand corner of the screen, click on the icon with your profile picture, and then on the settings. | ![image](https://user-images.githubusercontent.com/12210881/148611772-d5618152-002c-496c-bcb0-1da258b392c5.png)
Click on the “Developer Settings” button at the bottom left. | ![image](https://user-images.githubusercontent.com/12210881/148611844-2cc60d7c-88db-4f99-9736-2cf8d8a3ae8a.png)
Click on the “Personal access tokens” button. | ![image](https://user-images.githubusercontent.com/12210881/148611927-20330743-23ed-4157-8bae-3aaf248b6275.png)
Click on the “Generate new token” icon in the top right of the screen (you may be prompted to log in again upon clicking this). | ![image](https://user-images.githubusercontent.com/12210881/148612005-b95ccbdf-ca0a-4726-891e-9c7129b4be5e.png)
Add a Note so you know what the token is being used for. You can set it to never expire or add a custom expiration date (NOTE: every time the token expires you will need to update it in `tmp/config.txt`). Make sure to give it the “repo” and “read:packages” permissions. | ![image](https://user-images.githubusercontent.com/12210881/148612633-8bcf62f2-7238-48bc-9853-ea45024b055f.png)
Scroll to the bottom and click the “Generate token” button. | ![image](https://user-images.githubusercontent.com/12210881/148612852-b67538b2-e267-4d65-8a0d-9c1926fd6cc4.png)
Copy this new token and put it somewhere safe (or put it into the script directly). NOTE: This will be stored in a file called `config.txt` in the `tmp` in the same location as the scripts. | !![image](https://user-images.githubusercontent.com/12210881/148612967-0d27ae1a-8e1f-4d49-b685-f7652fad883c.png)

Some extra information about these tokens, you won’t be able to see them again after you get out of the page, so paste it in another file, or to where the script prompts you. The script will store it so you only have to do this once. However, if you delete the token on Github, the token will be rejected and you’ll need to delete or edit the config.txt file in order to be able to use them again. The script will give you an error if you use an invalid token.

## Get Organization Name
The next thing you’ll need to do is get the organization name from Github. This is relatively easy compared to making a personal access token. Once you’re added to the organization, you should be able to access it on the left of the Github homepage.

![image](https://user-images.githubusercontent.com/12210881/148613466-f5685d56-e503-46fe-9a6b-a5fceacf6a7f.png)

In order to ensure you spell it right, it’s recommended you click on the organization and copy the organization name from the link at the top of your browser, and then enter it into the script when prompted.

![image](https://user-images.githubusercontent.com/12210881/148613569-b098d878-9362-4349-bfed-d6b06f46872e.png)

## Get Class Roster

Finally we will be getting a classroom roster csv file from Github Classroom in order to make grading easier. This will allow the script to change github usernames to peoples actually usernames. This is option ofcouse but is highly recommended so that you don't have to clone every repo from the organization every time.

Steps | Guiding Images
:-----: | :-----------:
Go to https://classroom.github.com/classrooms and login if needed | 
Go to your classroom/organization for the semester | ![image](https://user-images.githubusercontent.com/12210881/148614399-e52af804-ea5e-47dc-8468-b94c52117579.png)
At the top click on the `Students` tab | ![image](https://user-images.githubusercontent.com/12210881/148614455-a2eb28f0-5920-4564-8f64-91d1ef67311f.png)
Then under classroom roster, click `download` | ![image](https://user-images.githubusercontent.com/12210881/148614534-833eb319-1c4a-49e4-b6d7-960cb3700a27.png)
Then click `Download without group names` | ![image](https://user-images.githubusercontent.com/12210881/148614634-e0e64e82-d8e0-4810-a174-dce89e47e549.png)

And Tada! You now have a CSV file containing all the students for your classroom. I recommend opening the CSV file to delete the entries of students you will not be grading.
I also recommend placing the classroom roster file into the `tmp` folder.

# How to use clone_repos.py
![image](https://user-images.githubusercontent.com/12210881/148616251-1b2a0714-5367-4d17-87c6-f412db4e9809.png)

This is a typical first running of the `clone_repos` script. You put in your Github auth token and the organization name first. Then enter the relative path to the classroom roster and state whether this path should be saved. Then state the parent folder where you want your cloned repos to go. Beyond that, you need to enter the assignment name. This can be found on the left-hand side of the organization.

![image](https://user-images.githubusercontent.com/12210881/148616483-f501ad70-77bb-45f0-a432-e3fe278efea3.png)

Next, you enter the day that it’s due in the proper format (‘yyyy-mm-dd’, ex: 2020-08-18). After that the time that the assignment is due (so it only gets the commits before that time) in 24 hour format (ex: ‘23:59’ for 11:59pm).

After you enter all the information, the script will clone all the repositories and put them all into the folder specified. Inside will be a folder named after the assignment name and the date/time specified.
![image](https://user-images.githubusercontent.com/12210881/148616913-aa034432-6ba8-4791-b99d-c5b0297f6ace.png)

## What does the output mean
A typical run of the clone_repos.py would look something like this.
![image](https://user-images.githubusercontent.com/12210881/148617201-0bee5f20-2e05-42e4-8229-f129eaa894f2.png)

The top contains the prompts. The middle contains output of the script running and can contain very useful information about where student repos are being cloned to, and the bottom show a summary of what the script did.

It is import to pay attention to the bottom because errors can occur while the script is running, causing a student to be skipped. Some common example of why a student would be skipped is because they accepted the assignment after the due date/time, their repo contains an invalid filename, or they didnt accept the assignment at all.

You may also notice "Found average lines per commit for 13/13 repos." If you look in the output folder you will see an averageLines.txt file. This file contains the average number of lines of code a student writes between each commit. It may be helpful for grading... idk.

# How to use clone_script.py
If you're more comfortable with command line or need to clone multiple assignments in bulk `clone_script.py` may be more useful.

clone_script.py can be from from command-line using `./clone_script.py ...` or `python clone_script.py ...` or `python3 clone_script.py ...` of couse replacing the `...` with your arguments. Here is the scripts usage
```
Usage: ./cloneScript.py <assignment name> <due date> <due time> [folder name]
    <assignment name>:    Set assignment name. Same as repo prefix in organization
    <due date>:           due date of assignment in yyyy-mm-dd format.
    <due time>:           due time of assignment in HH:MM 24hr format.
    [folder name]:        OPTIONAL. Changes output folder name from default assignment name
```


## Congratulations! You’ve either read or skimmed through my entire guide. May your grading be easy and enjoyable thanks to these scripts! 
