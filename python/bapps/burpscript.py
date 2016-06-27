"""
This extension allows execution of a custom Python script on each HTTP request 
and response processed by Burp.

To use, type or paste a Python script into the "Script" tab, and use Burp in the normal way. 
The script will be executed for each HTTP request and response. 

The following variables are defined in the context of the script:
1. extender
2. callbacks
3. helpers
4. toolFlag
5. messageIsRequest
6. messageInfo
"""


from java.awt import Font
from javax.swing import JScrollPane, JTextPane
from javax.swing.text import SimpleAttributeSet

from burp import IBurpExtender, IExtensionStateListener, IHttpListener, ITab

import base64
import traceback


class BurpExtender(IBurpExtender, IExtensionStateListener, IHttpListener, ITab):

    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.helpers
        
        # text pane
        self.scriptpane = JTextPane()
        self.scriptpane.setFont(Font('Monospaced', Font.PLAIN, 11))

        self.scrollpane = JScrollPane()
        self.scrollpane.setViewportView(self.scriptpane)
        
        # compile to bytecode
        self._code = compile('', '<string>', 'exec')
        self._script = ''
        
        #  load configuration settings for the extension that were saved using the method saveExtensionSetting().
        script = callbacks.loadExtensionSetting('script')
        
        if script:
            script = base64.b64decode(script)

            self.scriptpane.document.insertString(
                self.scriptpane.document.length,
                script,
                SimpleAttributeSet())

            self._script = script
            self._code = compile(script, '<string>', 'exec')
            
        # register
        callbacks.registerExtensionStateListener(self)
        callbacks.registerHttpListener(self)
        
        # ui
        callbacks.customizeUiComponent(self.getUiComponent())
        callbacks.addSuiteTab(self)

        self.scriptpane.requestFocus()
        
    #
    # extender unload
    #

    def extensionUnloaded(self):
        try:
            # save script, base64 encode
            self.callbacks.saveExtensionSetting(
                'script', base64.b64encode(self._script))
        except Exception:
            traceback.print_exc(file=self.callbacks.getStderr())
        return
    
    #
    # implement IHttpListener
    #
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        try:
            globals_ = {'extender': self,
                        'callbacks': self.callbacks,
                        'helpers': self.helpers
            }
            locals_  = {'toolFlag': toolFlag,
                        'messageIsRequest': messageIsRequest,
                        'messageInfo': messageInfo
            }
            exec(self.script, globals_, locals_)
        except Exception:
            traceback.print_exc(file=self.callbacks.getStderr())
        return

    #
    # implement ITab
    #
    def getTabCaption(self):
        return 'Script'

    def getUiComponent(self):
        return self.scrollpane
    
    #
    # script 不变时，不用重复编译， 优化性能
    #
    
    @property
    def script(self):
        end = self.scriptpane.document.length
        _script = self.scriptpane.document.getText(0, end)

        if _script == self._script:
            return self._code

        self._script = _script
        self._code = compile(_script, '<string>', 'exec')
        return self._code