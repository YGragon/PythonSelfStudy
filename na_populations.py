import pygal

wm = pygal.Worldmap()
wm.title = 'Populations of Countries in North America'
# 传入字典，国别码作为键，人口数作为值
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
