#!/usr/bin/python -tt
# Copyright Jeff Keddy & Pier 1 ECommerce Production Team
"""
Demandware Category Slot Delete
Similar to dw_cleanup, this program's export is a delete XML. 

Notes: The use of .txt files is just for review. Can be switched to lists.
.xml files need the xmlns attributes manually removed.
"""
import sys
import re
import os
import xml.etree.ElementTree as ET
reload(sys) 
sys.setdefaultencoding('utf8')
def main():

	# vars
	slot=[]
	catalog=[]
	campaign=[]
	unused=[]
	st=0 #slot total
	ct=0 #removed count

	# Takes 2 XML files and compares them based on specific id values
	# Test should find Canada, France, USA

	tree = ET.parse('pier1_slot_list.xml')
	root = tree.getroot()

	# Removes Superfluous Campaign Information
	for context in root.findall('./slot-configuration-campaign-assignment/[@configuration-id]'):
		cid=context.get('configuration-id').encode('utf-8')
		campaign.append(cid)
	output = sorted(campaign)
	#print 'Campaign Results: '
	#print output
	results = open('results_campaign.txt','w')
	for i in output:
  		results.write("%s\n" % i)
  	results = open('results_campaign.txt','r')
  	unused=results.read().split('\n')
	for context in root.findall('slot-configuration-campaign-assignment'):
		config = context.get('configuration-id')
		if config in unused:
			#print 'Removed: ' + str(config)
			root.remove(context)
	tree.write('pier1-slot-list-no-campaigns.xml')
	
	# Records all slot configurations
	tree = ET.parse('pier1-slot-list-no-campaigns.xml')
	root = tree.getroot()
	for context in root.findall('./slot-configuration/[@context-id]'):
		st=st+1
		cid=context.get('context-id').encode('utf-8')
		slot.append(cid)
	#print 'Slot Results: '
	#print sorted(slot)

	# Records all catalog entries
	tree = ET.parse('pier1_catalog.xml')
	root = tree.getroot()
	for category in root.findall('./category/[@category-id]'):
		cid=category.get('category-id').encode('utf-8')
		catalog.append(cid)
	#print 'Catalog Results: '
	#print sorted(catalog)
	
	# Compares catalogs and slots. Output should be Safe to Delete slots
	unused = set(slot)-set(catalog)
	output = sorted(unused)
	results = open('results-delete.txt','w')
	for i in output:
  		results.write("%s\n" % i)
  	#print "Output in:" + str(results)

  	# Removes hidden slots.
  	# Test data should remove Canada, France, USA
  	tree = ET.parse('pier1-slot-list-no-campaigns.xml')
	root = tree.getroot()
  	results = open('results.txt','r')
  	unused = results.read().split('\n') #list
	for context in root.findall('slot-configuration'):
		config = context.get('context-id') #str
		gSlot = context.get('context')
		# Test for global slot
		if gSlot == 'global':
			conId = context.get('configuration-id')
			#print 'Global Slot: ' + str(conId) + ' Removed'
			root.remove(context)
		# Test if hidden/unused category slot
		elif config in unused:
			ct=ct+1
			print 'Will remove: ' + str(config) + ' Slot'
		else:
			root.remove(context)

	tree.write('pier1-slot-list-delete.xml')
	print 'Resulting file will remove: ' + str(ct) + ' Slot Configurations'

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()