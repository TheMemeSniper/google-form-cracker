# google-form-cracker
AIM-9 Sidewinder for google forms

# What does it do?
This program seeks for ```quot``` in a Google Form's mhtml source code. When found, it will be written to output.txt

This program can break the following forms:
- Escape Rooms
- Poorly Designed Tests
- Anything else that uses the response validation feature

# How do I read this?

This program outputs the full line it finds ```quot``` on, since ```quot``` is used by Google Forms to indicate most response validation options, this will also dump the answer to that question.

# Where do I find the .mhtml source code?

**Method 1:**

1: Right click the page and press "View page source".
2: Press CTRL+S to save the page as mhtml.

**Method 2:**

1: Type ```view-source:``` at the beginning of your form link.
2: Press CTRL+S to save the page as mhtml.
