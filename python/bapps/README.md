## burpscript

This extension allows execution of a custom Python script on each HTTP request and response processed by Burp.

To use, type or paste a Python script into the "Script" tab, and use Burp in the normal way. The script will be executed for each HTTP request and response. 

The following variables are defined in the context of the script:

1. extender
2. callbacks
3. helpers
4. toolFlag
5. messageIsRequest
6. messageInfo

## SQLiPy