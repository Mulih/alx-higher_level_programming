Python Try Except
The tr y block lets you test a block of code for errors.
The excep t block lets you handle the error.
The finall y block lets you execute code, regardless of the result of the try- and except blocks.
Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the tr y statement:
Example
The tr y block will generate an exception, because x is not defined:
try :
  print (x)
except :
  print ("An exception occurred" )
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
