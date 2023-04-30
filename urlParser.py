from urllib.parse import urlparse

with open('urls.txt') as file:
    urls = file.readlines()

paths = []

for url in urls:
    parsed_url = urlparse(url)
    path_components = parsed_url.path.split('/')[1:]
    for path in path_components:
        paths.append(path)

with open('all_paths.txt', 'w') as file:
    for path in paths:
        file.write(path + '\n')
