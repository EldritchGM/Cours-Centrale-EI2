renverseur' [] rs = rs
renverseur' (h:t) rs = renverseur' t (h:rs)

renverseur l = renverseur' l []

echo_renverseur = getLine >>= (\x -> putStrLn (x ++ " " ++ (renverseur x)))

echo_double = getLine >>= (\x -> getLine >>= (\y -> putStrLn (y ++ " " ++ x)))

ioLength:: IO Int
ioLength = getLine >>= return.length

main = do
    ioLength >>= putStrLn.show