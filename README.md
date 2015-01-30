# visites-et-enterprises

This script automates the web login at CERN's favourite aparthotel using Selenium.

![](login.png)

# quick start

Install Selenium:

```Bash
firefox release.seleniumhq.org/selenium-ide/2.8.0/selenium-ide-2.8.0.xpi
```

Install Python bindings for Selenium:

```Python
pip install selenium
```

Download the script ```visites-et-enterprises.py```:

```Bash
wget https://raw.githubusercontent.com/wdbm/visites-et-enterprises/master/visites-et-enterprises.py
```

Change the identification and passcode specified in the script as appropriate:

```Python
identification = "Apt999"
passcode       = "wanknob"
```

Run the script to log in and access... the web.
