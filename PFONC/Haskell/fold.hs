import Data.List (foldl,foldr)

sum'::[Integer]->Integer
sum' l = foldl (+) 0 l

maxi'::[Integer]->Integer
maxi' [] = error "maximum: liste vide"
maxi' (h:t) = foldl (max) h t

and'::[Bool]->Bool
and' l = foldl (&&) True l

or' = foldl (||) False

any::(a->Bool)->[a]->Bool
any predicate l = or' $ map predicate l

concat'::[[a]]->[a]
concat' = foldl (++) []

main = print $ Main.concat' ["a","bc","d"]

