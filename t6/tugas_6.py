import mapnik
m = mapnik.Map(600,300)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('cyan'), 1)

r.symbols.append(line_symbolizer)





s.rules.append(r)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_provinsi/INDONESIA_PROP.shp")
layer = mapnik.Layer('provinsi_indonesia')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer2 = mapnik.LineSymbolizer(mapnik.Color('red'), 1)
r.symbols.append(line_symbolizer2)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[nama]'), 'DejaVu Sans Bold',4,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color ('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)
s.rules.append(r)


m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="shp_ibukota/ibukota_indonesia.shp")
layer = mapnik.Layer('ibukota_indonesia')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m, 'ibukota_indonesia.pdf', 'pdf')
print "rendered image to 'ibukota_indonesia.pdf' "

