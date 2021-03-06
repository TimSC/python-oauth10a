"""
The MIT License

Copyright (c) 2007-2010 Leah Culver, Joe Stump, Mark Paschal, Vic Fryzel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import oauth10a
import smtplib
import base64


class SMTP(smtplib.SMTP):
    """SMTP wrapper for smtplib.SMTP that implements XOAUTH."""

    def authenticate(self, url, consumer, token):
        if consumer is not None and not isinstance(consumer, oauth10a.Consumer):
            raise ValueError("Invalid consumer.")

        if token is not None and not isinstance(token, oauth10a.Token):
            raise ValueError("Invalid token.")

        self.docmd('AUTH', 'XOAUTH %s' % \
            base64.b64encode(oauth10a.build_xoauth_string(url, consumer, token)))
