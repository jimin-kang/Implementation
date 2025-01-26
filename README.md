## Description
Basic implementation of Shamir's secret sharing scheme ([SSSS](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing)).

Associated writeup: <add link>

This is a toy implementation that is by no means cryptographically secure, but just meant to implement the basic ideas in the associated writeup. This implementation works with numeric secrets/shares, but in practice operations would be performed directly on bitstrings.


## Files
* main.py: executes the program
* ssss.py: contains the implementation of algorithmic logic behind Shamir's secret sharing scheme
* prompt_inputs.py: functions for prompting users for relevant parameters for defining scheme and secret reconstruction 
* constants.py: establishes relevant constants used across other files

## Environment Setup & Program Execution
This project was developed using Python 3.10. However, you should be able to run these notebooks with any version of Python 3.

The required dependencies for this project are listed in requirements.txt. For more information on creating an environment from a requirements file, check out the following:
* https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/