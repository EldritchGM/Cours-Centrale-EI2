ap::m(a->b)->ma->mb 
fmap::(a->b)->ma->mb 

fmap f = (pure.f)

inverse::int->Maybe Double
inverse 0 = Nothing
inverse x = Just 1/x

sommeInverse 0 _ = Nothing
sommeInverse _ 0 = Nothing
sommeInverse x y = do
    Just x' = inverse x
    Just y' = inverse y
    return x' + y'

