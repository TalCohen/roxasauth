# RoxasAuth
RoxasAuth is a Python wrapper for the [Roxas](https://github.com/TalCohen/roxas) API.

Installation
------------

You can install roxasauth with [pip](https://pypi.python.org/pypi/pip).

```
pip install roxasauth
```


Usage
-----

Create a roxasauth object with your Roxas-registered device's API key:

```
>>> from roxasauth import roxasauth
>>> r = roxasauth("API_KEY")
```

For ibutton authentication, call the ibutton method with the user's ibutton and a list of the desired LDAP attributes. A dictionary is returned with three keys: whether the user can access the device or not, a message, and the requested attributes as a dictionary of attributes to their values.

```
>>> attrs = ["uid", "entryUUID", "roomNumber"]
>>> r.ibutton("4F0A0D0022824A01", attrs)
{'message': 'Successfully authenticated user.', 'can_access': True, 'returned_attrs': {'uid': 'tcohen', 'entryUUID': 'ba9b46f4-94cb-1031-9eb0-1fc026a2fe14', 'roomNumber': '3074'}}
```

If the request to the server does not return a status code of 200, `None` is returned instead.
