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
The text recognition software determines the text size. 
For more information about the text recognition software used for this project, 
click [here](#to-be-determined-----text-recognition).

#### Overall Score
The overall score is calculated using the average score of all other categories. 
This score is the first one presented to the user. 

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

template:  
* `[<file/folder name>] breif summary of work done` 

examples: 
* `[README] Add Project Details section`  
* `[/src] Refactor all unit test files`

### Git branching strategy
Create a branch of the `main` branch, the production branch, and make your branch with a 
meaningful name that instantly lets any contributor know the purpose of that branch. 
Immediately after creating the new branch, create an upstream to the remote and a draft pull 
request for the new branch. After committing any recent changes, push them up immediately to 
the remote branch. Once finished, please mark your draft pull request as ready for review and 
select at least two reviewers. After getting approved by @TylerAdamMartinez, the current main 
maintainer,  or obtaining the approval of two reviewers, can your branch be squashed and 
merged into the production branch.  

## Testing
### Test Driven Development (TDD)
Write a unit test to test the functionality that you aim to complete. Then proceed to write 
enough code to pass the unit test. Commit these changes and push it up to the remote 
immediately. 

### Our test naming conventions
#### Test Files
All test files will be named in the following format. The name of the file you are writing 
the unit tests for followed by the `.test.py` extension. This extension lets the GitHub 
action know it's a testing file. For example, if you are testing functions inside the 
`colorAnaysis.py` file, the unit test file would be `colorAnaysis.test.py`. Make sure to 
import `unittest` at the top of each test file. 

#### Unit tests
All unit test methods will start with the `test_` prefix. Therefore, a proper unit test 
method name for a unit test to test the text recognition abilities would be 
`test_textRecognition(self)`. The test class should be a child class of the 
`unittest. TestCase` class. A contributor should create one test class per new test file. 
The class name should start with `Test` followed by the name of the category of functions 
it's testing. At the end of the file, make sure to call `unittest.main()` to automatically 
run all the unit tests once that file is called run. For an example of a good test file 
see the section below. 

##### Test file with basic unit tests example
```python
# Filename: src/Foo.test.py

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

For more information about the `unittest` library, please refer to the documentation 
[here](https://docs.python.org/3/library/unittest.html)

### GitHub actions/workflows