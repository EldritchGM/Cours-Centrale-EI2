data Entier = One | Two | Five | Valeur Integer Integer

valeur::Entier->Integer
valeur One = 1
valeur Two = 2
valeur Five = 5
valeur (Valeur t q) = 3 * t + 4 * q

data Point = Carthesien Float Float | Polaire Float Float

dOrigine::Point->Float
dOrigine (Polaire r theta) = r
dOrigine (Carthesien x y) = sqrt (x^2 + y^2)

data ExprA = Node (Int->Int->Int) ExprA ExprA| Root Int

expr = Node (+) (Root 1) (Node (*) (Root 2) (Root 3))

evaluate::ExprA->Int
evaluate (Root x) = x
evaluate (Node ope filsG filsD) = ope (evaluate filsG) (evaluate filsD)