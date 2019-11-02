# Image Steganography :sunrise_over_mountains: <-> :hash:

This repository contains an image with a hidden ASCII message, the python code used to extract the message and some thoughts about the process of the group's investigation and reporting. 

</br>

---
## Requirements
- Docker :whale: [*Optional for running python*]
- Python <img src="./images/python.png" height="25">
- `pillow` for Python 3

</br>

---
## Getting Started
> Environment setup

Start by cloning down this repository which contains the [imgSteganography.py]() script, together with the manipulated image [Stego.png](). </br>
Installing **pillow** can be done by executing `pip3 install pillow` on your favourite terminal.
 
If you **don't** have **python3** on your system, make sure your docker is running and then execute the following command:
`docker run -it --rm davi7816/pybuntu`. </br>
This will give you a running instance of ubuntu with all the necessary applications installed (python, git, nano, wget and unzip).</br>
After that follow the steps listed at the beginning of this sub-sections.

</br>

> Execution

Navigate to the cloned directory. </br>
In order to run the program you should run `python3 imgSteganography.py`.

</br>

> Result

The output presented would be the hidden message stored in the image, and will be displayed like so:
**"Congratulations, this is the secret message of the UFO class! (no, not 42)"**.

</br>

---
## Investigation and Reporting
### Search history
A list of all Google queries made to solve this assignment, including timestamps and all URLs of the visited pages can be found in [historyCSV]() file.

</br>

### 3 biggest stumbling blocks 
In the following paragraphs you can find what we came across and our reflection on why these were problematic:

**Finding example code for looping through an image pixels that wouldn’t work with our current image.**
> This was problematic because it prevent us from proceeding with the exercise. The search queries we were using weren’t returning any valuable results until we found the root cause of the error, which enabled us to perform more targeted queries. This resulted into learning that it was necessary to also receive the ALPHA value from each pixel, in conjunction to the 3 color channels.
</br>

**Extracting the least significant bit from the red color channel of each pixel.**
> In order to comply with the guidance received in class, it was important that we could extract the lsb from the red channel. For this process to be considered completed, we had to convert the integer value from the R channel to a binary, from which we could then extract the last bit. After some research we figured that the easiest way would be to convert the binary into a string and then extract last character.
</br>

**Getting gibberish as an output**
> Once the collection of bits had been converted to chars, we noticed the output provided on the screen had no valid English expressions, therefore, we went back to the drawing board to figure out what could’ve been wrong with our methods. An idea that came forward was that our sequences of 8 bits (ASCII-character length) might need to be reversed, so that a different character would be printed out. Unfortunately, this approach didn’t resolve in a readable msg either. A decision was made to try the same processing (reversed & non-reversed) with the remaining color channels. This led us to finding the message “Congratulations, this is the secret message of the UFO class! (no, not 42)” within the blue channel using the reversed method.

</br>

### Diaries
The following section contains our *“every 30 min”* diaries for the 1 hour we spent solving the task at hand.

#### Entry 1 - Doing implementation to read the needed value from an image.
* **How long did it take to do?** - 30 mins.
* **What misunderstandings arose?** - not using the appropriate implementation for an image with an Alpha channel, as well as trying to convert from a bitarray when we just had a normal array with each binary number as a character.
* **Which micro-experiments were done?** - trying different variable names as 1 of them appeared to be reserved as a keyword; trying code to join array of strings into an integer; trying different approaches to get the last character of a string.
* **Which false leads were taken?** - the first code example that we found for manipulating image data didn’t account for the fact that this image had an Alpha channel and therefore errors arose from it. The misunderstanding that we were dealing with a string array then a bitarray.

#### Entry 2 - Try to get anything else than gibberish.
* **How long did it take to do?** - 20 mins.
* **What misunderstandings arose?** - the way that reversing of an array functions in python.
* **Which micro-experiments were done?** - reversing the string array containing the sequence of 8 bits representing an ASCII char; checking what would result from using the other color channels.
* **Which false leads were taken?** - the exercise description mentioned that the message was hidden on the red channel which prevented us from coming up with other implementation ideas faster.

</br>

### Reflection
**Which aspect of the exercise was taking you the longest time to solve?** 
> The first 30 mins (check diary) since we were brainstorming using pen and paper and then challenging ourselves with a language we don’t use daily to implement the conclusions we’d gathered from the brainstorm.
</br>

**Which part of the exercise was side tracking you the most (which dead-ends did you pursue)?**
> The deceiving description that was provided as guidance to accomplish the assignment. The wrong channel was mentioned which led to the team’s wrong assumptions. 
</br>

**What was the most helpful information you came across (it could be someone else helping you)?**
> All the search queries we did helped us to improve our implementation bit by bit, therefore all of them were equally important to the fulfillment of the exercise. 
</br>

**How can you avoid those problems in the future, and how can the helpful resources help you in the future?**
> Don’t discard any outside-of-the-box thinking because of a task guide. It is always good to guide yourself with the description but you shouldn’t give up before look at other possibilities.

</br>

___
> #### Assignment made by:   
`David Alves 👨🏻‍💻 ` :octocat: [Github](https://github.com/davi7725) <br />
`Elitsa Marinovska 👩🏻‍💻 ` :octocat: [Github](https://github.com/elit0451) <br />
> Attending "Investigation & reporting (UFO)" course of Software Development bachelor's degree
