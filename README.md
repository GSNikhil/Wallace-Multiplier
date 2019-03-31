# Wallace-Multiplier

This project was a part of VLSI course at National Institute of Technology Karnataka, Surathkal. Submitted by Divya Pentela and G S Nikhil under the guidance of Prof. M Kini and Lab Incharge Mr. Yajunath.

How to use?

1. Open a terminal in this folder and run the following command:

	magic -T pharosc 16EC214_215.mag

2. In the Tcl console, run the following commands:
	
	save
	extract
	ext2sim

3. Now close the Tcl console

4. In the terminal, run the following command:

	irsim scmos100.prm 16EC214_215.sim

5. In the irsim terminal, run the follwing command:

	source test.cmd

6. Close irsim terminal.

7. run the following command in the terminal:

	python complete.py

   It will compare the simulated output with the correct output
