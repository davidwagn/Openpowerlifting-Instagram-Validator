This project is not affiliated with OpenPowerlifting. Find its source code on [GitLab](https://gitlab.com/openpowerlifting).

# Note: Instagram does not send 404 status code anymore, even when the account does not exist. This script won't work without finding a new way to determine if accounts are dead or alive. Instagram also killed the little ?__a=1 trick in the url to only get a quick JSON response.

# OpenPowerlifting Instagram Validator

This project is used to check Instagram links used in OpenPowerlifting's dataset for validity. Specifically, it checks if the Instagram site exists or not.


# Usage

1. Clone the repo (update the Instagram csv to it's [current state](https://gitlab.com/openpowerlifting/opl-data/-/blob/main/lifter-data/social-instagram.csv)).

2. Create a "results" directory inside the repo.

3. Provide your own headers in the dummy headers file. Note that this file must be valid JSON.

4. Run validator.py.

5. Wait - most of the time spent is sleeping, as the script sleeps 1 second between each check to not get blocked by Instagram's spam detection.

6. Wait until Instagram's spam detection blocks you anyways.

7. Go to Instagram's site on your browser, you'll be forced to reset your password because they think your account was compromised.

8. Redo your headers. You'll likely only need to update parts of your cookie.

9. Copy the accounts_left file and rename it.

10. Add a line at the very top using 1 comma (something like "name,Instagram")

11. Change the validator.py to use your copied and renamed accounts_left file's path as data path

12. Goto step 4

Instagram will not be happy about you doing this. You may want to use a burner account. Going through all links will take a few hours. Steps 9 and 10 might be obsolete in a future update, they only exist because I chose a bad way to store the temp results.

# How to get your headers

1. Log in to Instagram on your browser if you aren't.

2. Open your browser's developer tools.

3. Visit https://www.instagram.com/instagram/?__a=1.

4. Check the request headers in your developer tools and fill them into the headers file.

These should be the headers you need. All fields in the dummy header file should be filled. If you see other fields (especially those starting with :), ignore them.

**Make sure to properly escape special characters in your headers, particularly " and \\**

# Why do I need to provide these headers instead of an access token or similar?

Instagram's new public API is stupid beyond any reasonability. Since this doesn't use the public API, you don't need an API key, but need to pretend you're a browser.
