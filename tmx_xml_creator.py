import xml.etree.ElementTree as ET
import xml.dom.minidom


def create_xml_from_dicts(src_dict, src_lang, tr_dict, tr_lang):
    # -- Create root
    root = ET.Element('tmx')
    root.set('version', "1.4")

    # -- Configure file header
    # TODO: This could be specified in a .conf file or
    #  some-such and then created from that file
    header = ET.SubElement(root, 'header')
    header.set('creationtool', 'tmxtool')
    header.set('creationtoolversion', '1.0.0')
    header.set('datatype', 'PlainText')
    header.set('segtype', 'phrase')
    header.set('adminlang', src_lang + '-' + tr_lang)
    header.set('srclang', src_lang)
    header.set('o-tmf', '.srt')

    # -- Configure file body
    body = ET.SubElement(root, 'body')

    for key in src_dict.keys():
        tu = ET.SubElement(body, 'tu')

        tuv_src = ET.SubElement(tu, 'tuv')
        tuv_src.set('xml:lang', src_lang)
        seg_src = ET.SubElement(tuv_src, 'seg')
        seg_src.text = '\n' + key + '\n' + src_dict[key][1] + '\n'

        tuv_tr = ET.SubElement(tu, 'tuv')
        tuv_tr.set('xml:lang', tr_lang)
        seg_tr = ET.SubElement(tuv_tr, 'seg')
        seg_tr.text = '\n' + key + '\n' + tr_dict[key][1] + '\n'

    dom = ET.tostring(root, encoding='unicode', method='xml')
    # -- Before returning, remove the first line of the string
    tempstring = xml.dom.minidom.parseString(dom).toprettyxml()
    tempstring = tempstring.split('\n', 1)[1]
    return tempstring
