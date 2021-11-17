# blog-site
Blog website with some basic dynamic functionality via python

# What the script does
The script locates any .md articles in the directory it was placed in, converts them to html files, scans the first line for the title, second for the date, third for tags, and fifth for the content (or fourth if there are no tags).  It then adds a link with the title, date, and a preview into the html of the main page that hosts all the articles, as well as any other pages that are mentioned in the tags.  These are placed on the line specified by 'num' in the script.

# Styling
\# [Title]

\### [Date]

\### [Tags] (optional)

\~~~

(no lines in between)
