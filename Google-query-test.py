import mechanize


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'chrome')]

entry = river
query = "https://www.google.com/search?sclient=psy-ab&site=&source=hp&q=" + entry + "&oq=" + entry
print(query)