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

[github][1]

SQLiPy is a Python plugin for Burp Suite that integrates SQLMap using the SQLMap API.

SQLMap comes with a RESTful based server that will execute SQLMap scans. This plugin can start the API for you or connect to an already running API to perform a scan.

### Requirements

* Jython 2.7 beta, due to the use of json
* Java 1.7 or 1.8 (the beta version of Jython 2.7 requires this)

### Usage

SQLiPy relies on a running instance of the SQLMap API server. You can manually start the server with:

`python sqlmapapi.py -s -H <ip> -p <port>`

Or, you can use the SQLMap API tab to select the IP/Port on which to run, as well as the path to python and sqlmapapi.py on your system.

Once the SQLMap API is running, it is just a matter of right mouse clicking in the 'Request' sub tab of either the Target or Proxy main tabs and choosing 'SQLiPy Scan'.

This will populate the SQLMap Scanner tab of the plugin with information about that request. Clicking the 'Start Scan' button will execute a scan.

If the page is vulnerable to SQL injection, then a thread from the plugin will poll the results and add them to the Scanner Results tab.



[1]: https://github.com/codewatchorg/sqlipy