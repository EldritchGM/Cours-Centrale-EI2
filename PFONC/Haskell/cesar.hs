import Data.Char


--on considère un message seulement en minuscules
cesar n s = return (map (\x -> chr ((((ord x) - 97 + n) `mod` 26) + 97)) s)

main = do
    putStrLn "Entrez le décalage"
    n <- getLine
    if (read n) < 1 || (read n) > 25 then do 
        putStrLn "La valeur doit être comprise entre 1 et 25"
        Main.main
    else do
        putStrLn "Entrez le mot" 
        getLine >>= (cesar (read n)) >>= putStrLn

