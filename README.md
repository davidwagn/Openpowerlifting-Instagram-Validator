This project is not affiliated with OpenPowerlifting. Find the original source code on [GitLab](https://gitlab.com/openpowerlifting).

# OpenPowerlifting Instagram Validator

This project is used to check Instagram links used in OpenPowerlifting's dataset for validity. Specifically, it checks if the Instagram site exists or not.


# Usage

1. Clone the repo (update the Instagram csv to it's [current state](https://gitlab.com/openpowerlifting/opl-data/-/blob/main/lifter-data/social-instagram.csv)).

2. Create a "results" directory inside the repo.

3. Provide your own headers in the dummy headers file. Note that this file must be valid JSON.

4. Run the script.

5. Wait - most of the time spent is sleeping, as the script sleeps 1 second between each check to not get blocked by Instagram's spam detection.


# How to get your headers

1. Log in to Instagram on your browser if you aren't.

2. Open your browser's developer tools.

3. Visit https://www.instagram.com/instagram/?__a=1.

4. Check the request headers in your developer tools and fill them into the headers file.

These should be the headers you need. All fields in the dummy header file should be filled. If you see other fields (especially those starting with :), ignore them.

**Make sure to properly escape special characters in your headers, particularly " and \\**

# Why do I need to provide these headers instead of an access token or similar?

Instagram's new public API is stupid beyond any reasonability. Since this doesn't use the public API, you don't need an API key, but need to pretend you're a browser.
