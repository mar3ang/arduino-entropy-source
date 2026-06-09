# Hardware Entropy Source and Randomness Analysis System

## Overview
This project implements a hardware-based entropy generation and analysis system using an Arduino Uno. The system samples analog noise from the microcontroller’s ADC and external circuit configurations, converts the signal into digital data, and evaluates randomness properties using statistical methods in Python.

The goal is to explore physical sources of entropy, signal acquisition techniques, and quantitative measures of randomness quality.

---

## System Architecture
The system consists of:

- Arduino Uno R3 (data acquisition and sampling)
- Analog input (A0) used for noise measurement
- Serial communication interface to host computer
- Python-based analysis pipeline for statistical evaluation

---

## Data Acquisition
The Arduino samples analog signals using the built-in ADC via `analogRead(A0)`. Data is transmitted over serial communication to a host computer for storage and analysis.

Key characteristics:
- Configurable sampling rate
- 10-bit ADC resolution (0–1023 range)
- Raw signal capture from electrical noise sources

---

## Signal Processing
Collected data is processed using Python-based tools. The pipeline includes:

- Conversion of analog values into bitstreams using thresholding
- Optional debiasing using statistical filtering methods
- Preprocessing for noise normalization

---

## Statistical Analysis
Randomness quality is evaluated using multiple statistical techniques:

- Value distribution (histogram analysis)
- Autocorrelation analysis
- Entropy estimation
- Run-length distribution analysis
- Comparison against pseudorandom baselines

---

## Results
Initial experiments demonstrate measurable variability in sampled analog signals consistent with stochastic electrical noise behavior. Further analysis is ongoing to quantify entropy characteristics and improve signal quality.

---

## Requirements

### Hardware
- Arduino Uno R3
- USB connection to host computer

### Software
- Python 3.9+
- numpy
- scipy
- matplotlib

---

## Usage

### 1. Arduino Setup
Upload the provided firmware:

Open the serial monitor to verify data output.

---

### 2. Data Collection
Stream data from the Arduino and save it to a file for analysis.

---

### 3. Python Analysis
Run the analysis pipeline:

Project Structure 
```
arduino-entropy-source/
│
├── arduino/
│   └── noise_sampler.ino
│
├── analysis/
│   ├── main.py
│   ├── entropy.py
│   ├── autocorrelation.py
│   └── visualization.py
│
├── data/
|   ├── logger.py
|   ├── 0Rsamples.txt  
|   ├── 1Rsamples.txt 
│   └── 2Rsamples.txt
|
├── documentation/notes/
│   └── engineering_journal.md
|
├── images/
|   ├── arduino-1.png
│   └── arduino-2.png
│
└── README.md
```