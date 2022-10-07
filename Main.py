import os

if __name__ == '__main__':
    path = "/Users/zhouwenyang/work/books/axures"

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            o = f"""- [{f}](./axures/{f})"""
            print(o)