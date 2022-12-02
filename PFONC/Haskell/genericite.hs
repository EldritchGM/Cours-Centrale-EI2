import Data.Maybe (fromJust, isNothing)

data Expr a = Val a | Inc (Expr a) | Dec (Expr a) | Inv (Expr a) | Neg (Expr a) deriving Show

evaluate::(Fractional a) => Expr a -> a
evaluate (Val x) = x
evaluate (Inc e) = (evaluate e) + 1
evaluate (Dec e) = (evaluate e) - 1
evaluate (Inv e) = 1/(evaluate e)
evaluate (Neg e) = negate $ evaluate e

isZero:: (Eq a, Num a) => Maybe a -> Bool
isZero Nothing = False
isZero (Just x) = (x==0)

mfmap::(a->b)->Maybe a -> Maybe b
mfmap f Nothing = Nothing
mfmap f (Just x) = Just $ f x

mevaluate :: (Eq a, Fractional a) => Expr a -> Maybe a
mevaluate (Val x) = Just x
mevaluate (Inc e) = mfmap (\x -> x + 1) $ mevaluate e
mevaluate (Dec e) = mfmap (\x -> x - 1) $ mevaluate e
mevaluate (Neg e) = mfmap negate $ mevaluate e
mevaluate (Inv e) = let me = mevaluate e in 
                        if isZero me then Nothing
                        else mfmap (\x -> 1/x) $ mevaluate e




