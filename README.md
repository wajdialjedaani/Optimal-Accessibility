# Optimal Accessibility

## Index
* [Project Ojectives](#project-objectives)
* [Project Details](#project-details)
* [Git Strategy](#git-strategy)
* [Testing](#testing)

## Project Objectives
### Overall objective
We aim to provide designers with a tool to assess the accessibility of their work 
and provide clear, concise, and helpful feedback to improve the accessibility of their work.

### How?
After the digital image is processed, the user will be given five individual scores rating 
them on color, text confidence level, text color, text size, and overall image score. 

#### Color
The image's color score is measured by taking the primary and secondary colors and 
comparing the contrast between the two colors—the more significant the color difference, 
the higher the color score. 

#### Text Confidence Level
The text recognition software generates the score and depends on a wide range of variables. 
For more information about the text recognition software used for this project, 
click [here](#to-be-determined-----text-recognition).

#### Text Color
Similarly to the image's color score, the text color score is measured by taking the 
difference between two colors—the color of the text and the color immediately surrounding 
the text. Moreover, the greater the contrast between these colors, the higher the text 
color score.  

#### Text Size


#### Overall Score

## Project Details
###  Our environments 
```json
   "production branch": "main",
   "current tag" : null,                                                          
```

### Project dependencies

```json
    "python" : "3.11.*",
    "unittest" : "Unit testing framework",
```

#### Unittest --- Unit testing framework
The [unittest](https://docs.python.org/3/library/unittest.html) unit testing framework 
was originally inspired by JUnit and has a similar flavor as major unit testing frameworks 
in other languages.  

It supports:  
* test automation 
* sharing of setup and shutdown code for tests
* aggregation of tests into collections
* independence of the tests from the reporting framework


#### (to be determined) --- Text Recognition
This library has yet to be determined.

### The repository's file structure
```
/(root)
|
|__ .github
|    |
|    |___ workflows # github actions scripts
|
|___ assets # images or any other need non-code assets
|
|___ src # source code for the project

```

## Git strategy
### Commit messages
Regularly consist of two parts. 
The first part of the commit message tells the reviewer what file or set of files has 
been modified. Moreover, if a bunch of files has been modified, then the developer 
should include the directory that contains all the modified files within it. 
In either case, the file name without the extension should be surrounded by a group 
of brackets, or a group of brackets should surround the utmost directory name. 
The second part of every good commit message includes a summary of what work was 
committed.  

example:  

`[<file/folder name>] breif summary of work done`

### Git branching strategy



## Testing
### Test Driven Development (TDD)



### Our test naming conventions



### GitHub actions/workflows