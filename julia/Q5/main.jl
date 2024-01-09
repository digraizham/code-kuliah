using CSV
using DataFrames

iris_data = CSV.File("iris.csv") |> DataFrame

setosa = filter(row -> row.class == "Iris-setosa", iris_data)
virginica = filter(row -> row.class == "Iris-virginica", iris_data)
versicolor = filter(row -> row.class == "Iris-versicolor", iris_data)

n1 = nrow(setosa)
n2 = nrow(versicolor)
n3 = nrow(virginica)

mid1 = div(n1, 2)
mid2 = div(n2, 2)
mid3 = div(n3, 2)

first_half1 = setosa[1:mid1, :]
second_half1 = setosa[mid1+1:end, :]
first_half2 = versicolor[1:mid2, :]
second_half2 = versicolor[mid2+1:end, :]
first_half3 = virginica[1:mid3, :]
second_half3 = virginica[mid3+1:end, :]

combined_first_half = vcat(first_half1, first_half2, first_half3)
combined_second_half = vcat(second_half1, second_half2, second_half3)

println(combined_first_half)
println(combined_second_half)