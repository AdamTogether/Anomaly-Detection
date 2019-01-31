###################################
## Data Science Coding Challenge ##
## Anomaly Detection             ##
## Version 1.0                   ##
###################################

#filename <- current_filename()
#print(commandArgs(trailingOnly = FALSE))
#source("exp.R", chdir = T)
#getwd()

dataSet = read.csv(file.choose(), header = TRUE)

attach(dataSet)

pairs(dataSet)
