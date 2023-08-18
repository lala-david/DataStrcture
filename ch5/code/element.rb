def ever_other(array)
    new_array = []

    array.each_with_index do |element, index|
        new_array << element if index.even?
    end

    return new_array
end 

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_array = ever_other(input_array)
puts result_array.inspect
