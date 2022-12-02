triplpyth = [(a,b,1000 - a - b) | a<-[1..1000], b<-[1..1000], a<b, a^2 + b^2 == (1000 - a -b)^2]

renverseur' [] rs = rs
renverseur' (h:t) rs = renverseur' t (h:rs)

renverseur l = renverseur' l []

delete e [] = []
delete e (h:t) = if e == h then t else (h:(delete e t))

maxi' [] m = m
maxi' (h:t) m = if h > m then (maxi' t h) else (maxi' t m)

maxi [] = error "maxi: errur liste vide"
maxi (h:t) = maxi' t h

trimax::[Integer]->[Integer]
trimax [] = []
trimax l = ((maxi l):(trimax (delete (maxi l) l)))

tri l = renverseur (trimax l)

main = do
    print triplpyth
    print (renverseur [1..10])
    print (Main.delete 4 [1..10])
    print (Main.maxi (Main.delete 10 [1..10]))
    print (Main.tri [1,4,2,8,7,22,11])

