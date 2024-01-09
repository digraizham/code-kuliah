using DataFrames

function euclidean_distance(point1, point2)
    if length(point1) != length(point2)
        throw(ArgumentError("Input points must have the same dimensionality"))
    end

    distance = sqrt(sum((point1[i] - point2[i])^2 for i in 1:length(point1)))
    return distance
end

function label(sepal, petal, point)
    
    distance1 = euclidean_distance([sepal[1],petal[1]],point)
    distance2 = euclidean_distance([sepal[2],petal[2]],point)
    distance3 = euclidean_distance([sepal[3],petal[3]],point)
    distances = [distance1,distance2,distance3]

    if min(distances)==distance1
        return 1.0
    elseif min(distances)==distance2
        return 2.0
    else
        return 3.0
    end
end

# Assuming df is your DataFrame with two columns
df = DataFrame(sepal=[4.9, 5.1, 6.0], petal=[1.5, 1.4, 4.5])

# Example call to the label function
result = label(df.sepal, df.petal, [5.0, 1.5])

println("Label: $result")