#=  
    Nama : Muhammad Alfin Khaerudin
    NIM : 1313621003
    Prodi : Ilmu Komputer 2021
=#

using Mongoc, Plots

println("Nama : Muhammad Alfin Khaerudin")
println("NIM : 1313621003")
println("Prodi : Ilmu Komputer 2021")
println("--------------------------------- Loading Data ---------------------------------")

client = Mongoc.Client("mongodb://localhost:27017")
db = Mongoc.Database(client, "pkb_iris")
collection = Mongoc.Collection(db, "tbl_iris")

file_csv_path = "iris.csv"
file = open(file_csv_path)
header = readline(file)
# println("Header: $header")
if (Mongoc.count_documents(collection, Mongoc.BSON()) == 0)
    println("Memasukkan data CSV ke MongoDB...")
    for line in eachline(file)
        line = replace(line, "\n" => "")
        line = split(line, ",")
        # println(line)
        doc = Mongoc.BSON(
            "sepallength" => parse(Float64, line[1]),
            "sepalwidth" => parse(Float64, line[2]),
            "petallength" => parse(Float64, line[3]),
            "petalwidth" => parse(Float64, line[4]),
            "class" => line[5]
        )
        # println(doc)
        Mongoc.insert_one(collection, doc)
    end
else
    println("Data CSV sudah ada di MongoDB...")
end
close(file)

view = Mongoc.find(
    collection,
    Mongoc.BSON("class" => Mongoc.BSON("\$in" => ["Iris-setosa", "Iris-virginica"]))
)
#= for doc in view
    println(doc)
end =#

pipeline = [
    Mongoc.BSON("\$match" => Mongoc.BSON("class" => Mongoc.BSON("\$in" => ["Iris-setosa", "Iris-virginica"]))),
    Mongoc.BSON("\$group" => Mongoc.BSON(
        "_id" => "\$class", 
        "sepallength" => Mongoc.BSON("\$avg" => "\$sepallength"), 
        "sepalwidth" => Mongoc.BSON("\$avg" => "\$sepalwidth"), 
        "petallength" => Mongoc.BSON("\$avg" => "\$petallength"), 
        "petalwidth" => Mongoc.BSON("\$avg" => "\$petalwidth")))
]

pipeline = Mongoc.BSON(pipeline)
view = Mongoc.aggregate(collection, pipeline)
#= for doc in view
    println(doc)
end =#

iris_setosa_avg = Dict{String, Float64}()
iris_virginica_avg = Dict{String, Float64}()

for doc in view
    # println(doc)
    class = doc["_id"]
    sepallength = doc["sepallength"]
    sepalwidth = doc["sepalwidth"]
    petallength = doc["petallength"]
    petalwidth = doc["petalwidth"]
    
    if class == "Iris-setosa"
        iris_setosa_avg["sepallength"] = sepallength
        iris_setosa_avg["sepalwidth"] = sepalwidth
        iris_setosa_avg["petallength"] = petallength
        iris_setosa_avg["petalwidth"] = petalwidth isa Float64 ? petalwidth : 0.0
    elseif class == "Iris-virginica"
        iris_virginica_avg["sepallength"] = sepallength
        iris_virginica_avg["sepalwidth"] = sepalwidth
        iris_virginica_avg["petallength"] = petallength
        iris_virginica_avg["petalwidth"] = petalwidth isa Float64 ? petalwidth : 0.0
    end
end

perbedaan_avg = Dict{String, Float64}()
for key in keys(iris_setosa_avg)
    perbedaan_avg[key] = iris_setosa_avg[key] - iris_virginica_avg[key]
    perbedaan_avg[key] = perbedaan_avg[key] < 0 ? perbedaan_avg[key] * -1 : perbedaan_avg[key]
end

println("Perbedaan Rata-rata antara Iris-setosa dan Iris-virginica:")
for (key, value) in perbedaan_avg
    println("$key: $value")
end

sorted_keys = sort(collect(perbedaan_avg), by=x->x[2], rev=true)
# println(sorted_keys)
selected_columns = [sorted_keys[1][1], sorted_keys[2][1]]
println("Kolom yang dipilih berdasarkan rata-rata terbesar: $selected_columns")
println("--------------------------------- Plotting Data ---------------------------------")

iris_setosa_data = []
for doc in Mongoc.find(collection, Mongoc.BSON("class" => "Iris-setosa"))
    push!(iris_setosa_data, doc)
end

iris_virginica_data = []
for doc in Mongoc.find(collection, Mongoc.BSON("class" => "Iris-virginica"))
    push!(iris_virginica_data, doc)
end

x_column = selected_columns[1]
y_column = selected_columns[2]
# println(y_column)

x_setosa = [row[x_column] for row in iris_setosa_data]
y_setosa = [row[y_column] for row in iris_setosa_data]
# println(y_setosa)
x_virginica = [row[x_column] for row in iris_virginica_data]
y_virginica = [row[y_column] for row in iris_virginica_data]
# println(y_virginica)

plt = scatter(x_setosa, y_setosa, label="Iris-setosa", legend=:topleft, xlabel=x_column, ylabel=y_column, title="Scatter Plot $x_column vs $y_column")
scatter!(plt, x_virginica, y_virginica, label="Iris-virginica")

display(plt)

println("Scatter Plot tersimpan di gambarscatterplot.png")
savefig("gambarscatterplot.png")