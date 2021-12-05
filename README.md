# Red-soci-mejorada
==========

Django Red-soci-mejorada is opensource Red-soci-mejorada on django framework. It has all
the basic features of Red-soci-mejorada to start with. We welcome code contributions
and feature requests via github.
is similar to facebook

This project contains the following modules:

> -   Feed
> -   Perfil
> -   Post


---

# Installation
We recommend windows/linux/ubuntu, no need to use postgres.

#### Install dependencies
---

* Create and activate a virtual environment.

```
virtualenv venv
source venv/bin/activate
```

* Install the project's dependencie

```
pip install -r requirements.txt
```

#### env variables
* Then refer to `env.md` for environment variables and keep those in the `.env` file in the current folder as your project is in.
* Add ```127.0.0.1   test.localhost``` to your hosts file ```/etc/hosts```. Then you can use test as company name to register and login.

#### next steps
```
python manage.py migrate
python manage.py runserver
```
Then open http://localhost:8000 in your borwser and create a new account with edit user-perfil. 


Community
=========

Get help or stay up to date.

-   Follow [@micropyramid](<https://www.linkedin.com/in/nicol%C3%A1s-alexis-gonz%C3%A1lez-pedraza-1a68a9140/detail/recent-activity/shares/>) on Twitter
-   Follow [@Github](<https://github.com/PIPNicolas/>) on GitHub
-   For customisations, email to <nicolas.dev.py@gmail.com>

Credits
-------

### Contributors

Nicolas Gonzalez

![image](https://avatars.githubusercontent.com/u/68659436?s=96&v=4?width=890&button=false)



