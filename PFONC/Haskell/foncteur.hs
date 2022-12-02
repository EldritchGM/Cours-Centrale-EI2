-- ########################################
-- ################Foncteur################
-- ########################################

fmap1::(a->b)->[a]->[b] -- on reconstruit simplement map
fmap1 _ [] = []
fmap1 f (x:xs) = f x : fmap1 f xs
fmap2::(a->b)->(r->a)->(r->b)
fmap2 f g = f.g

-- ###################################################
-- ################Foncteur applicatif################
-- ###################################################


data Expr a = Val a | Inc (Expr a) | Dec (Expr a) | Inv (Expr a) | Neg (Expr a) | Add (Expr a) (Expr a) | Sub (Expr a) (Expr a) | Mul (Expr a) (Expr a) | Div (Expr a) (Expr a) | Add3 (Expr a) (Expr a) (Expr a) deriving Show

mfmap::(a->b)->Maybe a -> Maybe b
mfmap f Nothing = Nothing
mfmap f (Just x) = Just $ f x

mfmap2::(a->b->c)->Maybe a -> Maybe b -> Maybe c
mfmap2 f Nothing _ = Nothing
mfmap2 f _ Nothing = Nothing
mfmap2 f (Just x) (Just y) = Just $ (f x y)

isZero:: (Eq a, Num a) => Maybe a -> Bool
isZero Nothing = False
isZero (Just x) = (x==0)

mevaluate :: (Eq a, Fractional a) => Expr a -> Maybe a
mevaluate (Val x) = Just x
mevaluate (Inc e) = mfmap (\x -> x + 1) $ mevaluate e
mevaluate (Dec e) = mfmap (\x -> x - 1) $ mevaluate e
mevaluate (Neg e) = mfmap negate $ mevaluate e
mevaluate (Inv e) = let me = mevaluate e in 
                        if isZero me then Nothing
                        else mfmap (\x -> 1/x) $ mevaluate e
mevaluate (Add a b) = mfmap2 (+) (mevaluate a) (mevaluate b)
mevaluate (Sub a b) = mfmap2 (-) (mevaluate a) (mevaluate b)
mevaluate (Mul a b) = mfmap2 (*) (mevaluate a) (mevaluate b)
mevaluate (Div a b) = mevaluate $ Mul a $ Inv b
mevaluate (Add3 x y z) = mfmap add3 (mevaluate x) `apm` (mevaluate y) `apm` (mevaluate z)


apm::Maybe(a -> b) -> Maybe a -> Maybe b 

apm _ Nothing = Nothing
apm Nothing _ = Nothing
apm (Just f) (Just x) = Just $ f x

--mlift2 a le même comportement que mfmap2
mlift2 :: (a -> b -> c) -> Maybe a -> Maybe b -> Maybe c
mlift2 f = apm.(mfmap f)

add3::(Num a) => a -> a -> a -> a
add3 x y z = x +  y + z 

fmap = (ap.pure)f 


f = (*) <*> cos
g = lift2 (*) cos sin
g = pure (*) <*> cos <*> sin 
