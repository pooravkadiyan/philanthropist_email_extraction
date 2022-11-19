# philanthropist_email_extraction

This project involves retrieving email of philanthropist all over the world from various sectors.

## Design & Working

This section explains the entire logic and design of the the email extraction system.

### Input 

The input would a csv file "input.csv" with names of the philanthropist in th 0th column.

### Process

The task is to search the entire internet for the email of the donor with google.

**The logic we are using is:-**


| Donor Type   |      Assumptions     |  Strategy |
|----------|:-------------:|------:|
| Professional | Must be having a personal website with contact details. For Example: A Interior Designer | <ul><li>Find a list of webpages by searching on google with different search combinations and operators.</li><li>We can extract the email from those webpages using regex.</li></ul>|
| Employee | Must be having a email associated with that organization. For example: CTO at Google |   Ignore for Now |
| Entrepreneur | Must be having a email on linkedin or on some white pages or maybe a personal blog. For example: Richard Branson |  Ignore for Now(except personal blog) |
| Organization | Must be having a business website with contact details. For Example: Bill & Melinda Gates Foundation | <ul><li>Find a list of webpages by searching on google with different search combinations and operators.</li><li>We can extract the email from those webpages using regex.</li></ul> |

Finding Portfolio website of a person 

1- Search "[name] + contact (or) contact information (or) contact me"







## Run Locally

Clone the project

```
  git clone https://github.com/pooravkadiyan/philanthropist_email_extraction.git
```

Go to the project directory

```
  cd philanthropist_email_extraction
```

Create and activate the Virtual Environment

```
  python3 -m venv env
```
```
  source env/bin/activate
```


Install dependencies

```
  pip install -r requirements.txt
```

Run the Script

```
  python3 main.py
```


## Problems Faced

Here are some of the problems faced while working on this project.

- **Google Search Limit** : The first 100 queries per day are free. Any more, then you have to pay $5 per 1000 queries, for up to 10,000 queries per day, just enable billing to do so. Each query returns a maximum of 10 results, so you can retrieve 1000 URL’s from your search per day for free.

So, to extract 100 emails(10 searches per email) it cost around 400 INR.

If you even rotate your IP address, google could detect that.

There are following ways to deal with it:-

1- To use captcha solver for each 100 queries, but getting such AI based captcha solver is hard.

2-Not only rotate proxy but also the router proxy, but getting such proxies(device+router proxies) is never quite costly. There are some free providers but the problem lies in increased time complexity.



## Author 

[@Poorav Kadiyan](https://github.com/pooravkadiyan)


##  About Me 

![image](https://media-exp1.licdn.com/dms/image/C4D22AQHyfm8BW7PTEw/feedshare-shrink_2048_1536/0/1660113794129?e=2147483647&v=beta&t=U8Si__KScWy3yY6F3Q61WKYIwaP0YfmobQFwttBSwIM)


Myself Poorav Kadiyan (first one from left), a former chess player and a hardcore ML guy. 😊

I really like training AI models and automating stuff, one of my recent projects was an AI model, that corrects lip movements while dubbing from one language to another. It was trained on 300k facial videos, to learn the phoneme mapping. 

And yeah I am a chess player, and even got to represent India in the Commonwealth 2019. I am also a part-time boxer.😅

I am really good at Java followed by Python and Javascript.

Honestly, I have a lot of ideas in my head, that I want to convert into reality and I am looking for collaborations. 

I think that’s enough about me.🤐

Feel free to contact me: poorav@pooravkadiyan.com

And here are my social media handles as well, if you wanna know me better.

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/PooravKadiyan)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pooravkadiyan/)
[![portfolio](https://img.shields.io/badge/instagram-0?style=for-the-badge&logo=instagram&logoColor=red)](https://www.instagram.com/pooravkadiyan/)







## Acknowledgements

 - [The Easiest Way to Use a Python Virtual Environment with Git](https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde)

  - [Selenium Documentation](https://www.selenium.dev/documentation/)

  - [12 Ways to Find Someone’s Personal Email Address](https://www.wordstream.com/blog/ws/2009/09/23/find-anyones-personal-email)

  - [Email Address Wikipedia](https://en.wikipedia.org/wiki/Email_address)

  - [Non-Numerical Encoding](https://www.youtube.com/watch?v=ut74oHojxqo&t=37s)

  



