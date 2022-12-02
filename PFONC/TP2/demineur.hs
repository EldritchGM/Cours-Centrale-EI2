import Data.Set (Set)
import qualified Data.Set as S
import System.Random (randomRs, StdGen, mkStdGen, newStdGen)
import Data.List (scanl, transpose, foldl')
import System.IO

data Cell = Covered Int Bool Bool | Uncovered Int | Selected
data Grid = Grid [[Cell]]

instance Show Cell where
    show Selected = "+"
    show (Uncovered n) = show n
    show (Covered _ _ True) = "P"
    show (Covered _ _ False) = "#" 

show_row::[Cell]->String
show_row row = concatMap show row

instance Show Grid where
    show (Grid rows) = unlines $ map show_row rows

--- Création de la grille --- 

insert' s x = S.insert x s

randSet::Int->StdGen->StdGen->Int->Int->Set (Int, Int)
randSet n g1 g2 xmax ymax = do
    let x_coord = randomRs (0, xmax - 1) g1 in
        let y_coord = randomRs (0, ymax - 1) g2 in
            let coors = zip x_coord y_coord in
                let sets = scanl insert' (S.empty) coors in 
                    head $ dropWhile (\x -> (S.size x) < n) sets



grid::Int->Int->Set (Int, Int)->Grid
grid h l mines = Grid [[Covered 0 (S.member (x,y) mines) False | x <- [0..(l-1)]] | y <- [0..(h-1)]]

makeGrid::Int->Int->Int->StdGen->StdGen->Grid
makeGrid h l n g1 g2 = grid h l $ randSet n g1 g2 h l

--- Nombre de Mines ---

mineIndic::Cell->Int
mineIndic (Covered _ x _) = if x then 1 else 0
mineIndic (Uncovered _) = 0

mines::Grid->[[Int]]
mines (Grid rows) = map (\row -> map mineIndic row) rows

moveUp::[[Int]]->[[Int]]
moveUp (h:t) = t ++ [(take (length h) (repeat 0))]

moveDown::[[Int]]->[[Int]]
moveDown liste = reverse $ moveUp $ reverse liste

moveLeft::[[Int]]->[[Int]]
moveLeft liste = transpose $ moveDown $ transpose liste

moveRight::[[Int]]->[[Int]]
moveRight liste = transpose $ moveUp $ transpose liste

gridmoves::[[Int]]->[[[Int]]]
gridmoves grid = map (\f -> f grid) [moveDown.moveLeft, moveDown, moveDown.moveRight, moveLeft, moveRight, moveUp.moveLeft, moveUp, moveUp.moveRight]

rowSum::[Int]->[Int]->[Int]
rowSum [] r = r
rowSum r [] = r
rowSum (h1:t1) (h2:t2) = (h1+h2):(rowSum t1 t2)

matrixSum::[[Int]]->[[Int]]->[[Int]]
matrixSum [] m = m
matrixSum m [] = m
matrixSum (h1:t1) (h2:t2) = (rowSum h1 h2):(matrixSum t1 t2)

neighbourMap::Grid->[[Int]]
neighbourMap grid = foldl matrixSum [] $ gridmoves $ mines grid

updateCell::Cell->Int->Cell
updateCell (Covered _ b1 b2) n = Covered n b1 b2
updateCell (Uncovered _) n = Uncovered n
updateCell Selected  _ = Selected



updateGrid::Grid->[[Int]]->Grid
updateGrid (Grid cell_matrix) int_matrix = Grid $ zipWith (\row_cell int_cell -> zipWith updateCell row_cell int_cell) cell_matrix int_matrix

----Découvrir une case----

applyi::(a->a)->Int->[a]->[a]
applyi f i xs = let (part1, part2) = splitAt i xs in
    concat [part1, [f $ head part2], tail part2]

applyij::(a->a)->Int->Int->[[a]]->[[a]]
applyij f i j xss = applyi (\x -> applyi f j x) i xss


isNotZero'::Cell->Bool
isNotZero' (Covered 0 False _) = False
isNotZero' _ = True

isNotZero::(Int, Int)->[[Cell]]->Bool
isNotZero (i,j) cell_matrix = isNotZero' $ head $ snd $ splitAt j $ head $ snd $ splitAt i cell_matrix 

uncoverCell::Cell->Cell
uncoverCell Selected = Selected
uncoverCell (Uncovered x) = Uncovered x
uncoverCell (Covered _ True _) = error "Une mine!"
uncoverCell (Covered x False _) = Uncovered x



uncover::Grid->(Int, Int)->Grid
uncover (Grid cell_matrix) (i,j)  = if isNotZero (i,j) cell_matrix then Grid $ applyij uncoverCell i j cell_matrix else
    foldl' (\grid couple -> uncover grid couple) (Grid $ applyij uncoverCell i j cell_matrix) [(m,n) | m<-[i-1, i, i+1], n<-[j-1,j,j+1], m > -1, n > -1, m < ((length cell_matrix)), n < ((length $ head cell_matrix))]


--- Boucle principale de jeu ---

covIndic::Cell->Int
covIndic (Covered _ _ _) = 1
covIndic _ = 0

won::Grid->Int->Bool
won (Grid cell_matrix) nb_mines = nb_mines == (sum $ concat $ map (\row -> map covIndic row) cell_matrix)

toggleFlag::Cell->Cell
toggleFlag (Covered n mine flag) = Covered n mine (not flag)
toggleFlag x = x

loop :: Int -> Int -> Int -> Grid -> IO ()
loop i j n b@ ( Grid xs ) -- le paramètre b se décompose en (Grid xs)
    | won b n = putStrLn " Victoire ␣ ! "
    | otherwise = do
    -- affiche la grille avec la case i, j sélectionnée
    putStrLn $ show $ Grid $ applyij ( const Selected ) i j xs
    -- lit un caractère
    c <- getChar
    case c of
        'i' -> loop ( max ( i - 1) 0) j n b                         -- bouge le curseur vers le haut
        'k' -> loop ( min ( i + 1) ((length xs) -1)) j n b        -- bouge le curseur vers le bas
        'j' -> loop  i ( max ( j - 1) 0) n b                        -- bouge le curseur vers la gauche
        'l' -> loop  i ( min ( j + 1) ((length $ head xs) - 1)) n b                -- bouge le curseur vers la droite
        'f' -> loop i j n (Grid $ applyij toggleFlag i j xs)     -- pose ou enlève un drapeau sur la case i, j
        'u' -> loop i j n (uncover b (i,j))                           -- découvre la case i, j; BOUM ?
        otherwise -> loop i j n b -- ne fait rien

main :: IO ()
main = do
    hSetBuffering stdin NoBuffering     -- désactive l’attente de la touche entrée pour l’acquisition
    hSetEcho stdin False -- désactive l’écho du caractère entré sur le terminal
    g1 <- newStdGen -- récupère deux StdGen pour la génération aléatoire
    g2 <- newStdGen
    let nmines = 5 -- nombre de mines, lignes, colonnes
    let l = 7
    let c = 10
    let grid = makeGrid l c nmines g1 g2 -- créer la grille, ajouter les mines, mettre à jour les voisins
    let start_grid = updateGrid grid $ neighbourMap grid
    loop 0 0 nmines start_grid -- démarrer la REPL