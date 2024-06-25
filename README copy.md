## Unitests

<pre><codes>
collenk@LAPTOP-QU24OQM9:~/AirBnB_clone_v2$ ls
AUTHORS  README.md  console.py  models  tests  web_static
collenk@LAPTOP-QU24OQM9:~/AirBnB_clone_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
collenk@LAPTOP-QU24OQM9:~/AirBnB_clone_v2$
collenk@LAPTOP-QU24OQM9:~/AirBnB_clone_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
collenk@LAPTOP-QU24OQM9:~/AirBnB_clone_v2$
</code></pre>