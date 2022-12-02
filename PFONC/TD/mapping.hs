import Data.Char

map2D::(a->b)->[[a]]->[[b]]
map2D f [] = []
map2D f (t:q) = (map f t):(map2D f q)

petite_puissance::Int->Int->Int
petite_puissance x y = head $ filter (\x -> x > y) $ map (\n ->  x ^ n) [1..]

cesarchr::Int->(Char->Char)
cesarchr shift = chr.(`mod` 26).(+ shift).ord

cesar::String->Int->String
cesar texte shift = (map $ cesarchr shift) texte
