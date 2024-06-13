## Web Framework
> In the backend, we use Flask as the web framework and Jinja as the template.

### Resources:
- [What is a web framework?](https://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)
- [Flask - Quickstart: Minimal Application, Routing except HTTP methods, Rendering templates](http://flask.pocoo.org/docs/1.0/quickstart/)
- [Jinja - Template Designer: Synopsis, Variables, Comments, Whitespace control, List of Control Structures (read up to Call)](http://jinja.pocoo.org/docs/2.9/templates/)

### Setting Up and Importing Data:

```bash
# Import data on cities and states into SQL database
$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

# Import data on places into SQL database
$ curl -o 10-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
