# Naive approach to the two Sum problem

function twoSum(N::Vector, target)
    
    len = length(N)

    for i in 1:len - 1 
        for j in i + 1:len
            if N[i] + N[j]  == target
                
                println("pair found: ", [i, j])
            end              
        end
    end
    return "completed"
end

nums = [2,7,11,15, -4, 11]
target = 9


@show twoSum(nums, target)


    