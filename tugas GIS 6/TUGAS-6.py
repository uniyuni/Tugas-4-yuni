import mapnik
m = mapnik.Map(600,300)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)

r.symbols.append(line_symbolizer)

s.rules.append(r)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_provinsi/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer2 = mapnik.LineSymbolizer(mapnik.Color('red'), 1)
r.symbols.append(line_symbolizer2)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[nama]'), 'DejaVu Sans Bold',5,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color ('pink')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

# point_sym = mapnik.PointSymbolizer()
# point_sym.allow_overlap = True
# r.symbols.append(point_sym)

s.rules.append(r)

m.append_style('My Style2',s)
# ds = mapnik.Shapefile(file="pantaiindonesia/IND_PNT_polyline.shp")
ds = mapnik.Shapefile(file="Tugas 4 yuni/Tugas6QGIS.shp")
layer = mapnik.Layer('AIRPORT')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'SRI_WAHYUNI-TUGAS-GIS6.pdf', 'pdf')
print "rendered image to 'SRI_WAHYUNI-TUGAS-GIS6.png'"