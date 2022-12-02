import Data.List (delete, nub, foldl1)
import Data.Char (ord, chr)
import Data.Maybe  (isNothing, fromJust)

puissance :: Integer -> Integer -> Integer
puissance x 0 = 1
puissance x n = x * puissance x (n - 1)

puissance' :: Integer -> Integer -> Integer
puissance' x 0 = 1
puissance' x n = if even n
    then puissance' (x*x) (div n 2)
    else x * puissance' (x*x) (div n 2)

-- Fibonacci, version exponentielle
fibBad :: Integer -> Integer
fibBad 0 = 0
fibBad 1 = 1
fibBad n = fibBad (n-1) + fibBad (n-2)

-- Fibonacci, version linéaire
fib' :: Integer -> Integer -> Integer -> Integer
fib' 0 _ n2  = n2
fib' n n1 n2 = fib' (n-1) (n1 + n2) n1

fib :: Integer -> Integer
fib n = fib' n 1 0

-- hauteur palindromique
hpal :: Integer -> Integer
hpal x = if x == r x 
    then 0
    else 1 + hpal (x + r x)

r' :: Integer -> Integer -> Integer 
r' 0 m = m
r' x m = r' (div x 10) (10 * m + mod x 10)

r :: Integer -> Integer 
r x = r' x 0

-- et logique
et :: Bool -> Bool -> Bool
et True True = True
et _ _       = False

-- Points et Figures
-- un point en coordonnées cartésiennes
data Point = Point Double Double deriving Show 

distance :: Point -> Point -> Double
distance (Point x1 y1) (Point x2 y2) = sqrt  ((x1 - x2)^2 + (y1-y2)^2)

data Vecteur = Vecteur Double Double

norme :: Vecteur -> Double
norme (Vecteur x y) = distance (Point 0 0) (Point x y)

data Figure = FigP Point | Cercle Point Double | Carre Point Vecteur

perimetre :: Figure -> Double
perimetre (FigP _) = 0
perimetre (Cercle _  r) = 2 * pi * r
perimetre (Carre _ v) = 4 * norme v

-- Nat
data Nat = Zero | Succ Nat deriving Show

eval :: Nat -> Integer
eval Zero = 0
eval (Succ n) = 1 + eval n

addition :: Nat -> Nat -> Nat
addition Zero n = n
addition (Succ n1) n2 = addition n1 (Succ n2)

-- Listes custom
data Liste = Vide | Cons Integer Liste

somme :: Liste -> Integer
somme Vide = 0
somme (Cons x xs) = x + somme xs

data Arbre = VideA | ConsA Integer Arbre Arbre

hauteur :: Arbre -> Integer
hauteur VideA = 0
hauteur (ConsA _ xs ys) = 1 + max (hauteur xs) (hauteur ys)

-- triplets pythagoriciens
pytha :: [(Int, Int, Int)]
pytha = [(a,b,1000-a-b) | a<- [1..333], b<- [(a+1)..500], 
                          a*a+b*b==(1000-a-b)*(1000-a-b), 1000-a-b>b]

 -- inversion
reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

reverse'' :: [a] -> [a] -> [a]
reverse'' [] rs = rs
reverse'' (x:xs) rs = reverse'' xs (x:rs)

rev :: [a] -> [a]
rev xs = reverse'' xs []

-- trimax
suppr x [] = []
suppr x (y:ys) = if x == y then ys else y:suppr x ys

maxi [] = error "maxi: liste vide"
maxi [x] = x
maxi (x:xs) = max x (maxi xs)

trimax [] = []
trimax xs = let y = maxi xs
             in y: trimax (suppr y xs)

-- anagrammes
an :: String -> [String]
an "" = [""]
an xs = concat $ map (\x -> map (x:) $ an $ delete x xs) $ nub xs

-- entiers premiers, filter
diviseurs :: Integer -> [Integer]
diviseurs n = filter ((==0).(rem n)) [1..n]

premiers :: Integer -> [Integer]
premiers n = filter ((==2).fromIntegral.length.diviseurs) [2..n-1]

-- folds
sum' :: [Integer]->Integer
sum' = foldl (+) 0

maximum' :: [Integer] -> Integer
maximum' [] = error "maximum': liste vide"
maximum' xs = foldl1 max xs

and' :: [Bool] -> Bool
and' = foldr (&&) True

or' :: [Bool] -> Bool
or' = foldr (||) False

concat' :: [[a]] -> [a]
concat' = foldl (++) []

any' :: (a->Bool)->[a]->Bool
any' f = or'.(map f)

divisors :: Integer -> [Integer]
divisors n = filter ((==0).(rem n)) $ takeWhile ((<=n).(^2)) primes

primes :: [Integer]
primes = 2:filter (null.divisors) [3..]

-- Entrées, sorties
-- echo
echo :: IO ()
echo = getLine >>= putStrLn

echo1 :: IO ()
echo1 = getLine >>= (\x -> putStrLn (x ++ " " ++ reverse x))

