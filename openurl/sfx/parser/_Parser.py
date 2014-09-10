## In The Name of Allah

try:
    from lxml import etree
except ImportError as e:
    import xml.ElemetTree as etree
except:
    raise Exception("Sth wrong happened!")

import six

def parse (res, res_type='detail'):
    if isinstance(res, six.string_types):
        strio = six.StringIO()
        strio.writelines(res)
        strio.seek(0)
        xml = etree.parse(strio)
        root = xml.getroot()
        if res_type == 'detail':
            return parse_detail(root)
        elif res_type == 'simple':
            return parse_simple(root)
        elif res_type == 'multi':
            return parse_multi(root)
        elif res_type == 'exist':
            return parse_exist(root)
        else:
            raise ValueError('bad response type!\nExpects "Detail" (default), "simple" of "multi"')
#    elif isinstance(res, 

def parse_simple (root):
    pass

def parse_multi (root):
    pass

def parse_exist (root):
    pass

def parse_detail (root):
    pass

