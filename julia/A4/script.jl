using CSV, Plots, Mongoc, Statistics

client = Mongoc.Client("mongodb://localhost:27017/")
db = client["Julia"]
collection = db["bebas"]
iris_data = collect(collection)

# Create a dictionary to store the column names and corresponding lists
column_names = ["sepallength", "sepalwidth", "petallength", "petalwidth"]
data_by_class = Dict()

# Loop through the class labels
for class_label in ["Iris-setosa", "Iris-virginica"]
    data_by_class[class_label] = Dict()
    
    # Loop through the column names
    for col in column_names
        # Filter the data for the current class and column
        data = [x[col] for x in filter(row -> row["class"] == class_label, iris_data)]
        data_by_class[class_label][col] = data
    end
end

class_labels = ["Iris-setosa", "Iris-virginica"]

# Define the differences dictionary here
differences = Dict()

for col in column_names
    differences[col] = Dict()
    for class_label in class_labels
        data = data_by_class[class_label][col]
        mean_diff = abs(mean(data_by_class["Iris-setosa"][col]) - mean(data_by_class["Iris-virginica"][col]))
        differences[col][class_label] = mean_diff
    end
end

variables = Dict("sepallength" => differences["sepallength"]["Iris-setosa"], "sepalwidth" => differences["sepalwidth"]["Iris-setosa"], "petallength" => differences["petallength"]["Iris-setosa"], "petalwidth" => differences["petalwidth"]["Iris-setosa"])
sorted_variables = sort(collect(variables), by=x->x[2], rev=true)

first_setosa = [x["$(sorted_variables[1][1])"] for x in filter(row -> row["class"] == "Iris-setosa", iris_data)]
second_setosa = [x["$(sorted_variables[2][1])"] for x in filter(row -> row["class"] == "Iris-setosa", iris_data)]
first_virginica = [x["$(sorted_variables[1][1])"] for x in filter(row -> row["class"] == "Iris-virginica", iris_data)]
second_virginica = [x["$(sorted_variables[2][1])"] for x in filter(row -> row["class"] == "Iris-virginica", iris_data)]

plot(xlabel=sorted_variables[1][1], ylabel=sorted_variables[2][1], title="$(sorted_variables[1][1]) vs $(sorted_variables[2][1])", legend=:topright, background=:black, size=(800, 600))
scatter!(first_setosa, second_setosa, label="Iris-setosa", shape=:square)
scatter!(first_virginica, second_virginica, label="Iris-virginica", shape=:circle)

savefig("iris.png")
