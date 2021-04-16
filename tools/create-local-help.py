#!/usr/bin/env python3


# the structure of the help files is:
# - ANY_DIR/help/LANG/help.html  (files generated by deltachat-pages)
# - ANY_DIR/help/help.css  (file is should be provided by deltachat-UI, not generated by deltachat-pages)


from shutil import copyfile
import sys
import os
import re


# list all files that should go to the local help here.
# the path should be the path used eg. in the <img> tag.
linked_files = ["assets/home/delta-what-optim.png"]


def read_file(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content


def write_file(filename, content):
    f = open(filename, 'w')
    f.write(content)
    f.close()


def generate_file(srcdir, destdir, lang, file, add_top_links):
    print("generate local help in " + destdir + "/" + lang + "/" + file)

    content = read_file(srcdir + "/" + lang + "/" + file)

    content = re.sub(r"^.*<div id=\"content\">.*<h1>.*?</h1>.*?<ul.*?>",
                       "<!DOCTYPE html>\n"
                     + "<html>"
                     +   "<head>"
                     +     "<meta charset=\"UTF-8\" />"
                     +     "<meta name=\"viewport\" content=\"initial-scale=1.0\" />"
                     +     "<link rel=\"stylesheet\" href=\"../help.css\" />"
                     +   "</head>"
                     +   "<body>"
                     +     "<ul id=\"top\">",
                     content,
                     flags=re.MULTILINE|re.DOTALL)

    content = re.sub(r"</div>.*?</body>.*</html>.*$",
                         "</body>"
                     + "</html>",
                     content,
                     flags=re.MULTILINE|re.DOTALL)

    for linked_file in linked_files:
        srcfile  = "../" + linked_file
        destfile = "../" + linked_file.split("/")[-1]
        content = re.sub(srcfile, destfile, content)

    if add_top_links:
        top_link = "<p class=\"back\"><a href=\"#top\">^</a></p>"
        content = re.sub(r"<h([234].*?)>",
                          top_link + "<h\\1>",
                         content,
                         flags=re.MULTILINE|re.DOTALL) + top_link

    write_file(destdir + "/" + lang + "/" + file, content)


def generate_lang(srcdir, destdir, lang, add_top_links):
    os.makedirs(destdir + "/" + lang, exist_ok=True)
    generate_file(srcdir, destdir, lang, "help.html", add_top_links)


def generate_help(srcdir, destdir, add_top_links=False):
    generate_lang(srcdir, destdir, "cs", add_top_links)
    generate_lang(srcdir, destdir, "de", add_top_links)
    generate_lang(srcdir, destdir, "en", add_top_links)
    generate_lang(srcdir, destdir, "es", add_top_links)
    generate_lang(srcdir, destdir, "fr", add_top_links)
    generate_lang(srcdir, destdir, "it", add_top_links)
    generate_lang(srcdir, destdir, "nl", add_top_links)
    generate_lang(srcdir, destdir, "ru", add_top_links)
    generate_lang(srcdir, destdir, "sq", add_top_links)
    generate_lang(srcdir, destdir, "zh_CN", add_top_links)
    for linked_file in linked_files:
        srcfile  = srcdir  + "/" + linked_file
        destfile = destdir + "/" + linked_file.split("/")[-1]
        print("copy " + srcfile + " to " + destfile)
        copyfile(srcfile, destfile)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        raise SystemExit("usage: create-local-help.py INPUT_DIR OUTPUT_DIR [--add-top-links]"
                      +"\n   eg. create-local-help.py _site     ../foobar")

    srcdir = sys.argv[1]
    print("using source directory:        " + srcdir)

    destdir = sys.argv[2]
    print("using destination directory:   " + destdir)

    add_top_links = False
    if len(sys.argv) == 4 and sys.argv[3] == "--add-top-links":
        add_top_links = True
        print("add links back to top of file: yes")
    else:
        print("add links back to top of file: no")

    if not os.path.isdir(destdir):
        raise SystemExit("Error: " + srcdir + " is no existent directory.")

    if not os.path.isdir(destdir):
        raise SystemExit("Error: " + destdir + " is no existent directory.")

    generate_help(srcdir, destdir, add_top_links=add_top_links)