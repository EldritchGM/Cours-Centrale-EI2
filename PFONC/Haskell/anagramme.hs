import Data.List (delete, nub)


an "" = [""]
an xs = concat $ map (\x -> map (x:) $ an $ delete x xs) $ nub xs

main = do
    print $ an $ "abc"s