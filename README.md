# wiki-pagecounts-merge
A series of Python scripts to download and merge Wikipedia.org page count dumps into a single file.  
For the page counts files format see [here](https://wikitech.wikimedia.org/wiki/Analytics/Data/Pagecounts-raw).  
The resulting merged file will have appended a timestamp in each line extracted from the own file name (e.g. 20090505-010000).  

Right now there is are two independent scripts to download the `gzip` files into a folder and merge them in a single text file. Multiple merges can be appended to the same output file.    

