using StatsPlots, RDatasets
using CSV, DataFrames
using Statistics
import Mongoc

# prepare the data
iris = dataset("datasets", "iris")
path = "iris.csv"
data = CSV.read(path, DataFrame)

#open db connection
client = Mongoc.Client("mongodb://localhost:27017")
database = client["iris"]
collection = database["tab"]

#read data frame line by line to insert to mongo
m,n = size(data)
for i=1:m
    row = Mongoc.BSON()
    #insert df row into row
    for j=1:n
        row[names(data)[j]] = data[i,j]
    end
    #insert row BSON into mongorow
    result = push!(collection,row) 
end