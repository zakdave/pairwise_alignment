# Optimal Pairwise Alignment

In bioinformatics, pairwise alignment is a method used to compare two sequences and identify regions of similarity. This repository provides an implementation of a pairwise alignment algorithm which outputs score and the alignment to the console. This is based on the following scoring system. 

## Table of Contents

1. [Rules](#introduction)
2. [Installation and Usage](#installation-and-usage)
3. [Testing and matrix visualization](#testing-and-matrix-visualization)
4. [Note about gaps](#note-about-gaps)

## Rules

Match: +5pts
Mismastch: -1pts
Linear Gap Penalty: -4 points 

## Installation and Usage

To use this code, you need to have Python installed. Clone this repository to your local machine and run the pairwise.py file. 
Enter your first sequence and your second sequence when prompted in the console. 

## Testing and matrix visualization
Uncomment the function calls at the bottom of the pariwise.py file beneath the #test comment. Run the pairwise.py to see tests. Additionally, the matrix output to the console can be enabled visually track the matrix and check the algorithm manually by uncommenting the associated print statements. This is disabled by default. 

## Note about gaps
Linear gaps are denoted in the output by the hyphen character: '-'. The script will not allow a '-' character in either of the input sequences to avoid ambiguity in the output. For example, a mismatched '-' would look the same as a vertical or horizontal linear gap. All other characters are valid. 
