import os

files = os.listdir("data/web")

out_str = "words\n"
for f in files:
    path = os.path.join("data/web", f)
    if os.path.isfile(path):
        with open(path) as fs:
            out_str += fs.read()

with open("data/word_list.csv", mode="w") as fs:
    fs.write(out_str)
