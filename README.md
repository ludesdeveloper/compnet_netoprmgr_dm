# Local Installation

Python 3.7+ is recommended

You can also create virtual environment to use this module.
1.	Clone source code from netoprmgr_dm repository
	```
	https://github.com/ludesdeveloper/netoprmgr_dm.git
	cd netoprmgr_dm
	```
	
2.	Install requirements
	```
	pip install -r requirements.txt
	```

# Usage

1.	Run python -m netoprmgr_dm__main__

	![run_main](https://github.com/ludesdeveloper/netoprmgr_dm/blob/master/images/run_main.jpg)

2.	Or you can run python from your directory that contains netoprmgr_dm packages

	![run_main](https://github.com/ludesdeveloper/netoprmgr_dm/blob/master/images/run_main_dir.jpg)

3.	Open web browser, type localhost:5000

	![open_web](https://github.com/ludesdeveloper/netoprmgr_dm/blob/master/images/main_web.jpg)

# Docker

1.	netoprmgr_dm can be pulled from docker
	```
	docker pull ludesdeveloper/netoprmgr_dm
	```
2.	Then run docker
	```
	docker run -d -p 5000:5000 ludesdeveloper/netoprmgr_dm
	```