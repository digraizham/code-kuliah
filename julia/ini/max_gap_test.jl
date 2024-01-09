using StatsPlots, RDatasets
using CSV, DataFrames
using Statistics

iris = dataset("datasets", "iris")
path = "iris_nolabel.csv"
data = CSV.read(path, DataFrame)

# step 1: phase out row based on class of interest
fdata = filter(row -> row[end]=="Iris-virginica" || row[end]=="Iris-setosa", data)

# step 2: iterate for each row 
col_size = size(fdata)[2]
feature_size = col_size-1
groups = unique(fdata[:,end])
class_size = size(groups)[1]
# get unique class

mu = zeros(class_size, feature_size)
#do the rest

for i = 1:feature_size
    
    for j = 1:class_size
        mu[j, i] = mean(fdata(findall(x -> x)))
    end
end 