
function ed(p::Vector{T}, q::Vector{T}) where {T}

    if length(p) != length(q)
        return "error"
    end
    res = sum((p[i] - q[i])^2 for i in 1:length(p))
    res = sqrt(res) 
    
    return res
end

v1 = [1.3, 2.3, 4.5, 4.4, 3.1]
v2 = [2.4, 1.2, 1.4, 3.3, 1.1]

println(ed(v1, v2))