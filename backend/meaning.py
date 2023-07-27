from classes import defs_en, defs_tr

def get_en_meaning(anno):
    objects = []
    duplicate = False
    for x in anno["annotations"]:
        for y in objects:
            if x['obj'] == y['name']:
                duplicate = True
        
        if duplicate == False:
            objects.append({'name': x['obj'], 'meaning': defs_en[x['obj']]})
        
        duplicate = False

    return objects

def get_tr_meaning(anno):
    objects = []
    translated = []
    duplicate = False
    for x in anno['annotations']:
        if x['obj'] == 'penis':
            continue
        tr = defs_tr[x['obj']]
        translated.append({'obj': tr['tr'], 'pos': x['pos']})
        for y in objects:
            if tr['tr'] == y['name']:
                duplicate = True

        if duplicate == False: 
            objects.append({'name': tr['tr'], 'meaning': tr['anlam']})

        duplicate = False

    anno['annotations'] = translated
    return anno | {'defs': objects}
