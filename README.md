# BurpExtender
BurpExtender

## 0x01 python

### 001 bapps

| name          | description                  |
| ------------- | ---------------------------- |
| burpscript    | allows execution of a custom Python script on each HTTP request and response processed by Burp |
| SQLiPy        | a Python plugin for Burp Suite that integrates SQLMap using the SQLMap API |

### 002 demo


| name          | description                  |
| ------------- | ---------------------------- |
| Custom editor tab | adds a new tab to Burp's HTTP message editor, in order to handle an unsupported data serialization format |
| Custom logger | adds a new tab to Burp's user interface, and displays a log of HTTP traffic for all Burp tools, in the style of Burp's Proxy history |
| Custom scan insertion points | provides custom attack insertion points for active scanning, allowing Burp's scanning engine to work with an unsupported data serialization format |
| Event listeners | registers listeners for various runtime events, and prints a message when each event occurs |
| Hello world     | simple extension that prints some output to various locations within Burp |
| Traffic redirector | redirects all outbound requests from one host to another |
