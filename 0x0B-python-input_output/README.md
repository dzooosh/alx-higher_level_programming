# Python Input and Ouput

## What I learnt
<ul>
<li>Opening a file can be done directly using open() function which takes  3 arguments. The filename, mode and the encoding. Using this method, f.close() must be used at the end or it will take up memory as it can never close itself.</li>
<li>Opening or handling files using "with". This method is preferable because it closes automatically at the end of the action be it read, write, tell and so on</li>
<li>How to read a file line by line using readline(), read full content, write text, knowing how many characters was inputed, knowing the position of cursor and move cursor.</li>
<li>JSON, serialization and deserialization, conversion from python data structure to JSON string and reverse</li>
<li>The second argument which is the mode in open() contains a few characters describing the way in which the file will be used.
           <ul> mode can be:
           <li> 'r' when the file will only be read, </li>
           <li> 'w' for only writing (an existing file with the same name will be erased), and </li>
           <li> 'a' opens the file for appending; any data written to the file is automatically added to the end. </li>
           <li> 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.</li></ul>
</li>
</ul>
