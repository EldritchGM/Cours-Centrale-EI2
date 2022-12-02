import Data.List (filter)

diviseurs n = filter ((==0).(rem n)) [1..n]
premiers n = filter ((==2).length.diviseurs) [2..n]



main = print $ premiers 100

apm::Maybe(a -> b) -> Maybe a -> Maybe b 

apm _ Nothing = Nothing
apm f (Just x) = Just f x