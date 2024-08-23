import xml.etree.ElementTree as ET

class RSS:
    def __init__(self, **kwargs):
        self.rss_content = kwargs

        return self.__create_xml()

    def __add_children(self, item, content):

        for tag in content:
            if type(content[tag]) is list:
                categories = content[tag]
                for category_name in categories:
                    category = ET.SubElement(item, 'category')
                    category.text = category_name
                continue
            item_element = ET.SubElement(item, tag)
            item_element.text = content[tag]

        return item


    def __create_xml(self):
        tree = ET.Element("rss")

        channel = ET.SubElement(tree, "channel")

        for tag in self.rss_content:
            content = self.rss_content[tag]
            if content is not None:
                if type(content) is list and len(content) > 0:
                    for iterable_content in content:
                        if type(iterable_content) is dict: # Means that its items:
                            item = ET.SubElement(channel, 'item')
                            self.__add_children(item, iterable_content)

                        elif type(iterable_content) is str:
                            category_name = iterable_content

                            category = ET.SubElement(channel, 'category')
                            category.text = category_name
                else:
                    element = ET.SubElement(channel, tag)
                    element.text = content

        return ET.tostring(tree)

    

rss = RSS(
    title='Dummy', 
    description='Dummy Description', 
    link='https://dummy.com', 
    category=["Newspapers", "Some random category"], 
    copyright=None, 
    docs=None, 
    pubDate=None, 
    rating=None, 
    skipDays=None, 
    skipHours=None, 
    textInput=None, 
    ttl=None, 
    webMaster=None, 
    items=[
        {
            "title": "Some title",
            "link": "https://some-link.com/path",
            "description": "Some description",
            "category": ["one category", "other category"]
        }
    ]
) 
print(rss)
"""
@pytest.mark.parametrize
    ( 
        "rss", 
        [ 
            RSSBuilder().build(), 
            RSSBuilder().set_language("en").build(), 
            RSSBuilder().set_pubDate("Sat, 07 Sep 2002 00:00:01 GMT").build(), 
            RSSBuilder().add_category("Newspapers") .add_category("Some random category") .build(), 
            RSSBuilder().set_lastBuildDate("Sat, 07 Sep 2002 09:42:31 GMT").build(), 
        ], 
    ) 
    def test_required_fields_in_rss_channel_plain(rss): 
        res = "".join(rss_parser(xml(rss))) > assert remove_all_whitespace_characters(res) == remove_all_whitespace_characters( plain(rss) ) 
    
    E 
        AssertionError: assert 'Feed:DummyDe...s://dummy.com' == 'Feed:DummyLi...myDescription' E E - Feed:DummyLink:https://dummy.comDescription:DummyDescription E + Feed:DummyDescription:DummyDescriptionLink:https://dummy.com tests/test_rss_reader.py:39: AssertionError
"""
print()

