## NewPipe Subscription to HTML Bookmark File  
Create an HTML bookmark file from the NewPipe Subscription JSON  
  
  
## Description  
Use case is to have a bookmark file that you can import into your browser or share with others.

## Getting Started  

### Requirements
* [Python 3.x](https://www.python.org/downloads/)
* [PIP](https://pip.pypa.io/en/stable/installation/)
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  (recommended)
  
### Installing  
 First, make sure you have **Requirements** installed on your machine.

Run the following in your command prompt to install:
```
git clone https://github.com/WhoKanICan/NewPipe2Bookmark.git
cd NewPipe2Bookmark
pip install -r requirements.txt
```

To install without git,  download the source code from GitHub, extract the archive, and follow the steps above beginning from the second line.
  
### Executing program  
 1. Firstly edit the **config.ini** file to look like this
```ini
[PATHS]
INPUT_PATH = path/to/where/the/JSON/file/sits/from/NewPIPEipe
OUTPUT_PATH = path/to/where/you/want/this/bookmark/saved
```  
**NOTE**: path to the directory where this file resides. The script will look for the latest JSON file that follows the file name format **newpipe_subscription_xxxxxxxxxxx.json**

2. Finally you can now execute the script using
```bash
python create_bookmark.py
```
  
## License  
  
This project is licensed under the MIT License - see the LICENSE file for details  
