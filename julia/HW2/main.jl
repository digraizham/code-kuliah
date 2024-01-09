using DataFrames, Serialization, Statistics

@time begin
    binary_data = open("data_78m.mat", "r")
    data = deserialize(binary_data)

    if isa(data, Matrix)
        col_names = [:sepallength, :sepalwidth, :petallength, :petalwidth, :x5]
        data = DataFrame(convert(Matrix{Float64}, data), col_names)
    end

    class1 = data[data[!, :x5] .== 1.0, :]
    class2 = data[data[!, :x5] .== 2.0, :]
    class3 = data[data[!, :x5] .== 3.0, :]

    # calculate mean of each column in each class
    means_class1 = [mean(skipmissing(class1[!, i])) for i in names(class1)[1:end-1]]
    means_class2 = [mean(skipmissing(class2[!, i])) for i in names(class2)[1:end-1]]
    means_class3 = [mean(skipmissing(class3[!, i])) for i in names(class3)[1:end-1]]

    # display mean
    println("\nMean values per feature (Class 1):\n$means_class1")
    println("\nMean values per feature (Class 2):\n$means_class2")
    println("\nMean values per feature (Class 3):\n$means_class3")
end