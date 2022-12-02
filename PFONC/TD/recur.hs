euclide::Int->Int->Int
euclide a 0 = a
euclide a b = euclide b $ a `mod` b

somme_n_premiers::Int->Int
somme_n_premiers 0 = 0
somme_n_premiers n = n + somme_n_premiers (n - 1)

somme_n_premiers_terminal'::Int->Int->Int
somme_n_premiers_terminal' 0 x = x
somme_n_premiers_terminal' n x = somme_n_premiers_terminal' (n - 1) (x + n)

somme_n_premiers_terminal::Int->Int
somme_n_premiers_terminal n = somme_n_premiers_terminal' n 0

est_multiple_de::Int->Int->Bool
est_multiple_de x y = (==0) $ mod x y

is_perfect'::Int->Int->Bool
is_perfect' n x = if x == n then True else
    if n `est_multiple_de` x then False else is_perfect' n $ x + 1

is_perfect::Int->Bool
is_perfect 1 = False
is_perfect n = is_perfect' n 2

syracuse::Int->Int->Int
syracuse 0 u = u
syracuse n u = if (==0) $ u `mod` 2 then syracuse (n - 1) (u `div` 2) else syracuse (n - 1) (3 * u + 1) 

isMatched'::[Char]->Int->Bool
isMatched' [] 0 = True
isMatched' [] x = False
isMatched' (')':q) 0 = False
isMatched' ('(':q) x = isMatched' q $ x + 1
isMatched' (')':q) x = isMatched' q $ x - 1


isMatched::[Char]->Bool
isMatched st = isMatched' st 0



minPath'::[[Int]]->Int->Int->[Int]->Int->([Int], Int)
minPath' matrix 0 0 path somme = ((matrix!!0!!0):path, somme + (matrix!!0!!0))
minPath' matrix 0 x path somme = minPath' matrix 0 (x - 1) ((matrix!!0!!x):path) (somme + (matrix!!0!!x))
minPath' matrix x 0 path somme = minPath' matrix (x - 1) 0 ((matrix!!x!!0):path) (somme + (matrix!!x!!0))
minPath' matrix x y path somme = 
    let path1 = minPath' matrix (x - 1) y ((matrix!!x!!y):path) (somme + (matrix!!x!!y)) in
        let path2 = minPath' matrix x (y - 1) ((matrix!!x!!y):path) (somme + (matrix!!x!!y)) in
            if (snd path1) <= (snd path2) then path1 else path2

minPath::[[Int]]->([Int], Int)
minPath (t:q) = minPath' (t:q) ((length (t:q)) - 1) ((length t) - 1)  [] 0 

puissancef::(a->a)->a->Int->a
puissancef ope x 0 = x
puissancef ope x n = puissancef ope (ope x) (n - 1)

rangPairs'::[a]->Int->[a]
rangPairs' [] _ = []
rangPairs' (t:q) n = if (==0) $ n `mod` 2 then t:(rangPairs' q (n + 1)) else rangPairs' q (n + 1)

rangPairs::[a]->[a]
rangPairs liste = rangPairs' liste 0

drop_homemade::[a]->Int->[a]
drop_homemade l 0 = l
drop_homemade [] x = []
drop_homemade (t:q) x = drop_homemade q $ x - 1

take'::[a]->Int->[a]->[a]
take' liste 0 res = res
take' (t:q) n res = take' q (n - 1) (res ++ [t])

take_homemade::[a]->Int->[a]
take_homemade liste n = take' liste n []

splitAt_homemade::[a]->Int->([a], [a])
splitAt_homemade liste n = (take_homemade liste n, drop_homemade liste n)