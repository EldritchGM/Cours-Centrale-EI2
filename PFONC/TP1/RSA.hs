import Data.Char
import Data.List

data Message = Message [Integer] deriving Show
e = 65537


stringToInt::String->[Integer]
stringToInt [] = []
stringToInt (h:t) = toInteger(ord(h)):stringToInt(t)

stringToMessage::String->Message
stringToMessage s = Message(stringToInt(s))


messageToString::Message->String
messageToString (Message []) = ""
messageToString (Message (h:t)) = chr(fromIntegral(h)):messageToString(Message(t))

pad::Int->Message->Message
pad bloc (Message(int_list)) = 
    let n = bloc - ((length int_list) `mod` bloc) in
        if n ==0 then 
            Message $ concat [int_list, (take bloc (repeat (toInteger bloc)))]
            else
                Message $ concat [int_list, (take n (repeat (toInteger n)))]

unpad::Message->Message
unpad (Message int_list) =
    let x = fromIntegral $ last int_list in
    Message (reverse $ drop x $ reverse int_list)

groupBytes'::[Integer]->Integer
groupBytes' [] = 0
groupBytes' (h:t) = h + 256 * groupBytes' t

groupBytes::[Integer]->Integer
groupBytes l = groupBytes' $ reverse l

ungroupBytes'::Integer->[Integer]
ungroupBytes' 0 = []
ungroupBytes' gb = 
    let x = (fromIntegral gb) `mod` 256 in
        let y = fromIntegral (gb - x) in
            x:(ungroupBytes' $ toInteger $ round (y/256))


ungroupBytes::Integer->[Integer]
ungroupBytes gb = reverse $ ungroupBytes' gb

groupN'::Int->[Integer]->[Integer]->[[Integer]]->[[Integer]]
groupN' bsize [] [] total = reverse total
groupN' bsize [] current total = (groupN' bsize [] [] ((reverse current):total))
groupN' bsize (h:t) current total =
    if (length current == bsize) then (groupN' bsize (h:t) [] ((reverse current):total))
    else                              (groupN' bsize t (h:current) total)

groupN::Int->[Integer]->[[Integer]]
groupN bsize l = groupN' bsize l [] []

makeBlocks::Int->Message->Message
makeBlocks bsize (Message int_list) = Message $ map groupBytes (groupN bsize int_list)

splitBlocks::Int->Message->Message
splitBlocks bsize (Message int_list) = Message $ concat $ map ungroupBytes int_list

prime::Integer->Bool
prime 1 = False
prime 2 = True
prime 3 = True 
prime 5 = True
prime n = not (any (\x -> (mod n x) == 0) $ concat [[2,3], [6 * k - 1| k <- [1..(round (((sqrt $ fromIntegral n) +1)/6))]], [6 * k + 1| k <- [1..(round (((sqrt $ fromIntegral n) - 1)/6))]]])

chooseprime::Integer->Integer
chooseprime b = if prime b then b else chooseprime (b+1)

euclid'::Integer->Integer->Integer->Integer->Integer->Integer->(Integer,Integer,Integer)
euclid' a 0 ua va ub vb = (a,ua,va)
euclid' a b ua va ub vb = 
    let q = fromIntegral $ div a b in
        euclid' b (a `rem` b) ub vb (ua - q * ub) (va - q * vb)

euclid::Integer->Integer->(Integer,Integer,Integer)
euclid a b = euclid' a b 1 0 0 1

modInv e n = let (x,y,z) = euclid e n in mod y n

modExp::Integer->Integer->Integer->Integer
modExp x 0 n = 1
modExp x p n = if p `mod` 2 == 0 
    then (modExp (x^2) (p `div` 2) n) 
    else mod ((x `mod` n) * ((modExp x (p-1) n) `mod` n)) n

--encrypt message 

encrypt_blocks::(Integer, Integer)->Message->Message
encrypt_blocks (e,n) (Message m) = Message (map (\x -> modExp x e n) m)

encrypt::(Integer, Integer)->Int->String->Message
encrypt (e,n) bsize chaine =
    let message = makeBlocks bsize $ pad bsize $ stringToMessage chaine in encrypt_blocks (e,n) message

decrypt_blocks::(Integer, Integer)->Message->Message
decrypt_blocks (d,n) (Message c) = Message (map (\x -> modExp x d n) c)

decrypt::(Integer,Integer)->Int->Message->String
decrypt (d,n) bsize message = do
    let decrypt = decrypt_blocks (d,n) message in messageToString $ unpad $ (splitBlocks bsize decrypt)

len (Message liste) = length liste

main = do 
    let message = "okok"
    let bsize = 5
    let p = chooseprime (256^bsize + 1)
    let q = 2
    let n = p*q
    let crypte = encrypt (e,n) bsize message
    print $ len crypte
    let d = modInv e ((p-1)*(q-1))
    let decrypte = decrypt (d,n) bsize crypte
    print decrypte
