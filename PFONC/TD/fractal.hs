import Data.Complex

fractale::Complex Double->Complex Double->Complex Double
fractale z c = z ^ 2 + c

norm::Complex Double->Double
norm z = sqrt $ (realPart z) ^ 2 + (imagPart z) ^ 2

divergence::Int->(Complex Double->Complex Double)->Complex Double->Int
divergence m f z = let z_list = take m $ iterate f z in
    let z_list_zipped = zip [1..m] z_list in
        let res = fst $ head $ reverse $ takeWhile (\couple -> (norm $ snd couple) > 2) z_list_zipped in 
            if res == m then 0 else res

hauteur::Int->Complex Double->Complex Double->Int
hauteur l c1 c2 = let x1 = realPart c1 in let x2 = realPart c2 in let y1 = imagPart c1 in let y2 = imagPart c2 in
    round $ (y2 - y1) * (fromIntegral l) / (x2 - x1)

createComplex::Double->Double->Complex Double
createComplex re im = (re :+ im)

map2D::(a->b)->[[a]]->[[b]]
map2D f [] = []
map2D f (t:q) = (map f t):(map2D f q)

points::Int->Int->Complex Double->Complex Double->[[Complex Double]]
points h l c1 c2 = let x1 = realPart c1 in let x2 = realPart c2 in let y1 = imagPart c1 in let y2 = imagPart c2 in
    let h_pixel = (y2 - y1)/(fromIntegral h) in let l_pixel = (x2 - x1)/(fromIntegral l) in
        [[createComplex (x1 + (fromIntegral i) * l_pixel) (y1 + (fromIntegral j) * h_pixel) | i <- [0..l]] | j <- [0..h]]

mandelbrot::Int->[[Complex Double]]->[[Int]]
mandelbrot m css = map2D (\c -> divergence m (\z -> fractale z c) (createComplex 0 0)) css

julia::Int->Complex Double->[[Complex Double]]->[[Int]]
julia m c css = map2D (\c0 -> divergence m (\z -> fractale z c) c0) css

show'::Int->String
show' x = (show x) ++ " "

fichier::[[Int]]
fichier intMatrix = concatMap show' intMatrix

main = writefile ("./resultat.pgm")