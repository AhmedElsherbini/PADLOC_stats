################################################
#received on 26.11.2021
#modified by : Ahmed Elsherbini - 30-11-2021

##############################################
library(stringr)
library(xlsx)
library(tidyverse)
library(pheatmap)
library(gplots)
library(SparseM)
library(ComplexHeatmap)
##############################################
setwd("/media/ahmed/CC69-620B6/00_Ph.D/DATA_results/0_accolens_prop_database_work/0_analysis/27_padLOC_immunity/padLOC_2")
wh <- read.xlsx("corny_presence absence.xlsx",sheetIndex = 1)

wh_matrix <- data.matrix(wh[,-1])
rownames(wh_matrix) = wh$Isolate


###########################################
metadata = read.xlsx("Metadata.xlsx",sheetIndex =1)

metadata2 = as.data.frame(metadata[,-1])
rownames(metadata2) = rownames(wh_matrix)
colnames(metadata2) <- c("Species") 


#annotation_colors = list(Country = c(Switzerland ="#6ef88a",Czechia = "#d357fe",Austerlia = "", Jaan = "", Uninted_Kingdom = " " )
ann_colors = list(Species = c(CA_I = "#008000", CA_II = "#FFAC1C", CA_III = "#DC143C",CA_IV = "#d357fe",CM = "#cfe2f3"))


pheatmap(wh_matrix,show_rownames = F,show_colnames = T,fontsize_row = 7.6, fontsize_col = 7 ,cluster_rows = F, annotation_row = metadata2 , annotation_colors = ann_colors, fontsize_number = 29)
