# Pier-1-DW-Cleaner
Python scripts designed to clean up Demandware slots, campaigns, etc

## dw_cleanup.py
Runs through the provided XML files and outputs a cleaned up XML. Good for starting a fresh set of slots. 

## dw_slot_delete.py
Runs through the provided XML files and outputs a delete.xml file. This is used to mass delete hidden slots.

## Requirements
Scripts both run on files named pier1_slot_list.xml and pier1_catalog.xml that need to be contained in the root folder. You will need to manually remove and add _xmlns="http://www.demandware.com/xml/impex/slot/2008-09-08_ from/to the root element of the slot list XML file. 

This is a bug and will hopefully be fixed soon, but XML namespaces are not the most friendly thing in the world.
