import xml.etree.ElementTree as ET

""" Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
a.	Un root de nom students.
b.	Cinc childs (del root) amb nom student.
c.	Cada child student ha de tindre 4 subchilds:
i.	 name
ii.	 surname
iii.	 email
iv.	 dni
d.	Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
e.	El text de cada etiqueta serà de la vostra elecció.
"""
def xmlstudents():

        p = ET.Element("students")

        """ Aqui van los child Student"""

        c = ET.SubElement(p , "student")
        d = ET.SubElement(p,"student")
        e = ET.SubElement(p , "student")
        f = ET.SubElement(p,"student")
        g = ET.SubElement(p , "student")

        """ Cada child tiene 4 subchilds . Cada subchild va precedido de la letra de su parent"""
        ca = ET.SubElement(c,"name")
        cb = ET.SubElement(c,"surname")
        cc = ET.SubElement(c,"email")
        cd = ET.SubElement(c,"dni")

        da = ET.SubElement(d,"name")
        db = ET.SubElement(d,"surname")
        dc = ET.SubElement(d,"email")
        dd = ET.SubElement(d,"dni")

        ea = ET.SubElement(e,"name")
        eb = ET.SubElement(e,"surname")
        ec = ET.SubElement(e,"email")
        ed = ET.SubElement(e,"dni")

        fa = ET.SubElement(f,"name")
        fb = ET.SubElement(f,"surname")
        fc = ET.SubElement(f,"email")
        fd = ET.SubElement(f,"dni")

        ga = ET.SubElement(g,"name")
        gb = ET.SubElement(g,"surname")
        gc = ET.SubElement(g,"email")
        gd = ET.SubElement(g,"dni")

        """ Aqui definimos los atributos de los 5 child de students , es decir , los atributos de student. Comenzaremos por el 
        student de índice 0 hasta llegar al 4 , en total 5"""
        element0=p[0]
        element0.set('Nota','5')
        element1=p[1]
        element1.set('Nota','6')
        element2=p[2]
        element2.set('Nota','7')
        element3=p[3]
        element3.set('Nota','8')
        element4=p[4]
        element4.set('Nota','9')

        """ Mostrar por la consola el XML (dump) y para que se vea en formato XML (indent)"""
        ET.indent(p)
        ET.dump(p)
""" Esta es la llamada a la función"""
xmlstudents()