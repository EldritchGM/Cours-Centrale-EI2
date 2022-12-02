argminf::(Int->Int)->Int->Int
argminf f min = head [x | x <- [0..], f x > min]

