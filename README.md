# datascrap
Installation:

1. I am assuming you already have python installed (preferably Python3.x).

        To install required libraries, issue a command as following -
        pip install -r requirements.txt

        Open terminal/command prompt in the directory same as this instruction file is in. (indeed/)

2. to run the scraper you will need to provide 2 arguments-
        1. query - (search keyword for job search)
        2. location - (location for jobs)

if you want you can use either one of them if you want to leave any one argument empty.

3. Issue commad as following -
        scrapy crawl indeed -a query='<keyword>' -a location='<location>' -o <outputfilename.csv>

        in above command, replace <keyword> with actual keyword and <location> with location name.
        The same goes with outputfile name.

        For example, if I want to search for HR manager in California -

        scrapy crawl indeed -a query='HR Manager' -a location='california' -o HR_calilfornia.csv

        Or if you just want to use keyword and not location, you can do something like -

        scrapy crawl indeed -a query='HR Manager' -o HR_manager.csv

4. Please note that here the output format is .CSV file, If you want JSON file, you can just change the output filename extension to .json instead of .csv like follwoing -

        scrapy crawl indeed -a query='HR Manager' -o HR_manager.json

5. Please do not forget to place the ip proxies to the ip_proxies.txt file.

6. Install Local Persist Volume Plugin for Docker (only works on ubuntu systems)

	curl -fsSL https://raw.githubusercontent.com/CWSpear/local-persist/master/scripts/install.sh | sudo bash

# USAGE: #

Then to use, you can create a volume with this plugin (this example will be for a shared folder for images):

	docker volume create -d local-persist -o mountpoint=/data/images --name=images
Then if you create a container, you can connect it to this Volume:

	docker run -d -v images:/path/to/images/on/one/ one
	docker run -d -v images:/path/to/images/on/two/ two
