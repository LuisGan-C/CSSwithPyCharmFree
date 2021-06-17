# CSSwithPyCharmFree
## How to use PyCharm community edition for CSS file edit and writing (enabling highlighting).

This repo shows you how you can enable PyCharm Community Edition for CSS keywords, attrs and properties highlighting to be able to write CSS code with the Free PyCharm IDE.

This repo scrapes the tables from the following web pages:
[Page for HTML5 tags](https://www.tutorialrepublic.com/html-reference/html5-tags.php)
[Page for CSS3 properties](https://www.tutorialrepublic.com/css-reference/css3-properties.php)
Then wrangles the data an create two text documents one with all the HTML tags and then all the CSS properties. 
It creates a "keywords1.txt" and "keywords2.txt" documents where the data is stored.
For enabling the CSS keywords highlighting do the following in the PyCharm IDE:
-Go to Settings -> Editor -> File Type. 
-Remove associaton with `*.css` of the default profile.
-Add a new configuration named CSS and associate it with `*.css` files. 
-Set the block comments start `/*` and end `*/`.
-Add the key words for each level:
 -Level 1: the data stored in the "Keywords1.txt" file
 -Level 2: the data stored in the "ketwords2.txt" file
 -level 3: 
 ``
 em
 pt
 px
 rgb
 rgba
 ``
 -level 4:
 ``
 !important
 active
 after
 before
 hover
 none
 visited
 ``
And thats it!
Idea taken from a comment form this StackOverflow question, answer from the user Andrea:
[StackOveflow Question](https://stackoverflow.com/questions/20986720/pycharm-is-community-edition-able-to-highlight-css-javascript)
