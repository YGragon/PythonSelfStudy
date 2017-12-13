import pygal

wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'
# 为指定的国家选择一种颜色，并在左边显示我们要突出的国家和国别码
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
