--map::(a->b)->[a]->[b]

flipper::(a->b->c)->(b->a->c)
flipper f a b = f b a

main = print (flip (-) 1 3)
