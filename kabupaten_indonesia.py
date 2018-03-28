import mapnik
m = mapnik.Map(1280,720)
m.background = mapnik.Color('red')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 3)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="SHP_kabupaten_indonesia/Indo_Kab_Kot.shp")
layer = mapnik.Layer('kabupaten_indonesia')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'kabupaten_indonesia.pdf', 'pdf')
print "rendered image to 'kabupaten_indonesia.pdf' "

