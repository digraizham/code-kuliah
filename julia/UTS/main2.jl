using ARFFFiles, DataFrames, LinearAlgebra

#Milestone 2 - gauss jordan elimination
df = ARFFFiles.load(DataFrame, "iris.arff")

matrix = Matrix(df[1:4, 1:4])
println("\nMatrix yang diambil: ", matrix)

function gauss_jordan_elimination(A)
    m, n = size(A)

    for i = 1:m
        pivot_row = argmax(abs.(A[i:m, i])) + i - 1
        A[i, :], A[pivot_row, :] = A[pivot_row, :], A[i, :]
        A[i, :] /= A[i, i]

        for j = 1:m
            if j != i
                A[j, :] -= A[j, i] * A[i, :]
            end
        end
    end

    return A
end


result = gauss_jordan_elimination(matrix)
solution = result[:, end]

println("\nSolution: ", solution)
