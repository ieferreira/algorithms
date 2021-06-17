function reverse(N::Vector) 
    len = length(N)

    for i = 1:len
        item = N[i]

        j = i
        while (j >= 1)
            # println(N[j])
            # print(item)
            
            if N[j] < item
                println(N[j])
                N[j] = N[j - 1]
                j -= 1

            end
            break
        end
        N[j] = item
    end    
    return N
end

nums = [2,7, 11, 15, -4, 11]
n = reverse(nums)
print(n)
