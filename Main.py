import os

def generate_docs():
    path = "./docs"

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            o = f"""- [{f}](./docs/{f})"""
            print(o)


def generate_axures():
    path = "./axures"

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            o = f"""- [{f}](./axures/{f})"""
            print(o)

if __name__ == '__main__':
    generate_docs()