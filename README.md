# google-form-cracker
AIM-9 Sidewinder for google forms

# What does it do?
This program seeks for ```quot``` in a Google Form's mhtml source code. Google Forms uses ```quot``` for response validation, so we dump the entire line containing the keyword to get the response validation condition.

This program can break the following forms:
- Escape Rooms
- Poorly Designed Tests
- Anything else that uses the response validation feature

# How do I read this?

The output may look a bit scary, but it's easily decoded. Your answer should usually be after the question text.

# Where do I find the .mhtml source code?

**Method 1:**

1: Right click the page and press "View page source".
2: Press CTRL+S to save the page as mhtml.

**Method 2:**

1: Type ```view-source:``` at the beginning of your form link.
2: Press CTRL+S to save the page as mhtml.
