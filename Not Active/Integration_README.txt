Hello class!

This is your new Raspain Operating system with ROS and OPENCV install.
Raspbian Stretch is a form of Debian Unix that runs with an ARM-V8 instruction set at 64bits.
ROS is the Robot Operating System and you will see it is sourced everytime you open a termi
OPENCV is a library for image processing
These are the base tools for most modern robots!

Some Tips:

-to open a terminal use 
	cntrl-alt-t
	cntrl-shift-t //opens new tab in existing terminal

--

-to perform actions with high level permissions
	sudo //stands for super user do

- to change directories in the command line we use 
	cd /$PATH$/

- to list all files in a directory
	ls
	ls -a //arguement -a lists all files even if hidden

-to easily edit files in the terminal we use the program nano, sudo can be used in combination with this 
	nano FileName.extension
	sudo nano FileName.extension (.extension can be .txt or .py or .c ...etc)

-to make your terminal do things when it starts we edit the below file from the home directory
	sudo nano .bashrc

-home directory is abbreviated 
	~/      //and can be acessed by typing just cd

-if you have trouble compiling large files
	-boot to CLI (command line interface)
	-increase swapfile size with 
		-sudo nano /etc/dphys-swapfile
			-increase CONF_SWAPSIZE = 1000, uncomment line above when done



Please take your time and run some ROS tutorials like turtle sim
	http://wiki.ros.org/ROS/tutorials

If you 


	



