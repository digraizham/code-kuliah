#Digra Murtaza Izham - 1313621010
#Mochamad Adam Lazuardi Agung - 1313621018

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

# calculate mean of each column in each class
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
# println("\nMean values :\n$means_class3")

# Separate DataFrame into sepal and petal DataFrames
sepal_df = select(data, [:sepallength, :sepalwidth])
petal_df = select(data, [:petallength, :petalwidth])

# Calculate the row-wise average for each group
sepal_avg = mean.(eachrow(sepal_df))
petal_avg = mean.(eachrow(petal_df))

# Display the results
# println("Sepal DataFrame:")
# display(sepal_df)
# println("\nSepal Average:")
# display(DataFrame(sepal_avg, [:sepallength_avg]))

println("\n------------------------\n")

# println("Petal DataFrame:")
# display(petal_df)
# println("\nPetal Average:")
# display(DataFrame(petal_avg, [:petallength_avg]))

data_fix = DataFrame(hcat(sepal_avg,petal_avg,data[!, :x5]),:auto)
display(data_fix)

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

class_fix1 = data_fix[data_fix[!, :x3].==1.0, :]
class_fix2 = data_fix[data_fix[!, :x3].==2.0, :]
class_fix3 = data_fix[data_fix[!, :x3].==3.0, :]

train_ratio = 0.8
train_data1, test_data1 = train_test_split(class_fix1, train_ratio)
train_data2, test_data2 = train_test_split(class_fix2, train_ratio)
train_data3, test_data3 = train_test_split(class_fix3, train_ratio)

# Display the sizes of the training and testing sets
println("Training set size: ", nrow(train_data))
println("Testing set size: ", nrow(test_data))

function euclidean_distance(point1, point2)
    if length(point1) != length(point2)
        throw(ArgumentError("Input points must have the same dimensionality"))
    end

    distance = sqrt(sum((point1[i] - point2[i])^2 for i in 1:length(point1)))
    return distance
end

function label(sepal, petal, point)
    
    distance1 = euclidean_distance([sepal[1],petal[1]],point)
    distance2 = euclidean_distance([sepal[2],petal[2]],point)
    distance3 = euclidean_distance([sepal[3],petal[3]],point)
    distances = [distance1,distance2,distance3]

    if min(distances)==distance1
        return 1.0
    elseif min(distances)==distance2
        return 2.0
    else
        return 3.0
    end
end