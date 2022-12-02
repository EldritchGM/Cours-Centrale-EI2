import Data.List (filter)

diviseurs n = filter ((==0).(rem n)) $ takeWhile ((<=n).(^2)) premiers
premiers = 2:filter (null.diviseurs) [3..]

main = print $ premiers !! 4