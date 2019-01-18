import urllib.request
with open('lecture_slide_links', 'r') as f:
    links = f.read().split(",\n")
#    print(links)
    for link in links:
        urllib.request.urlretrieve (link, link.split("/")[-1])
