"""
Script for SSO support, saves and converts the cookie string retrieved by the browser.
Please follow:
- https://github.com/lorenzodifuccia/safaribooks/issues/26
- https://github.com/lorenzodifuccia/safaribooks/issues/150#issuecomment-555423085
- https://github.com/lorenzodifuccia/safaribooks/issues/2#issuecomment-367726544


Thanks: @elrob, @noxymon
"""

import json
import safaribooks
import os


def transform(cookies_string=None):
    current_folder = os.path.dirname(os.path.realpath(__file__))
    cookie_file = os.path.join(current_folder, "tmp.txt")
    """
    1 .go to profile on webpage (https://learning.oreilly.com/profile/)
    2. open web inspector (
        in most browser click F12, 
        for new macos, 
            enable Web develope option in setting>advance>show features for developer
            there will be a new menu item "develop" in browser tool bar, click that menu and choose open web inspector
    3. go to network->profile->(request) header->cookies 
    """
    if not cookies_string:
        print("no cookie string pasted in the argument read from tmp.txt")
        with open(cookie_file, 'r') as f:
            cookies_string = f.readline()
            f.close()
    cookies = {}
    for cookie in cookies_string.split("; "):
        key, value = cookie.split("=", 1)
        cookies[key] = value
    print("check cookies")
    print(cookies)
    json.dump(cookies, open(safaribooks.COOKIES_FILE, 'w'))
    print("\n\nDone! Cookie Jar saved into `cookies.json`. "
          "Now you can run `safaribooks.py` without the `--cred` argument...")


USAGE = "\n\n[*] Please use this command putting as argument the cookies retrieved by your browser.\n" + \
        "[+] In order to do so, please follow these steps: \n" + \
        "https://github.com/lorenzodifuccia/safaribooks/issues/150#issuecomment-555423085\n"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("[!] Error: too few arguments." + USAGE)
        exit(1)

    elif len(sys.argv) > 2:
        print("[!] Error: too much arguments, try to enclose the string with quote '\"'." + USAGE)
        exit(1)

    transform(sys.argv[1])
