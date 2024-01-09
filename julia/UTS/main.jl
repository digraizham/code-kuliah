using ARFFFiles, DataFrames

#Milestone 1
df = ARFFFiles.load(DataFrame, "iris.arff")

println(df)