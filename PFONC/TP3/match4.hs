import Data.List
import Data.Ord
import System.IO
import Data.Char

--- Création des data ---

data Color = Jaune | Rouge deriving (Eq, Show)
data Cell = Vide | Color Color deriving Eq
type Column = [Cell]
data Grid = Grid [Column]

instance Show Cell where
    show Vide = "# "
    show (Color Jaune) = "\x1b[33mO \x1b[0m"
    show (Color Rouge) = "\x1b[31mO \x1b[0m" 


show_row::[Cell]->String
show_row row = concatMap show row

instance Show Grid where
    show (Grid columns) = unlines $ (++) ["0 1 2 3 4 5 6"] $ reverse $ map (concatMap show) (transpose columns)


--- grille vide ---

initial::Grid
initial = Grid $ replicate 7 $ replicate 6 Vide

--- jouer un coup ---

addToken::Column->Color->Column
addToken [] couleur = []
addToken (Vide:t) couleur = (Color couleur):t
addToken (h:t) couleur = h:(addToken t couleur)

applyi::(a->a)->Int->[a]->[a]
applyi f i xs = let (part1, part2) = splitAt i xs in
    concat [part1, [f $ head part2], tail part2]

play::Grid->Color->Int->Grid
play (Grid columns) color i = Grid $ applyi (\column -> addToken column color) i columns

--- Trouver le gagnant ---

addCellToList::[(Cell, Int)]->Cell->[(Cell,Int)]
addCellToList [] c = [(c,1)]
addCellToList ((current_c, current_i):t) c = if c == current_c then ((current_c, current_i + 1)):t else ((c, 1):(current_c, current_i):t)

summarize::[Cell]->[(Cell, Int)]
summarize = foldl' addCellToList []

diagonalize::[[a]]->[[a]]
diagonalize g = do
    let x = length g
    let y = length $ head g
    [[g!!i!!j | i<-[0..((length g) - 1)], j<-[0..((length $ head g) - 1)], i + j == n] | n<-[0..(x + y - 2)]]

summarize_columns::[[Cell]]->[(Cell, Int)]
summarize_columns columns = concatMap summarize columns

summarize_lines::[[Cell]]->[(Cell, Int)]
summarize_lines columns = concatMap summarize $ transpose columns

summarize_diag::[[Cell]]->[(Cell, Int)]
summarize_diag columns = concatMap summarize $ diagonalize columns

summarize_diag2::[[Cell]]->[(Cell, Int)]
summarize_diag2 columns = concatMap summarize $ diagonalize $ transpose $ map reverse columns

summary_result::[(Cell, Int)]->Maybe Color
summary_result [] = Nothing
summary_result (((Color Jaune), x):t) = if x >= 4 then Just Jaune else summary_result t
summary_result (((Color Rouge), x):t) = if x >= 4 then Just Rouge else summary_result t
summary_result (h:t) = summary_result t

won::Grid->Maybe Color
won (Grid columns) =  summary_result $ concatMap (\f -> f columns) [summarize_columns, summarize_lines, summarize_diag, summarize_diag2]

--- Intelligence Artificielle ---

full::Column->Bool
full [] = True
full (Vide:t) = False
full (h:t) = full t

legalMoves'::[Column]->Int->[Int]
legalMoves' [] _ = []
legalMoves' (hc:tc) n = if full hc then legalMoves' tc (n + 1) else n:(legalMoves' tc (n + 1))

legalMoves::Grid->[Int]
legalMoves (Grid columns)= legalMoves' columns 0

draw::Grid->Bool
draw grid = (length $ legalMoves grid) == 0

summary_evaluate::[(Cell, Int)]->Int
summary_evaluate [] = 0
summary_evaluate (((Color Jaune), x):t) =  (-1) * x * 100 ^ x + summary_evaluate t
summary_evaluate (((Color Rouge), x):t) = x * 100 ^ x + summary_evaluate t
summary_evaluate (h:t) = summary_evaluate t

evaluate::Grid->Int
evaluate (Grid columns) = summary_evaluate $ concatMap (\f -> f columns) [summarize_columns, summarize_lines, summarize_diag, summarize_diag2]

nextColor::Color->Color
nextColor Jaune = Jaune
nextColor Rouge = Rouge


negaMax::Color->Int->Int->Grid->(Int, Int)
negaMax c dp_max dp grid = 
    let comparaison = (case c of Jaune -> minimumBy; Rouge -> maximumBy) in
    let moves = legalMoves grid in
    
    if null moves then (evaluate grid, 0) else
    if dp >= dp_max then (evaluate grid, 0)
    else comparaison (comparing fst) (zipWith (\x y -> (x,y)) (map fst (map (\grid -> negaMax (nextColor c) dp_max (dp + 1) grid) (map (\x -> play grid c x) moves))) moves)



--- Boucle principale de jeu ---


-- Un joueur générique
-- Notez le IO Int car, pour un joueur humain, il faut lire au clavier
class Contestant a where
    move::a->Grid->IO Int -- donner un coup à jouer
    color::a->Color          -- donner sa couleur



data Human = Hum Color
data Computer = Com Color

instance Contestant Computer where
    color (Com c) = c
    move (Com c) grid = return $ fst $ negaMax c 4 0 grid

instance Contestant Human where
    color (Hum c) = c
    move (Hum c) grid = do
        chr <- getChar
        if not $ isDigit chr then move (Hum c) grid
        else if elem (digitToInt chr) (legalMoves grid) then return $ digitToInt chr else  move (Hum c) grid

loop::(Contestant a, Contestant b) => a -> b ->Grid->IO()
loop contest1 contest2 grid = do
    print $ grid
    case won grid of
        (Just Rouge) -> print "Le Rouge gagne"
        (Just Jaune) -> print "Le Jaune gagne"
        Nothing ->
            if (draw grid) then print "Match nul!" 
            else do
                nextMove <- move contest1 grid
                loop contest2 contest1 (play grid (color contest1) nextMove)

main::IO () -- Point d’entrée dans le programme
main = do
-- désactive l’attente de la touche entrée pour l’acquisition
    hSetBuffering stdin NoBuffering
-- désactive l’écho du caractère entré sur le terminal
    hSetEcho stdin False
-- lance la REPL
    loop ( Hum Rouge ) ( Com Jaune ) initial

