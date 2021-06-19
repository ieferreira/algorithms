# Naive approach to the two Sum problem

function binarySearch(N::Vector, low, high, target)

    if high > low
        mid = (high + low) ÷ 2
        println(mid)
        println(N[mid])
        if N[mid] == target
            return mid
        elseif N[mid] > target
            return binarySearch(N, low, mid, target)
        elseif N[mid] < target
            return binarySearch(N, mid, high, target)
        end

    end

end


nums = [2, 3, 4, 10, 14, 21, 25, 29, 32, 220, 980, 1001, 1200, 1230]
target = 1001

# indexing starts at 1
@show binarySearch(nums, 1, length(nums), target)


    