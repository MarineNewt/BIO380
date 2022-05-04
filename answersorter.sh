#!/bin/bash

#Frankie Leyva
#BIO380 Spring 22
#5/03/22
#Assignment 4

#This file will take the target file (nondata.txt) and break each column into its own seperate .txt file named after the first entry which is its column's description/key.

#Initiate for loop, to have varaible $column iterate through every column in the file nondata.txt
for column in {1..119}
do
#Pulls the first entry of the column to assign that entry as the title of the .txt file stored into varaible $t
title=$(cut -d "," -f $column nondata.txt | head -n 1)
t="$title".txt""
echo $t
#Takes all entries from the column and overwrites them into the text file named after their first entry.
cut -d "," -f $column nondata.txt > $t
done

