#!/usr/bin/python -tt
# Copyright Jeff Keddy & Pier 1 ECommerce Production Team
"""
Demandware Clean Up
This program takes 2 export XML files and compares an attribute from
each to determine invisible Demandware Slots. Results are exported to results.txt
Add "test/" to the front of all ET.parse calls to load Country xml example
"""
import sys
import re
import os
import xml.etree.ElementTree as ET
def main():
	# vars
	slot=[]
	catalog=[]
	campaign=[]
	unused=[]
	ct=0 #removed count

	# Takes 2 XML files and compares them based on specific id values
	# Test should find Canada, France, USA
	tree = ET.parse('pier1_catalog.xml')
	root = tree.getroot()
	for category in root.findall('./category/[@category-id]'):
		cid=category.get('category-id').encode('utf-8')
		catalog.append(cid)
	print 'Catalog Results: '
	print sorted(catalog)
	
	tree = ET.parse('pier1_slot_list.xml')
	root = tree.getroot()
	for context in root.findall('./slot-configuration/[@context-id]'):
		cid=context.get('context-id').encode('utf-8')
		slot.append(cid)
	print 'Slot Results: '
	print sorted(slot)

	#Comparison
	unused = set(slot)-set(catalog)
	output = sorted(unused)
	results = open('results.txt','w')
	for i in output:
  		results.write("%s\n" % i)
  	print "Output in:" + str(results)

  	# Removes hidden slots.
  	# Test data should remove Canada, France, USA
  	results = open('results.txt','r')
  	unused = results.read().split('\n')
	for context in root.findall('slot-configuration'):
		config = context.get('context-id')
		print config
		if config in unused:
			ct=ct+1
			#print 'Success! Removed: ' + str(config)
			root.remove(context)
	tree.write('pier1_slot_list_clean.xml')
	print 'Removed ' + str(ct) + ' Slot Configurations'

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()