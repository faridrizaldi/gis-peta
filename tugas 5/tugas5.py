import mapnik
m = mapnik.Map(1280,720)
m.background = mapnik.Color('red')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 


line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Bold',8,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap= True
r.symbols.append(point_sym)


s.rules.append(r)

highlight = mapnik.PolygonSymbolizer()
highlight.fill = mapnik.Color('pink')
germany = mapnik.Rule()
germany.filter = mapnik.Expression("[NAME]='Germany'")
germany.symbols.append(highlight)
s.rules.append(germany)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="shp1/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)


## peta pantai indonesia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)


m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_pantai/IND_PNT_polyline.shp")
layer = mapnik.Layer('pantai')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)


## peta kabupaten indonesia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('cyan'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)


m.append_style('My Style3',s)
ds = mapnik.Shapefile(file="SHP_kabupaten_indonesia/Indo_Kab_Kot.shp")
layer = mapnik.Layer('kabupaten')
layer.datasource = ds
layer.styles.append('My Style3')
m.layers.append(layer)



## peta railways asia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)


m.append_style('My Style4',s)
ds = mapnik.Shapefile(file="asia-railways-shape/railways.shp")
layer = mapnik.Layer('asia')
layer.datasource = ds
layer.styles.append('My Style4')
m.layers.append(layer)


## peta point asia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('orange'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)


m.append_style('My Style5',s)
ds = mapnik.Shapefile(file="asia-points-shape/points.shp")
layer = mapnik.Layer('asia')
layer.datasource = ds
layer.styles.append('My Style5')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m, 'world3.pdf', 'pdf')
print "rendered image to 'world2.png' "
