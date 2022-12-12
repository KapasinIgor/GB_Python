import html_creater
import xml_generator
import data_provider

# print(html_creater.create())
# print(xml_generator.create())

html_creater.new_create(xml_generator.new_create(data_provider.data_collection()))
