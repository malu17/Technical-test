# Simple_UI API


## Running Locally

Make sure you have Python 3.9 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup)


## Installation steps

1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `virtualenv venv`
4. Activate the virtual environment by running `source venv/bin/activate`

- On Windows use `source venv\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django collectstatic `python manage.py collectstatic`

8. Run the django development server using `python manage.py runserver`


## add change en heroku

```sh
$ heroku login
$ cd Simple_UI/
$ git init
$ heroku git:clone -a Simple_UI


$ git add .
$ git commit -am "make it better"
$ git push heroku master
$ heroku run python manage.py migrate
heroku run python manage.py createsuperuser
$ heroku open
```

## Have the complete repository

```sh
$ heroku login
$ heroku git:clone -a Simple_UI
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

# Technical-test

## 2021_2022
## :mega: Acknowledgments

* alx School (providing guidance)
[Elias fiseha]|[Twitter](https://twitter.com/eliasfiseha1) | [GitHub](https://github.com/malu17)
  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Used By

This project is used by the following companies:

- Flink

  
## 🔗 Links
<a href="https://github.com/malu17" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://twitter.com/eliasfiseha1" target="_blank">
<img src=https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white alt=twitter style="margin-bottom: 5px;" />
</a>

<a href="https://linkedin.com/in/linkedin.com/in/ella-fiseha-927673232" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>

  