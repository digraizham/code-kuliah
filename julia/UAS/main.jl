using DataFrames, Serialization, Statistics, Random

binary_data = open("data_9m.mat", "r")
data = deserialize(binary_data)
close(binary_data)

if isa(data, Matrix)
    col_names = [:sepallength, :sepalwidth, :petallength, :petalwidth, :x5]
    data = DataFrame(convert(Matrix{Float64}, data), col_names)
end

class1 = data[data[!, :x5].==1.0, :]
class2 = data[data[!, :x5].==2.0, :]
class3 = data[data[!, :x5].==3.0, :]

means_class1 = [mean(skipmissing(class1[!, i])) for i in names(class1)[1:end-1]]
means_class2 = [mean(skipmissing(class2[!, i])) for i in names(class2)[1:end-1]]
means_class3 = [mean(skipmissing(class3[!, i])) for i in names(class3)[1:end-1]]

sepal1 = (means_class1[1] + means_class1[2]) / 2
sepal2 = (means_class2[1] + means_class2[2]) / 2
sepal3 = (means_class3[1] + means_class3[2]) / 2

petal1 = (means_class1[3] + means_class1[4]) / 2
petal2 = (means_class2[3] + means_class2[4]) / 2
petal3 = (means_class3[3] + means_class3[4]) / 2

sepal = vcat(sepal1, sepal2, sepal3)
petal = vcat(petal1, petal2, petal3)

# display mean
println("\nMean values :\n$sepal")
println("\nMean values :\n$petal")


function train_test_split(data, train_ratio)
    n = nrow(data)
    indices = Random.shuffle(1:n)
    train_size = Int(floor(train_ratio * n))
    
    train_indices = indices[1:train_size]
    test_indices = indices[train_size+1:end]
    
    global train_data = data[train_indices, :]
    global test_data = data[test_indices, :]
    
    return train_data, test_data
end

train_ratio = 0.5
train_data, test_data = train_test_split(data, train_ratio)

# Display the training and testing sets
display(nrow(train_data))
display(nrow(test_data))

