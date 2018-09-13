Print("Generating your website, be patient, done ... check the scripting/docs folder")

cat templates/top.html content/index.html templates/bottom.html > docs/index.html
cat templates/top.html content/blogs.html templates/bottom.html > docs/index.html
cat templates/top.html content/contact.html templates/bottom.html > docs/index.html
cat templates/top.html content/projects.html templates/bottom.html > docs/index.html