echo2 :: IO ()
echo2 = getLine >>= (\x -> getLine >>= (\y -> putStrLn (y ++ " " ++ x)))

echo3 :: IO ()
echo3 = getLine >>= (\x -> getLine >>= (\y -> putStrLn y >> putStrLn x))

ioLength :: IO Int
ioLength = getLine >>= return.length

-- cesar
cesar :: Int -> String -> String
cesar n = let a = ord 'a' 
           in map (chr.(+a).(`mod` 26).(+n).(subtract a).ord)

execCesar :: IO ()
execCesar = do
    s <- getLine
    n <- getLine
    putStrLn $ cesar (read n) s

loopCesar :: IO ()
loopCesar = do
    n <- getLine
    let x = read n :: Int
    if x >= 1 && x <= 25 
        then do 
            s <- getLine
            putStrLn $ cesar x s
        else 
            putStrLn "try again" >> loopCesar


-- foncteurs

data Expr a = Val a 
            | Inc (Expr a) 
            | Dec (Expr a) 
            | Inv (Expr a) 
            | Neg (Expr a)
            | Add (Expr a) (Expr a)
            | Sub (Expr a) (Expr a)
            | Mul (Expr a) (Expr a)
            | Div (Expr a) (Expr a)
            | Add3 (Expr a) (Expr a) (Expr a)
            deriving Show

evaluate :: (Fractional a) => Expr a -> a
evaluate (Val x) = x
evaluate (Inc y) = evaluate y + 1
evaluate (Dec y) = evaluate y - 1
evaluate (Neg y) = negate $ evaluate y
evaluate (Inv y) = 1 / evaluate y
evaluate (Add y z) = evaluate y + evaluate z
evaluate (Sub y z) = evaluate y - evaluate z
evaluate (Mul y z) = evaluate y * evaluate z
evaluate (Div y z) = evaluate y / evaluate z
evaluate (Add3 x y z) = evaluate x + evaluate y + evaluate z

isZero :: (Eq a, Num a) => Maybe a -> Bool
isZero Nothing = False
isZero (Just x) = (x == 0)

--mevaluate' :: (Eq a, Fractional a) => Expr a -> Maybe a
--mevaluate' (Val x) = Just x
--mevaluate' (Inc y) = let my = mevaluate' y
--                     in if isNothing my 
--                           then Nothing
--                           else Just $ 1 + fromJust my
--mevaluate' (Dec y) = let my = mevaluate' y
--                     in if isNothing my 
--                           then Nothing
--                           else Just $ fromJust my - 1
--mevaluate' (Neg y) = let my = mevaluate' y
--                     in if isNothing my 
--                           then Nothing
--                           else Just $ negate $ fromJust my
--mevaluate' (Inv y) = let my = mevaluate' y
--                     in if isNothing my || isZero my
--                           then Nothing
--                           else Just $ 1 / fromJust my

mfmap' :: (a -> b) -> Maybe a -> Maybe b
mfmap' _ Nothing  = Nothing
mfmap' f (Just x) = Just $ f x

mlift2' :: (a -> b -> c) -> Maybe a -> Maybe b->Maybe c
mlift2' _ Nothing _ = Nothing
mlift2' _ _ Nothing = Nothing
mlift2' f (Just x) (Just y) = Just $ f x y


mevaluate :: (Eq a, Fractional a) => Expr a -> Maybe a
mevaluate (Val x) = Just x
mevaluate (Inc y) = mfmap (+1) $ mevaluate y
mevaluate (Dec y) = mfmap (subtract 1) $ mevaluate y
mevaluate (Neg y) = mfmap negate $ mevaluate y
mevaluate (Inv y) = let my = mevaluate y
                     in if isZero my then Nothing
                                     else mfmap (1/) my
mevaluate (Add y z) = mlift2 (+) (mevaluate y) (mevaluate z)
mevaluate (Add3 x y z) = (Just add3) `apm` (mevaluate x) `apm` (mevaluate y) `apm` (mevaluate z)
mevaluate (Sub y z) = mlift2 (-) (mevaluate y) (mevaluate z)
mevaluate (Mul y z) = mlift2 (*) (mevaluate y) (mevaluate z)
mevaluate (Div y z) = if isZero (mevaluate z)
                        then Nothing
                        else mlift2 (/)  (mevaluate y) (mevaluate z)


apm :: Maybe (a -> b) -> Maybe a -> Maybe b
apm Nothing _ = Nothing
apm _ Nothing = Nothing
apm (Just f) (Just x) = Just $ f x

mlift2 :: (a -> b -> c) -> Maybe a -> Maybe b -> Maybe c
mlift2 f = apm . mfmap f
-- mlift2 f x = apm (mfmap f x) 

add3 :: (Num a) => a -> a -> a -> a
add3 x y z = x + y + z

mfmap = apm . Just

main = print $ puissance 3 4
