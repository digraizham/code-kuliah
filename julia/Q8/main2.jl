#Digra Murtaza Izham - 1313621010
#Mochamad Adam Lazuardi Agung - 1313621018

using DataFrames, Serialization, Statistics, Random, MLJ, MLJLinearModels

binary_data = open("data_9m.mat", "r")
data = deserialize(binary_data)
close(binary_data)

if isa(data, Matrix)
    col_names = [:sepallength, :sepalwidth, :petallength, :petalwidth, :x5]
    data = DataFrame(convert(Matrix{Float64}, data), col_names)
end
display(data)

class1 = data[data[!, :x5].==1.0, :]
class2 = data[data[!, :x5].==2.0, :]
class3 = data[data[!, :x5].==3.0, :]

# calculate mean of each column in each class
means_class1 = [mean(skipmissing(class1[!, i])) for i in names(class1)[1:end-1]]
means_class2 = [mean(skipmissing(class2[!, i])) for i in names(class2)[1:end-1]]
means_class3 = [mean(skipmissing(class3[!, i])) for i in names(class3)[1:end-1]]

means_class = transpose(hcat(means_class1, means_class2, means_class3))
col_names = [:mean1, :mean2, :mean3, :mean4]
means_class = DataFrame(means_class, col_names)
display(means_class)

# split data by its column
chunk_size = div(size(data, 1), 4)
data_utuh_split = [data[i:min(i+chunk_size-1, end), :] for i in 1:chunk_size:size(data, 1)]

# split means_class by its column
chunk_size_miu = div(size(means_class, 1), 4)
data_hasil_miu_split = [means_class[i:min(i+chunk_size_miu-1, end), :] for i in 1:chunk_size_miu:size(means_class, 1)]

function euclidean_distance(row1, row2)
    return sqrt(sum((row1 .- row2) .^ 2))
end

function predict_class(row_utuh, data_hasil_miu_part)
    distances = [euclidean_distance(row_utuh[1:end-1], row_miu[1:end-1]) for row_miu in eachrow(data_hasil_miu_part)]
    min_distance_index = argmin(distances)
    return data_hasil_miu_part[min_distance_index, :class]
end

# Prediksi class dan tambahkan kolom hasil prediksi pada data utuh
for (i, data_part_utuh) in enumerate(data_utuh_split)
    predicted_classes = [predict_class(row_utuh, data_hasil_miu_split[i]) for row_utuh in eachrow(data_part_utuh)]
    data_part_utuh[!, :predicted_class] = predicted_classes
end

# Langkah 4: Hitung akurasi
correct_predictions = sum(data_part_utuh[:, :x5] .== data_part_utuh[:, :predicted_class])
total_samples = size(data_part_utuh, 1)
accuracy = correct_predictions / total_samples

println("Accuracy: $(accuracy * 100)%")