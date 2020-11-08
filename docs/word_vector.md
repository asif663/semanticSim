One mathematical way of representing words is as vectors.There are an estimated 13 million words in English language. But many of these are related. So do we want separate vectors for all 13 million words?
No. We must search for a N-dimensional vector space (where N << 13 million) that is sufficient to encode all semantics in our language. We need to have a sense of similarity and difference between words. We can exploit concept of vectors and distances between them (Cosine, Euclidean etc. ) to find similarities and differences between words.

Euclidean distance(L2 Normns) :- ((x2-x1)**2 + (y2-y1)**2 )**(1/2)
Manhattan distance(L1 Normns) :-|x2-x1|+|y2-y1|

Lp is minkowski, if p==1 then manhattan if 2 then euclidean 

cosine similarity is inversly proportional to cosine distance
1- cosine_sim  = cosine distance
cosine_sim = cos@


How word can be seen as vector:-

It’s like numbers are language, like all the letters in the language are turned into numbers, and so it’s something that everyone understands the same way. You lose the sounds of the letters and whether they click or pop or touch the palate, or go ooh or aah, and anything that can be misread or con you with its music or the pictures it puts in your mind, all of that is gone, along with the accent, and you have a new understanding entirely, a language of numbers, and everything becomes as clear to everyone as the writing on the wall. So as I say there comes a certain time for the reading of the numbers.

Now let’s see what are all the ways to convert sentences into vectors.

Word2Vec — From Google
Fasttext — From Facebook
Glove — From Standford