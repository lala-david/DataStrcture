def ever_other(array)
    new_array = []
    index = 0

    while index < array.length
        new_array << array[index]
        index += 2
    end
    
    return new_array
end

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_array = ever_other(input_array)
puts result_array.inspect