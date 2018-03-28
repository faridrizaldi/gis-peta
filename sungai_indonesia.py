import mapnik
m = mapnik.Map(800,800)
m.background = mapnik.Color('pink')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 2)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_sungai/IND_SNG_region.shp")
layer = mapnik.Layer('sungai_indonesia')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'sungai_indonesia.jpeg', 'jpeg')
print "rendered image to 'sungai_indonesia.jpeg' "

