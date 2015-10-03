# Bad CSS

See that there is a scheme to getting an image from the webserver in the format <url>/id=%d&usr=%d. Putting in an url that is anythign other than 1-4 gives you a broken image which upon opening in a text-editor gives:
> cat: images/: Is a directory

Navigating to <url>/images reveals a forbidden directory.
