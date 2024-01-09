using CSV
using DataFrames
using Plots
using Statistics

iris_data = CSV.File("iris_nolabel.csv") |> DataFrame

println("Select columns for plotting boundaries:")
println("1. Sepal Length")
println("2. Sepal Width")
println("3. Petal Length")
println("4. Petal Width")
println("Enter the numbers of the columns (e.g., 1 3 for Sepal Length and Petal Length):")

selected_columns = readline()
selected_columns = split(selected_columns)

column_names = ["sepallength", "sepalwidth", "petallength", "petalwidth"]
selected_names = [column_names[parse(Int, col)] for col in selected_columns]

setosa_shape = :circle
virginica_shape = :diamond

plot(xlabel=selected_names[1], ylabel=selected_names[2], title="$(selected_names[1]) vs $(selected_names[2])", legend=:topright)
scatter!(setosa[:, selected_names[1]], setosa[:, selected_names[2]], label="Iris-setosa", shape=setosa_shape)
scatter!(virginica[:, selected_names[1]], virginica[:, selected_names[2]], label="Iris-virginica", shape=virginica_shape)

savefig("iris_boundary.png")

println("Plot successfully saved as 'iris_boundary.png'")
