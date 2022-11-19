import re



def email_extractor(text):
    """This is a simple email searcher that will search for emails in a text file and return the emails found in the file.

    But it should be noted that this is not a perfect email searcher. It will not find emails that are in the format of:

    - warikoo at gmail dot com
    - "Warikoo"@ankurwarikoo.com
    


    Args:
      text: The place where to look for.

    Returns:
      A list of emails found. For example: ['warikoo@gmail.com', 'Warikoo@ankurwarikoo.com']

    Raises:
        None
    """
    emails = re.findall(r"[a-z0-9\.\-+_A-Z]+@[a-z0-9\.\-+_A-Z]+\.[a-z]+", text)
    return emails

