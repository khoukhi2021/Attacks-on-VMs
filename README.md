<a href="https://www.ensicaen.fr">
<img src="https://www.ensicaen.fr/wp-content/uploads/2017/02/LogoEnsicaen.gif" width="256" >
</a>

VM-Hacking
================================================
ANODEAU Boris
HANICOTTE Flavien
HERVET Marine

# Purpose 

The aim of the project was to develop an educational software application that contains cyberattacks.

This project focused on three specific attacks: the Arp poisoning attack, the DHCP Spoofing attack and VoIP Eavesdropping. 

# Services on the software platform

On the GUI (Graphical User Interface)
 - Read text information about these three attacks and one text about the attacks in general
 - Display the kind of data that can be captured by the attacks
 - Play audio file, including audio files extracted from the capture files
 - Extract image from a capture file

There are also three independant scripts:
 - a script for Arp Poisoning attack with virtual machines
 - a script for DCHP spoofing attack with virtual machines
 - a script to extract an audio file from a capture file
 
 
# Educational content

The educational content is both in the application and in a theoretical report in the folder "doc".

# Technologies and installation

This project was developed in Python 3.8.

Other softwares tools such as Wireshark, GNS3 and VrtualBox have been used and will be needed to use the virtual machines or to understand what is happening in the network and how the capture files are structured.

A User Manual is also available in the "doc" folder to install the required python librairies for this platform.

# Run the application

To run the GUI, you need to run the file called "Application.py"
