filenames = ['templates/top.html', 'content/index.html', 'templates/bottom.html']
with open('docs1/index.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = ['templates/top.html', 'content/contact.html', 'templates/bottom.html']
with open('docs1/contact.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = ['templates/top.html', 'content/blogs.html', 'templates/bottom.html']
with open('docs1/blogs.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = ['templates/top.html', 'content/projects.html', 'templates/bottom.html']
with open('docs1/projects.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())