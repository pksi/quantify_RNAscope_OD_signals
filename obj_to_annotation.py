import xml.etree.ElementTree as ET
import csv

# input information
inFile = "TranslateBio_ObjectData_FOV\SP-013270_9_hOTC-Codon-127-No-XMm.mrxs_job70920Indica Labs - ISH v4.1.3_object_results.csv"
layerName = "Bin 1"
imageName = "9_Bin1"


def write_xml(annotations_node, imagename):
    # write out xml
    mydata = ET.tostring(annotations_node, encoding="utf-8", method="xml").decode()
    print(f"Writing out {imagename}.annotations")
    with open(f"{imagename}.annotations", "w") as myfile:
        myfile.write(mydata)


with open(inFile, newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    annotations = ET.Element("Annotations")
    annotation = ET.SubElement(annotations, "Annotation")
    annotation.attrib = {
        "Name": f"{layerName}",
        "LineColor": "255",
        "Visible": "True",
    }

    regions = ET.SubElement(annotation, "Regions")

    for cell in reader:
        if 0 < float(cell["Probe 1 Avg OD"]) <= 0.5:
            # float(cell["Probe 1 Avg OD"])>1.5:
            # 1 < float(cell["Probe 1 Avg OD"]) <= 1.5:
            # float(cell["Probe 1 Avg OD"]) == 0:

            region = ET.SubElement(regions, "Region")
            region.attrib = {
                "Type": "Rectangle",
                "HasEndcaps": "0",
                "NegativeROA": "0",
            }
            vertices = ET.SubElement(region, "Vertices")

            coords = []
            coords.append([cell["XMin"], cell["YMin"]])
            coords.append([cell["XMax"], cell["YMax"]])

            for coord in coords:
                xmlvert = ET.SubElement(vertices, "V")
                xmlvert.attrib = {
                    "X": f"{coord[0]}",
                    "Y": f"{coord[1]}",
                }
            ET.SubElement(region, "Comments")

    write_xml(annotations, f"{imageName}")