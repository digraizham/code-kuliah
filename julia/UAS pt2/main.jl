# Digra Murtaza Izham - 1313621010
# UAS Pengantar Kecerdasan Buatan Pt 2

using DataFrames, Serialization, Statistics, Random, LIBSVM

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

means_class = hcat(means_class1, means_class2, means_class3)
means_class = mean(means_class, dims=3)
means_class = transpose(means_class)

sepal1 = (means_class1[1] + means_class1[2]) / 2
sepal2 = (means_class2[1] + means_class2[2]) / 2
sepal3 = (means_class3[1] + means_class3[2]) / 2

petal1 = (means_class1[3] + means_class1[4]) / 2
petal2 = (means_class2[3] + means_class2[4]) / 2
petal3 = (means_class3[3] + means_class3[4]) / 2

sepal = vcat(sepal1, sepal2, sepal3)
petal = vcat(petal1, petal2, petal3)

# display mean
println("\nMean values sepal :\n$sepal")
println("\nMean values petal :\n$petal\n")
display(means_class)

# Separate DataFrame into sepal and petal DataFrames
sepal_df = select(data, [:sepallength, :sepalwidth])
petal_df = select(data, [:petallength, :petalwidth])

# Calculate the row-wise average for each group
sepal_avg = mean.(eachrow(sepal_df))
petal_avg = mean.(eachrow(petal_df))

println("\n------------------------\n")

data_fix = DataFrame(hcat(sepal_avg,petal_avg,data[!, :x5]),:auto)
display(data_fix)

function euclidean_distance(point1, point2)
    if length(point1) != length(point2)
        throw(ArgumentError("Input points must have the same dimensionality"))
    end

    distance = sqrt(sum((point1[i] - point2[i])^2 for i in 1:length(point1)))
    return distance
end

function label(sepal, petal, point1, point2)
    point = [point1, point2]
    distance1 = euclidean_distance([sepal[1],petal[1]],point)
    distance2 = euclidean_distance([sepal[2],petal[2]],point)
    distance3 = euclidean_distance([sepal[3],petal[3]],point)
    distances = [distance1,distance2,distance3]

    if minimum(distances)==distance1
        return 1.0
    elseif minimum(distances)==distance2
        return 2.0
    elseif minimum(distances)==distance3
        return 3.0
    end
end

point1 = convert(Matrix, Tables.matrix(select(data_fix, [:x1])))
point2 = convert(Matrix, Tables.matrix(select(data_fix, [:x2])))
# display(point[1, 2])
labels = []
# display(point1[2])
# display(point2[2])
for i in 1:nrow(data_fix)
    push!(labels, label(sepal, petal, point1[i], point2[i]))
end
display(labels)