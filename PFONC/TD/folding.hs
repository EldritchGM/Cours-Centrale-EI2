reverse_homemade::[a]->[a]
reverse_homemade [] = []
reverse_homemade liste = foldl (\ l x -> x:l) [] liste

map_homemade::(a->b)->[a]->[b]
map_homemade f [] = []
map_homemade f liste = reverse $ foldl (\ l x -> (f x):l) [] liste