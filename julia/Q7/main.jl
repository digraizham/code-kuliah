using DataFrames, Serialization, Statistics

binary_data = open("data_78m.mat", "r")
data = deserialize(binary_data)
close(binary_data)

if isa(data, Matrix)
    col_names = [:sepallength, :sepalwidth, :petallength, :petalwidth, :x5]
    data = DataFrame(data, col_names)
end

class1 = data[data[!, :x5] .== 1.0, :]
class2 = data[data[!, :x5] .== 2.0, :]
class3 = data[data[!, :x5] .== 3.0, :]

# split rows from each class with 12800
rows1 = class1[randperm(length(class1)),:]
rows2 = class2[randperm(length(class2)),:]
rows3 = class3[randperm(length(class3)),:]

display(rows1)