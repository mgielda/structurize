#!/usr/bin/env python3

def watch(filename, port=9000):

    from livereload import Server, shell
    server = Server()
    server.watch(filename, shell(f'./structurize.py {filename}', output='index.html'))

    server.serve(root='.', open_url=True, port=port)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Need a filename argument.")
        sys.exit(1)
    import subprocess
    filename = sys.argv[1]
    with open("index.html", "w") as f:
        subprocess.call(["./structurize.py", filename], stdout = f)

    watch(filename)
