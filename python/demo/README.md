# Burp Extender Demo

[https://portswigger.net/burp/extender/][1]

## 0x01 Hello world 

This is a very simple extension that prints some output to various locations within Burp.

## 0x02 Event listeners

This extension registers listeners for various runtime events, and prints a message when each event occurs.


## 0x03 Traffic redirector

This extension redirects all outbound requests from one host to another. 

## 0x04 Custom logger

This extension adds a new tab to Burp's user interface, and displays a log of HTTP traffic for all Burp tools, in the style of Burp's Proxy history.

## 0x05 Custom editor tab 

This extension adds a new tab to Burp's HTTP message editor, in order to handle an unsupported data serialization format.

## 0x06 Custom scan insertion points 

This extension provides custom attack insertion points for active scanning, allowing Burp's scanning engine to work with an unsupported data serialization format.



[1]: https://portswigger.net/burp/extender/