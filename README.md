   Experimental keylogger program (v1.0)
===========================================

In the scope of our cybersecurity training, we were asked to design a small keylogger program in Python. We were free to choose how to implement it, and I decided to specifically target machines running on Windows. To make it more realistic, the program should remain as discreet as possible and should self-destroy itself after execution. Another possible option would be to automatically launch it during computer start.

![screenshot](https://github.com/user-attachments/assets/8173fe57-0254-48df-a4e8-ebc41d01ccd0)

The screenshot above shows our keylogger, running in background.

Disclaimer
----------

This program has been designed for educational purposes only. I am not responsible for any damage caused by misuse or malicious utilization of this program.  
Please read this article to know more about legal considerations: [https://crowdstrike.com/en-us/cybersecurity-101/cyberattacks/keylogger/](https://crowdstrike.com/en-us/cybersecurity-101/cyberattacks/keylogger/)

Installation
------------

First install Python 3.13.2 or above.  
Then, make sure you have the following Python packages installed: `requests`, `pynput`.

You can install these packages with:
```
pip install requests pynput
```

Then, clone this repository and edit `keylogger.pyw` to add your own custom webhook URL at line 40.  

---
Double-click on `keylogger.pyw`. You will not see anything as the program starts in background. You can check if the program has successfully started with the following command:
```
tasklist | findstr /I "python"
```


Future work
-----------

A few ideas to improve this project:
- Add mouse's position capture and send this data to the server.
- Automatically take a screenshot of the whole screen and send it to the server.
- Get some system information with `os.system('systeminfo')` and send them to the server.
- Automatically start the keylogger at computer start (thus not self-destroying it).

License
-------

This work is shared under the [MIT license](LICENSE).  
Do not use this program without appropriate permissions.
