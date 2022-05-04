#!/bin/bash

#Frankie Leyva
#BIO380 Spring 22
#5/03/22
#Assignment 4

#

#
for column in {1..119}
do
title=$(cut -d "," -f $column nondata.txt | head -n 1)
t="$title".txt""
echo $t
cut -d "," -f $column nondata.txt > $t
done

