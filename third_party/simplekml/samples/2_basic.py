import os

from simplekml import *

kml = Kml()

doc = kml.newdocument(name="A Document")
nestdoc = doc.newdocument()

nestdoc.name = "A Nested Document"
nestdoc.description = "This is the nested document's description."

fol = kml.newfolder()
fol.name = "A Folder"
fol.description = "Description of a folder"
fol = fol.newfolder(name='A Nested Folder', description="Description of a nested folder")
fol = kml.newfolder(name='Point Tests', description="Description of Point Folder")
stpnt = fol.newpoint(name="Cape Town Stadium", description='The Cape Town statdium built for the 2010 world cup soccer.', coords=[(18.411102, -33.903486)])
vapnt = fol.newpoint()
vapnt.name = "V&A Waterfront"
vapnt.description = "The V&A Waterfront in Cape Town"
vapnt.coords = [(18.418699, -33.907080)]
vapnt.style.labelstyle.color = 'ff0000ff'
vapnt.labelstyle.scale = 2
vapnt.labelstyle.colormode = ColorMode.random
vapnt.style.iconstyle.color = 'ffff00ff'
vapnt.iconstyle.heading = 45
vapnt.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/arrow.png'
fwpnt = fol.newpoint(name="Ferris Wheel", description="Same style as V&A", coords=[(18.422892, -33.912937)])
fwpnt.style = vapnt.style
shpnt = fol.newpoint(name="Signal Hill", description="Style from a class", coords=[(18.399813, -33.920250)])
style = Style()
style.labelstyle.color = "ff00ffff"
shpnt.style = style

fol = kml.newfolder(name="LineString Tests", description="Description of LineString Folder")
hwlin = fol.newlinestring(name='Habour Wall', description='The harbour wall.', coords=[(18.4344241201222,-33.89769114130021,0), (18.42577537818946,-33.90011519574129,0)])
rblin = fol.newlinestring()
rblin.name = "Rotating Bridge"
rblin.description = 'The bridge rotates!'
rblin.coords = [(18.42180448650733,-33.90615962911964,0),(18.42201572227569,-33.9064462880076,0)]
rblin.altitudemode = AltitudeMode.clamptoground
rblin.style.linestyle.width = 10
rblin.linestyle.color = "ff00ffff"

fol = kml.newfolder(name="Polygon Tests", description="Description of Polgon Folder")
pol = fol.newpolygon(name='Two Oceans Aquarium', description='A aquarium with fish.', outerboundaryis=[(18.41754659343738,-33.90835172260248,0),(18.41812390156041,-33.90809723020431,0),(18.41794038110668,-33.9078222852994,0),(18.41770068653614,-33.90793436536714,0),(18.41747401819836,-33.90771808929424,0),(18.41719328543339,-33.9079095416603,0),(18.41734156322152,-33.90807829739979,0),(18.41717060935807,-33.90819466465658,0),(18.41731950597035,-33.90835166308609,0),(18.41745256837932,-33.90826680151411,0),(18.41754659343738,-33.90835172260248,0 )])
pol = fol.newpolygon()
pol.name = 'Protea Hotel'
pol.description = 'A hotel.'
pol.outerboundaryis = [(18.41543354224076,-33.90815042775773,0),(18.41588475318415,-33.90785215367858,0),(18.41559067227835,-33.90755041505265,0),(18.41514037818727,-33.907849668799,0),(18.41543354224076,-33.90815042775773,0)]
pol.innerboundaryis = [(18.41544664378987,-33.90797757844747,0),(18.415668772438,-33.90782646170953,0),(18.41557012808532,-33.90772429063932,0),(18.4153486707404,-33.90787067928737,0),(18.41544664378987,-33.90797757844747,0)]
pol.style.linestyle.color = 'ff0000ff'
pol.linestyle.width = 5
pol.style.polystyle.color = 'ffff00ff'

fol.newpolygon(name='Two Oceans Aquarium2', description='A aquarium with fish.', outerboundaryis=[(18.41754659343738,-33.90835172260248,0),(18.41812390156041,-33.90809723020431,0),(18.41794038110668,-33.9078222852994,0),(18.41770068653614,-33.90793436536714,0),(18.41747401819836,-33.90771808929424,0),(18.41719328543339,-33.9079095416603,0),(18.41734156322152,-33.90807829739979,0),(18.41717060935807,-33.90819466465658,0),(18.41731950597035,-33.90835166308609,0),(18.41745256837932,-33.90826680151411,0),(18.41754659343738,-33.90835172260248,0 )])


kml.save(os.path.join(os.path.split(__file__)[0], "2_basic.kml"))