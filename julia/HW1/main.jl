using CSV, DataFrames, StatsBase

@time begin
    function balanced_resampling(data1, data, generation, range)
        resampled_data = DataFrame()

        data = vcat([data for i in 1:66666]...)

        for i in 1:generation
            setosa = filter(row -> row.class == "Iris-setosa", data)
            virginica = filter(row -> row.class == "Iris-virginica", data)
            versicolor = filter(row -> row.class == "Iris-versicolor", data)

            setosa_resample = setosa[rand(1:end, Int(0.5 * size(setosa, 1))), :]
            virginica_resample = virginica[rand(1:end, Int(0.5 * size(virginica, 1))), :]
            versicolor_resample = versicolor[rand(1:end, Int(0.5 * size(versicolor, 1))), :]

            resampled_data = vcat(resampled_data, setosa_resample, virginica_resample, versicolor_resample)

            rows_amount = size(resampled_data, 1)
            for feature in names(data)[1:end-1]
                resampled_data[:, feature] = round.(max.(0, resampled_data[:, feature] .+ rand(-0.1:range:0.1, rows_amount)), digits=3)
            end
        end

        resampled_data = vcat(data1, resampled_data)

        setosa1 = filter(row -> row.class == "Iris-setosa", resampled_data)
        virginica1 = filter(row -> row.class == "Iris-virginica", resampled_data)
        versicolor1 = filter(row -> row.class == "Iris-versicolor", resampled_data)

        resampled_data = vcat(setosa1, virginica1, versicolor1)

        new_filename = "balanced_resampled_data.csv"
        hasil = CSV.write(new_filename, resampled_data)
        return hasil
    end

    data = CSV.File("iris.csv") |> DataFrame
    data_original = data
    balanced_resampling(data_original, data, 2, 0.01)
end