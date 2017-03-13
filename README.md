# Pier-1-DW-Cleaner
Python scripts designed to clean up Demandware slots, campaigns, etc

## dw_cleanup.py
Runs through the provided XML files and outputs a cleaned up XML. Good for starting a fresh set of slots. 

## dw_slot_delete.py
Runs through the provided XML files and outputs a delete.xml file. This is used to mass delete hidden slots.

## Requirements
Scripts both run on files named pier1_slot_list.xml and pier1_catalog.xml that need to be contained in the root folder. You will need to manually remove and add _xmlns="http://www.demandware.com/xml/impex/slot/2008-09-08"_ from/to the root element of the slot list XML file. 

This is a bug and will hopefully be fixed soon, but XML namespaces are not the most friendly thing in the world.

<<<<<<< HEAD
## How to dw_slot_delete.py

1. Ensure you have required XML files in your local root folder
  * XML files are exported from Demandware under *Online Marketing > Imports & Export* and *Products and Catalogs > Import & Export*
2. Manually remove xmlns value from both files
3. Open Terminal
4. Navigate to Pier-1-DW-Cleaner folder
5. *python dw_slot_delete.py*
6. Script will run and generate several .txt files and xml files.
7. Upload pier1-slot-list-delete.xml (or pier1-slot-list-clean.xml) to *Online Marketing > Imports & Export*
8. Navigate to _Content Slots_ import page. 
  * Choose your file from the list
  * XML Validation happens
  * Choose delete
=======
## How to

1. Ensure you have required XML files in your local root folder
2. Open Terminal
3. Navigate to Pier-1-DW-Cleaner folder
4. *python dw_slot_delete.py*
5. Script will run and generate several .txt files and xml files.
>>>>>>> d8f9e3613f92716b267051bdba72bcc27f59ce40

## To Do

1. Fix XML namespace bug
2. Add user interaction