# Engineering Journal 

## Start 06/01/2026 - End 

### Initial Idea
Learn more about the Arduino Boards and build various circuits on breadboards. Apply the accumulated theoretical knowledge to real-life experiments and gain more hands-on experience. 

### Items obtained (as of 06/01):

- Arduino UNO R3 Board
- Breadboard 
- Jumper wires 
- Resistor 10kΩ 
- USB-c/USB-b cable 

### Progress (constantly updated)
#### 06/01:
Learn how an Arduino UNO R3 works, know what all the input points are for and how they impact the final result. Be able to collect information from the Arduino Board and store it. Become comfortable with all the devices. 

#### 06/03: 
Collect the data from an Arduino Board attached to a circuit containing of a resistor, 5V voltage and a grounded wire.(see images/Arduino-1.png for the visualisation) Compare that this data to the data obtained previously from the single Arduino, and analyze the difference. Assume why those differences happen. 

#### 06/05:
New circuit with two resistors (trying to make the results more scientifically correct since right now they are pretty chaotic which means that the system is constantly disturbed by the nevironmental noise which is an unfavorable outcome). Start building software for visualization of the results of the so far 3 different setups.  

#### 06/08: 
Complete the softaware for the visualization: graphs & histograms. Improve the data quality based on the made graphs. Make assumptions on why this data is structured in such way, and perhaps, run the the tests once again. 

#### 06/09: 
After analysis of the graphs and histograms, I decided to only consider the arduino-2 set up. The tiny bumps illustrated will be the exact source of our entropy. If you look at the data that the graph of the 2Rcircuit is using (data/2Rsamples.txt), you will notice that it sues only *2* numbers *(509 and 510)*. Hence, if I convert it to the binary system *(509 -> 1 & 510 -> 0)*, I will get a consistent binary code that could be unterpreted asneeded. However, the problem is that the system is too consistent. A majority of the numbers are 1s (the voltage is consistently around *509 = 2.38V*). However, the problem is that we are trying to get to randomness/entropy, which indicates that ideally 1s should only take up *50%* of the whole list of numbers. In order to achieve that, I used the Von Neumann extractor, which ignores all combinations of 11 and 00 (if the propability of getting a 1 and a 0 was *83%* and *17%* accordicngly, then getting 01 and 10 is both 15%). However, that means that the majority of the list of data *(75%)* will be ignored, which makes the mechanism very inefficient. Within a bit less than a minute it will create around 500 values in the decimal system (which is around 2000 in binary).
Although this algorithm will probably need improvement, so far the main goal has been achieved - based on the environmental electrical noise, the system was able to convert this entropy into a binary code, where 0s and 1s appear pretty close to *50/50*. This is why I have put the name like that: Arduino-entropy-source, which we just achieved. 
So far, the efficiency of the algorithm after it recieves the data is *500/10000 = 5%*, which is a great problem to work on. The prospective efficiency is 25% (assuming that the data recieved is more noise dependent, but it is still converted into binary code, which cuts the amount of numbers by *4*, due to data conversion)

As of now, the work should be continued on: 
- improving the circuit, finding new materials or parts such as a noise translator or a diode
- improving the algorithm which wouldn't have to ignore so much data: maybe not use the binary conversion since it consums so much data. 
- making the project more easy to access, start working on the main file. So far, the idea is to make a single program that would do everything: run the data collection, analyze it, then convert it into binary system (or any other way, if I find it)
