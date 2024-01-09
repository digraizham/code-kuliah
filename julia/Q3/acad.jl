using Mongoc, Plots, Statistics, DataFrames

# Koneksi MongoDB
client = Mongoc.Client("mongodb://localhost:27017/")
db = client["Julia"]
collection = db["bebas"]

data_setosa = [doc for doc in collection if doc["class"] == "Iris-setosa"]
data_virginica = [doc for doc in collection if doc["class"] == "Iris-virginica"]

columns = setdiff(collect(keys(first(data_setosa))), ["_id", "class"])

# Fungsi Hitung Mean
function hitung_mean(data, column)
    return mean([row[column] for row in data])
end

# Hitung Selisih mean dari masing kolom
differences = Dict()

for col in columns
    mean_setosa = hitung_mean(data_setosa, col)
    mean_virginica = hitung_mean(data_virginica, col)
    diff = abs(mean_setosa - mean_virginica)
    differences[col] = diff
end

sorted_columns = sort(collect(differences), by = tuple -> last(tuple), rev=true)
top_2_columns = [sorted_columns[1][1], sorted_columns[2][1]]

x_col = top_2_columns[1]
y_col = top_2_columns[2]

x_data_setosa = [row[x_col] for row in data_setosa]
y_data_setosa = [row[y_col] for row in data_setosa]

x_data_virginica = [row[x_col] for row in data_virginica]
y_data_virginica = [row[y_col] for row in data_virginica]

scatter(x_data_setosa, y_data_setosa, label="Iris-setosa", xlabel=x_col, ylabel=y_col)
scatter!(x_data_virginica, y_data_virginica, label="Iris-virginica")

savefig("scatter.png")