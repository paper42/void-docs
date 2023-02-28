import json
import sys


def adjustChapter(chapter):
    incodeblock = False
    newcontent = ""
    for line in chapter['content'].splitlines():
        if line == "```":
            incodeblock = not incodeblock
        if incodeblock and line.startswith("# "):
            newcontent += line.replace('# ', '<span class="unselectable"># </span>') + "\n"
        else:
            newcontent += line + "\n"
    chapter['content'] = newcontent
    for subchapter in chapter['sub_items']:
        adjustChapter(subchapter['Chapter'])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "supports":
            sys.exit(0)

    context, book = json.load(sys.stdin)

    # only for testing
    with open("book.json", "w+", encoding="utf-8") as f:
        print(json.dumps(book, indent=4), file=f)

    for section in book['sections']:
        adjustChapter(section['Chapter'])

    # we are done with the book's modification, we can just print it to stdout,
    print(json.dumps(book, indent=4))
