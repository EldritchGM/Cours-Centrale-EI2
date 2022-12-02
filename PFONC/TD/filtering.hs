import Data.List

list_min::[Int]->Int
list_min (t:[]) = t
list_min (t:q) = min t $ list_min q 

get_index'::[Int]->Int->Int->Int
get_index' (t:q) elt i = if t == elt then i else get_index' q elt (i + 1)

get_index::[Int]->Int->Int
get_index liste elt = get_index' liste elt 0

subMax'::[Int]->[Int]->[Int]
subMax' [] _ = []
subMax' liste [] = subMax' liste [list_min liste]
subMax' liste (t:q) = let filtre = filter (\x -> x > t) liste in
    if filtre == [] then (t:q) else 
        let mini = list_min filtre in
        subMax' (drop (get_index filtre mini) filtre) $ mini:t:q

subMax::[Int]->Int
subMax liste = length $ subMax' liste []

sommePairs::[Int]->Int
sommePairs = sum.filter (\x -> x `mod` 2 == 0)
